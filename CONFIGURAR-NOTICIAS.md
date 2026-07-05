# Configurar el panel de noticias manuales

Este panel permite que la encargada de redes publique noticias (título, texto y foto)
que aparecen **al instante** en la portada y en la página de Noticias, además del feed
automático de Instagram.

- **Panel de publicación:** `https://TU-SITIO/admin-noticias.html`
- **API:** `api/noticias.js` (ya incluida en el proyecto)

La configuración es **una sola vez**. Sigue estos 4 pasos en el panel de Supabase.

---

## Paso 1 · Crear la tabla `noticias`

En Supabase → **SQL Editor** → pega y ejecuta:

```sql
create table if not exists public.noticias (
  id          uuid primary key default gen_random_uuid(),
  title       text not null,
  caption     text default '',
  tag         text default 'Actualidad',
  media_url   text default '',
  permalink   text default 'https://www.instagram.com/arquimcbo/',
  timestamp   timestamptz default now(),
  published   boolean default true,
  author      text,
  created_at  timestamptz default now()
);

-- Seguridad a nivel de fila: las escrituras van por el servidor (service role),
-- así que sólo hace falta permitir la LECTURA pública de las noticias publicadas.
alter table public.noticias enable row level security;

create policy "Lectura pública de noticias publicadas"
  on public.noticias for select
  using ( published = true );
```

---

## Paso 2 · Crear el almacenamiento de fotos (bucket)

En Supabase → **Storage** → **New bucket**:

- **Name:** `noticias`
- **Public bucket:** ✅ **activado** (para que las fotos se vean en el sitio)

Crea el bucket. No hace falta nada más: la subida de imágenes la hace el servidor
de forma segura.

---

## Paso 3 · Añadir la clave de servicio en Vercel

Esto permite que el servidor guarde noticias y suba fotos de forma segura (esta clave
**nunca** se muestra en el navegador).

1. En Supabase → **Project Settings → API** → copia el valor de **`service_role` secret**.
2. En Vercel → tu proyecto → **Settings → Environment Variables** → añade:

   | Name                        | Value                              |
   |-----------------------------|------------------------------------|
   | `SUPABASE_SERVICE_ROLE_KEY` | *(pega la clave service_role)*     |

3. Asegúrate de que también existan `SUPABASE_URL` y `SUPABASE_ANON_KEY` (ya deberían estar,
   porque el login y el feed de Instagram las usan).
4. Haz un **Redeploy** en Vercel para que tome la variable nueva.

> ⚠️ La `service_role` es una clave sensible. Ponla **solo** en las variables de entorno
> de Vercel, nunca en el código ni en el repositorio.

---

## Paso 4 · Dar acceso a la encargada de redes

El panel reutiliza el mismo login del portal. La encargada necesita una cuenta con rol
`editor` (o `admin`) en la tabla `sacerdotes`.

En Supabase → **SQL Editor**:

```sql
-- Reemplaza el correo, el nombre y la contraseña por los reales
insert into public.sacerdotes (name, email, password, role)
values ('Encargada de Redes', 'redes@arquidiocesisdemaracaibo.org', 'CAMBIA-ESTA-CLAVE', 'editor');
```

- Si la persona **ya tiene** cuenta, basta con cambiar su rol a `editor`:
  ```sql
  update public.sacerdotes set role = 'editor'
  where email = 'su-correo@arquidiocesisdemaracaibo.org';
  ```
- El administrador (`role = 'admin'`) también puede publicar.

---

## Cómo se usa

1. La encargada entra a `https://TU-SITIO/admin-noticias.html`
   (también hay un botón directo en el **Portal de Cancillería → Instagram → “Publicar noticias manualmente”**).
2. Inicia sesión con su correo y contraseña.
3. Llena **título**, **texto**, **etiqueta**, **fecha** y elige una **foto** (se optimiza sola).
4. Pulsa **Publicar**. La noticia aparece de inmediato en la portada y en Noticias.
5. Desde la lista puede **eliminar** noticias cuando quiera.

## Notas técnicas

- Si la base de datos no está disponible, el sitio usa como respaldo el archivo
  `noticias.json` del repositorio, y luego el feed de Instagram. Nunca se queda sin noticias.
- Las noticias manuales y las de Instagram se **combinan** y se ordenan por fecha
  (más recientes primero), sin duplicados.
- El panel `admin-noticias.html` está marcado como `noindex` (no aparece en Google).
