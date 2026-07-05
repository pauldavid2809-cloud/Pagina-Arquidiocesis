import { handleCors } from './_cors.js';

/**
 * API de Noticias editoriales de la Arquidiócesis.
 *
 *   GET    /api/noticias            -> lista pública de noticias publicadas
 *   POST   /api/noticias            -> crea una noticia (requiere editor válido)
 *   DELETE /api/noticias            -> elimina una noticia (requiere editor válido)
 *
 * Autenticación de escritura: se reutiliza el sistema de login existente.
 * El editor envía { email, password }; se validan contra la tabla `sacerdotes`
 * (rol 'admin' o 'editor') del lado del servidor. Las escrituras y la subida de
 * imágenes usan la SERVICE ROLE key (nunca se expone al navegador).
 */

const SUPABASE_URL = process.env.SUPABASE_URL;
const ANON_KEY = process.env.SUPABASE_ANON_KEY;
// Para escrituras seguras. Si no está, se cae al anon key (requiere RLS permisiva).
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY;
const BUCKET = 'noticias';
const EDITOR_ROLES = ['admin', 'editor'];

function sbHeaders(key, extra = {}) {
  return { apikey: key, Authorization: `Bearer ${key}`, ...extra };
}

function parseBody(req) {
  if (typeof req.body === 'string') {
    try { return JSON.parse(req.body); } catch { return {}; }
  }
  return req.body || {};
}

// Valida credenciales del editor contra la tabla `sacerdotes`.
async function validateEditor(email, password) {
  if (!email || !password) return { ok: false, error: 'Faltan credenciales.' };
  const url = `${SUPABASE_URL}/rest/v1/sacerdotes?email=eq.${encodeURIComponent(email.trim().toLowerCase())}&select=email,password,role`;
  const res = await fetch(url, { headers: sbHeaders(SERVICE_KEY) });
  if (!res.ok) return { ok: false, error: 'No se pudo validar el usuario.' };
  const rows = await res.json();
  if (!rows || rows.length === 0) return { ok: false, error: 'Usuario no registrado.' };
  const user = rows[0];
  if (user.password !== password) return { ok: false, error: 'Contraseña incorrecta.' };
  if (!EDITOR_ROLES.includes((user.role || '').toLowerCase())) {
    return { ok: false, error: 'Este usuario no tiene permiso para publicar noticias.' };
  }
  return { ok: true, user };
}

// Sube una imagen (base64) a Supabase Storage y devuelve su URL pública.
async function uploadImage(base64, mime) {
  const ext = (mime && mime.split('/')[1] || 'jpg').replace('jpeg', 'jpg');
  const name = `${Date.now()}-${Math.random().toString(36).slice(2, 8)}.${ext}`;
  const bytes = Buffer.from(base64, 'base64');
  const upUrl = `${SUPABASE_URL}/storage/v1/object/${BUCKET}/${name}`;
  const res = await fetch(upUrl, {
    method: 'POST',
    headers: sbHeaders(SERVICE_KEY, { 'Content-Type': mime || 'image/jpeg', 'x-upsert': 'true' }),
    body: bytes
  });
  if (!res.ok) {
    const t = await res.text().catch(() => '');
    throw new Error(`No se pudo subir la imagen: ${res.status} ${t}`);
  }
  return `${SUPABASE_URL}/storage/v1/object/public/${BUCKET}/${name}`;
}

export default async function handler(req, res) {
  if (!handleCors(req, res)) return;

  if (!SUPABASE_URL || !ANON_KEY) {
    return res.status(500).json({ error: 'Supabase no está configurado en el servidor.' });
  }

  // ── LISTA PÚBLICA ───────────────────────────────────────────────
  if (req.method === 'GET') {
    try {
      const includeAll = req.query.all === 'true';
      let url = `${SUPABASE_URL}/rest/v1/noticias?select=*&order=timestamp.desc`;
      if (!includeAll) url += `&published=eq.true`;
      const r = await fetch(url, { headers: sbHeaders(SERVICE_KEY) });
      if (!r.ok) return res.status(r.status).json({ error: 'No se pudieron obtener las noticias.' });
      const data = await r.json();
      res.setHeader('Cache-Control', 's-maxage=60, stale-while-revalidate=300');
      return res.status(200).json({ data });
    } catch (err) {
      return res.status(500).json({ error: 'Error al leer noticias', details: err.message });
    }
  }

  // ── CREAR ───────────────────────────────────────────────────────
  if (req.method === 'POST') {
    const body = parseBody(req);
    const auth = await validateEditor(body.email, body.password);
    if (!auth.ok) return res.status(401).json({ error: auth.error });

    const n = body.news || {};
    if (!n.title || !String(n.title).trim()) {
      return res.status(400).json({ error: 'El título es obligatorio.' });
    }

    try {
      let media_url = n.media_url || '';
      if (body.imageBase64) {
        media_url = await uploadImage(body.imageBase64, body.imageMime);
      }

      const row = {
        title: String(n.title).trim(),
        caption: n.caption ? String(n.caption).trim() : '',
        tag: n.tag ? String(n.tag).trim() : 'Actualidad',
        media_url,
        permalink: n.permalink ? String(n.permalink).trim() : 'https://www.instagram.com/arquimcbo/',
        timestamp: n.timestamp || new Date().toISOString(),
        published: n.published !== false,
        author: auth.user.email
      };

      const r = await fetch(`${SUPABASE_URL}/rest/v1/noticias`, {
        method: 'POST',
        headers: sbHeaders(SERVICE_KEY, { 'Content-Type': 'application/json', Prefer: 'return=representation' }),
        body: JSON.stringify(row)
      });
      if (!r.ok) {
        const t = await r.text().catch(() => '');
        return res.status(r.status).json({ error: 'No se pudo guardar la noticia.', details: t });
      }
      const created = await r.json();
      return res.status(201).json({ success: true, news: Array.isArray(created) ? created[0] : created });
    } catch (err) {
      return res.status(500).json({ error: 'Error al crear la noticia', details: err.message });
    }
  }

  // ── ELIMINAR ────────────────────────────────────────────────────
  if (req.method === 'DELETE') {
    const body = parseBody(req);
    const auth = await validateEditor(body.email, body.password);
    if (!auth.ok) return res.status(401).json({ error: auth.error });
    if (!body.id) return res.status(400).json({ error: 'Falta el id de la noticia.' });

    try {
      const r = await fetch(`${SUPABASE_URL}/rest/v1/noticias?id=eq.${encodeURIComponent(body.id)}`, {
        method: 'DELETE',
        headers: sbHeaders(SERVICE_KEY, { Prefer: 'return=minimal' })
      });
      if (!r.ok) {
        const t = await r.text().catch(() => '');
        return res.status(r.status).json({ error: 'No se pudo eliminar la noticia.', details: t });
      }
      return res.status(200).json({ success: true });
    } catch (err) {
      return res.status(500).json({ error: 'Error al eliminar la noticia', details: err.message });
    }
  }

  return res.status(405).json({ error: 'Método no permitido' });
}
