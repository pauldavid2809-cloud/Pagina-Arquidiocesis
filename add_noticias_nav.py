import os
import re

# ─── Configuración ────────────────────────────────────────────────────────────
# Cambia esta ruta a la carpeta donde tienes tus HTML
dir_path = r"."   # Si lo corres desde la carpeta del proyecto, déjalo así
                  # Si no, pon la ruta completa, ej: r"C:\Users\luxmu\OneDrive\Escritorio\Web Arquidiócesis"

# Línea que queremos insertar
new_link = '                <a href="noticias.html">Noticias</a>'

# La insertamos DESPUÉS del link de Pastoral
anchor = '<a href="pastoral.html">Pastoral</a>'
# ─────────────────────────────────────────────────────────────────────────────

updated = 0
skipped = 0
already = 0

html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join(dir_path, filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Si ya tiene el link de noticias, no tocar
    if 'href="noticias.html"' in content:
        already += 1
        print(f"  [ya tiene] {filename}")
        continue

    # Si no tiene el anchor de pastoral, saltar
    if anchor not in content:
        skipped += 1
        print(f"  [sin anchor] {filename}")
        continue

    # Insertar el nuevo link justo después del anchor
    new_content = content.replace(
        anchor,
        anchor + '\n' + new_link
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    updated += 1
    print(f"  [actualizado] {filename}")

print(f"\n✅ Listo: {updated} actualizados, {already} ya tenían el link, {skipped} sin anchor.")
