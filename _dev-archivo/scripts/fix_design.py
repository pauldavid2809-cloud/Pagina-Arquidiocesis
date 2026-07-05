# -*- coding: utf-8 -*-
import os
import re

dir_path = r"."

# ─── 1. CORREGIR LA FLECHA "EXPLORAR" EN index.html ──────────────────────────
# El problema: hero-scroll está dentro de hero-content, debe estar fuera
index_path = os.path.join(dir_path, 'index.html')
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        idx = f.read()

    # Quitar el hero-scroll de dentro de hero-content
    idx = idx.replace(
        '''        <div class="hero-scroll">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
            Explorar
        </div>''',
        ''
    )

    # Insertarlo DESPUÉS del cierre de hero-content y ANTES del cierre de section.hero
    idx = idx.replace(
        '    </div>\n</section>',
        '''    </div>
    <div class="hero-scroll">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
        Explorar
    </div>
</section>''',
        1  # solo primera ocurrencia (el hero)
    )

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(idx)
    print("  [OK] Flecha Explorar movida al lugar correcto en index.html")

# ─── 2. ACTUALIZAR FUENTES EN directorio.html Y noticias.html ────────────────
# Estos archivos tienen sus fuentes hardcodeadas en <style> interno
# Necesitamos actualizar la referencia de Google Fonts Y las variables CSS

targets = ['directorio.html', 'noticias.html', 'directorio_wa.html']

old_fonts_variants = [
    "https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap",
    "https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Poppins:wght@700&display=swap",
]
new_fonts = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&family=Poppins:wght@700;800&display=swap"

# Variables CSS viejas -> nuevas dentro de <style> de cada archivo
old_vars = """        :root {
            --color-primary: #003366;
            --color-secondary: #FFCC00;
            --color-danger: #B23A48;
            --color-bg: #F8F9FA;
            --color-text: #333333;
            --color-text-light: #666666;
            --color-border: #E5E7EB;"""

new_vars = """        :root {
            --color-primary: #003366;
            --color-secondary: #FFCC00;
            --color-danger: #B23A48;
            --color-bg: #FAF8F4;
            --color-text: #1a1a2e;
            --color-text-light: #5a6478;
            --color-border: #e8e6e0;"""

# Fuente en variables CSS internas
font_body_old  = "--font-body: 'Manrope', sans-serif;"
font_body_new  = "--font-body: 'Inter', system-ui, sans-serif;"
font_head_old  = "--font-heading: 'Playfair Display', serif;"
font_head_new  = "--font-heading: 'Cormorant Garamond', Georgia, serif;"

for filename in targets:
    fp = os.path.join(dir_path, filename)
    if not os.path.exists(fp):
        print("  [--] {} no encontrado".format(filename))
        continue

    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()

    changed = False

    # Fuentes de Google
    for old_f in old_fonts_variants:
        if old_f in c:
            c = c.replace(old_f, new_fonts)
            changed = True

    # Variables de color
    if old_vars in c:
        c = c.replace(old_vars, new_vars)
        changed = True

    # Variables de fuente
    if font_body_old in c:
        c = c.replace(font_body_old, font_body_new)
        changed = True
    if font_head_old in c:
        c = c.replace(font_head_old, font_head_new)
        changed = True

    # Variante con color-text: #333333 pero sin el bloque completo
    c = c.replace("color: var(--font-body, 'Manrope')", "color: var(--font-body, 'Inter')")
    c = c.replace("font-family: 'Manrope'", "font-family: 'Inter'")
    c = c.replace("font-family: var(--font-body), 'Manrope'", "font-family: var(--font-body), 'Inter'")

    if changed:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        print("  [OK] {} actualizado".format(filename))
    else:
        print("  [--] {} sin cambios detectados (revisa manualmente)".format(filename))

# ─── 3. ACTUALIZAR TODOS LOS HTML RESTANTES (pasada general) ─────────────────
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
general_updated = 0
for filename in html_files:
    fp = os.path.join(dir_path, filename)
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    changed = False
    for old_f in old_fonts_variants:
        if old_f in c:
            c = c.replace(old_f, new_fonts)
            changed = True
    if changed:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        general_updated += 1

print("  [OK] Fuentes actualizadas en {} archivos adicionales".format(general_updated))

print("""
Correcciones aplicadas:
  1. Flecha 'Explorar' movida debajo de los botones del hero
  2. directorio.html - fuentes y colores actualizados
  3. noticias.html   - fuentes y colores actualizados
  4. Todos los HTML  - fuentes de Google sincronizadas
""")
