// Mantiene activo el proyecto de Supabase (el plan gratuito pausa los
// proyectos tras ~7 días sin peticiones a la API). Un cron de Vercel
// invoca este endpoint a diario (ver "crons" en vercel.json).

const SUPABASE_URL = process.env.SUPABASE_URL;
const ANON_KEY = process.env.SUPABASE_ANON_KEY;

export default async function handler(req, res) {
  // La respuesta nunca debe servirse desde la caché del CDN:
  // el objetivo es que cada invocación llegue a Supabase.
  res.setHeader('Cache-Control', 'no-store');

  if (!SUPABASE_URL || !ANON_KEY) {
    return res.status(500).json({ ok: false, error: 'Faltan las variables SUPABASE_URL / SUPABASE_ANON_KEY' });
  }

  try {
    const r = await fetch(`${SUPABASE_URL}/rest/v1/noticias?select=id&limit=1`, {
      headers: {
        apikey: ANON_KEY,
        Authorization: `Bearer ${ANON_KEY}`
      }
    });

    if (!r.ok) {
      const detail = await r.text().catch(() => '');
      return res.status(502).json({ ok: false, status: r.status, detail: detail.slice(0, 200) });
    }

    return res.status(200).json({ ok: true, pinged: new Date().toISOString() });
  } catch (err) {
    return res.status(502).json({ ok: false, error: String(err && err.message || err) });
  }
}
