import os
import re

# ─── Configuración ────────────────────────────────────────────────────────────
dir_path = r"."  # Carpeta del proyecto
# ─────────────────────────────────────────────────────────────────────────────

# 1. Nueva fuente a agregar en el <head>
old_font_link = 'href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap"'
new_font_link = 'href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Poppins:wght@700&display=swap"'

# 2. Cambiar el estilo del logo en el HTML
# De:
old_logo_h1 = '<div class="logo-text"><h1>Arquidiócesis</h1><p>de Maracaibo</p></div>'
# A:
new_logo_h1 = '<div class="logo-text"><h1 style="font-family:\'Rotis Sans Serif\',\'Gill Sans\',\'Trebuchet MS\',sans-serif;">Arquidiócesis</h1><p style="font-family:\'Poppins\',sans-serif;font-weight:700;color:#003366;">de Maracaibo</p></div>'

# También hay versiones con espacios distintos, cubrimos ambas
old_logo_h1_b = '<div class="logo-text">\n                    <h1>Arquidiócesis</h1>\n                    <p>de Maracaibo</p>\n                </div>'
new_logo_h1_b = '<div class="logo-text">\n                    <h1 style="font-family:\'Rotis Sans Serif\',\'Gill Sans\',\'Trebuchet MS\',sans-serif;">Arquidiócesis</h1>\n                    <p style="font-family:\'Poppins\',sans-serif;font-weight:700;color:#003366;">de Maracaibo</p>\n                </div>'

updated = 0
skipped = 0

html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join(dir_path, filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Actualizar el link de fuentes
    if old_font_link in content:
        content = content.replace(old_font_link, new_font_link)
        changed = True

    # Actualizar el logo (versión compacta)
    if old_logo_h1 in content:
        content = content.replace(old_logo_h1, new_logo_h1)
        changed = True

    # Actualizar el logo (versión con saltos de línea)
    if old_logo_h1_b in content:
        content = content.replace(old_logo_h1_b, new_logo_h1_b)
        changed = True

    # Regex de respaldo para cualquier variante
    pattern = re.compile(
        r'<div class="logo-text">\s*<h1>(Arquidi[oó]cesis)<\/h1>\s*<p>(de Maracaibo)<\/p>\s*<\/div>',
        re.IGNORECASE
    )
    if pattern.search(content):
        content = pattern.sub(
            '<div class="logo-text">'
            '<h1 style="font-family:\'Rotis Sans Serif\',\'Gill Sans\',\'Trebuchet MS\',sans-serif;">\\1</h1>'
            '<p style="font-family:\'Poppins\',sans-serif;font-weight:700;color:#003366;">\\2</p>'
            '</div>',
            content
        )
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f"  [actualizado] {filename}")
    else:
        skipped += 1
        print(f"  [sin cambios] {filename}")

print(f"\n✅ Listo: {updated} archivos actualizados, {skipped} sin cambios.")
print("\nNota: 'Rotis Sans Serif' es una fuente de pago (Adobe Fonts).")
print("Si no la tienes instalada, el navegador usará 'Gill Sans' o 'Trebuchet MS' como alternativa.")
print("Para usarla en web necesitas licencia de Adobe Fonts o un archivo .woff2 propio.")
