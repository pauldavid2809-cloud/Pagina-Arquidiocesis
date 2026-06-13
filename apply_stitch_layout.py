# -*- coding: utf-8 -*-
"""Apply Stitch design shell (from index.html) to all inner pages."""

import os
import re

DIR = os.path.dirname(os.path.abspath(__file__))

PAGES = [
    "arquidiocesis.html",
    "arzobispo.html",
    "pastoral.html",
    "noticias.html",
    "directorio.html",
    "donaciones.html",
    "cancilleria.html",
    "seminario.html",
    "vida-consagrada.html",
    "ambientes.html",
    "portal-sacerdotes.html",
]

STITCH_HEAD = """<!DOCTYPE html>
<html class="light" lang="es">
<head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<meta name="description" content="{description}">
<title>{title}</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@100..900&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/stitch-pages.css">
{extra_head}
<script id="tailwind-config">
        tailwind.config = {{
            darkMode: "class",
            theme: {{
                extend: {{
                    "colors": {{
                        "inverse-on-surface": "#f4eeff",
                        "on-primary-fixed-variant": "#474364",
                        "outline-variant": "#c9c5ce",
                        "surface-variant": "#e5e0f3",
                        "outline": "#78767e",
                        "on-tertiary": "#ffffff",
                        "primary-fixed-dim": "#c8c2ea",
                        "background": "#fdf8ff",
                        "tertiary-fixed-dim": "#c8c5ce",
                        "secondary-container": "#cabafe",
                        "on-secondary-fixed": "#1f0f4a",
                        "inverse-primary": "#c8c2ea",
                        "tertiary-container": "#212127",
                        "on-surface": "#1c1a27",
                        "surface-bright": "#fdf8ff",
                        "primary-container": "#211d3c",
                        "primary": "#0a0524",
                        "on-background": "#1c1a27",
                        "secondary-fixed-dim": "#cdbdff",
                        "on-secondary-container": "#554783",
                        "surface-container-high": "#ebe5f9",
                        "surface-container-highest": "#e5e0f3",
                        "tertiary": "#0a0a10",
                        "surface-container-low": "#f7f1ff",
                        "on-primary": "#ffffff",
                        "error-container": "#ffdad6",
                        "secondary": "#635592",
                        "error": "#ba1a1a",
                        "surface": "#fdf8ff",
                        "tertiary-fixed": "#e4e1ea",
                        "surface-container-lowest": "#ffffff",
                        "on-error": "#ffffff",
                        "on-tertiary-container": "#898890",
                        "secondary-fixed": "#e7deff",
                        "on-primary-fixed": "#1b1736",
                        "surface-container": "#f1ebfe",
                        "inverse-surface": "#312f3d",
                        "surface-dim": "#ddd7ea",
                        "on-surface-variant": "#48464d",
                        "on-error-container": "#93000a",
                        "surface-tint": "#5f5a7d",
                        "on-secondary": "#ffffff",
                        "on-tertiary-fixed-variant": "#46464d",
                        "on-tertiary-fixed": "#1b1b21",
                        "on-secondary-fixed-variant": "#4b3d78"
                    }},
                    "borderRadius": {{
                        "DEFAULT": "0.25rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "full": "9999px"
                    }},
                    "spacing": {{
                        "section-gap": "120px",
                        "margin-mobile": "16px",
                        "margin-desktop": "64px",
                        "container-max": "1280px",
                        "gutter": "24px"
                    }},
                    "fontFamily": {{
                        "label-sm": ["Geist"],
                        "headline-lg-mobile": ["Geist"],
                        "headline-display": ["Geist"],
                        "headline-md": ["Geist"],
                        "body-md": ["Geist"],
                        "body-lg": ["Geist"],
                        "headline-lg": ["Geist"]
                    }},
                    "fontSize": {{
                        "label-sm": ["14px", {{"lineHeight": "1.4", "letterSpacing": "0.01em", "fontWeight": "500"}}],
                        "headline-lg-mobile": ["36px", {{"lineHeight": "1.2", "fontWeight": "500"}}],
                        "headline-display": ["64px", {{"lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "500"}}],
                        "headline-md": ["32px", {{"lineHeight": "1.3", "fontWeight": "500"}}],
                        "body-md": ["16px", {{"lineHeight": "1.5", "fontWeight": "400"}}],
                        "body-lg": ["18px", {{"lineHeight": "1.6", "fontWeight": "400"}}],
                        "headline-lg": ["48px", {{"lineHeight": "1.2", "letterSpacing": "-0.01em", "fontWeight": "500"}}]
                    }}
                }}
            }}
        }}
    </script>
<style>
        body {{ background-color: #fdf8ff; color: #1c1a27; font-family: 'Geist', sans-serif; }}
        .glass-card {{ background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(20px); border: 1px solid rgba(157, 142, 207, 0.1); }}
        .hero-gradient {{ background: radial-gradient(circle at top right, #e7deff 0%, #fdf8ff 60%); }}
        .material-symbols-outlined {{ font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }}
    </style>
</head>
<body class="stitch-layout selection:bg-secondary-container selection:text-on-secondary-container overflow-x-hidden">
"""

STITCH_NAV = """
<!-- TopNavBar -->
<nav class="bg-surface/80 backdrop-blur-xl docked full-width top-0 sticky z-50 shadow-sm transition-all duration-300 py-4">
<div class="flex justify-between items-center w-full px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto">
<a href="index.html" class="flex items-center gap-3 hover:opacity-90 transition-opacity">
<img alt="Arquidiócesis de Maracaibo Logo" class="w-auto h-8" src="img/logo-arquidiocesis.webp" onerror="this.src='https://placehold.co/120x40/0a0524/ffffff?text=Arquidiocesis'">
<span class="font-headline-md text-primary tracking-tight hidden lg:block font-medium text-lg">Arquidiócesis de Maracaibo</span>
</a>
<div class="hidden md:flex items-center gap-8">
<a class="text-on-surface-variant hover:text-primary transition-colors font-label-sm text-label-sm" href="arquidiocesis.html">Arquidiócesis</a>
<a class="text-on-surface-variant hover:text-primary transition-colors font-label-sm text-label-sm" href="arzobispo.html">Arzobispo</a>
<a class="text-on-surface-variant hover:text-primary transition-colors font-label-sm text-label-sm" href="pastoral.html">Pastoral</a>
<a class="text-on-surface-variant hover:text-primary transition-colors font-label-sm text-label-sm" href="noticias.html">Noticias</a>
<a class="text-on-surface-variant hover:text-primary transition-colors font-label-sm text-label-sm" href="directorio.html">Directorio</a>
</div>
<div class="flex items-center gap-4">
<a class="bg-primary text-on-primary px-6 py-2.5 rounded-full font-label-sm text-label-sm font-bold hover:opacity-80 active:scale-95 transition-all" href="donaciones.html">Donar</a>
<button id="mobileMenuBtn" class="md:hidden text-primary p-2 focus:outline-none focus:ring-2 focus:ring-primary rounded-lg flex items-center justify-center" aria-label="Abrir menú">
<span class="material-symbols-outlined text-2xl">menu</span>
</button>
</div>
</div>
</nav>

<!-- Mobile Drawer -->
<div id="mobileDrawer" class="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm opacity-0 pointer-events-none transition-all duration-300 md:hidden">
<div class="fixed top-0 right-0 h-full w-[280px] bg-surface p-6 shadow-2xl flex flex-col justify-between translate-x-full transition-transform duration-300 ease-out" id="mobileDrawerContent">
<div>
<div class="flex justify-between items-center mb-8">
<span class="font-bold text-primary text-lg">Menú</span>
<button id="closeDrawerBtn" class="text-primary p-2 rounded-lg flex items-center justify-center" aria-label="Cerrar menú">
<span class="material-symbols-outlined text-2xl">close</span>
</button>
</div>
<div class="flex flex-col gap-5 font-medium text-base">
<a class="text-on-surface-variant hover:text-primary transition-colors py-1" href="arquidiocesis.html">Arquidiócesis</a>
<a class="text-on-surface-variant hover:text-primary transition-colors py-1" href="arzobispo.html">Arzobispo</a>
<a class="text-on-surface-variant hover:text-primary transition-colors py-1" href="pastoral.html">Pastoral</a>
<a class="text-on-surface-variant hover:text-primary transition-colors py-1" href="noticias.html">Noticias</a>
<a class="text-on-surface-variant hover:text-primary transition-colors py-1" href="directorio.html">Directorio</a>
<div class="h-px bg-outline-variant/20 my-1"></div>
<a class="text-on-surface-variant hover:text-primary transition-colors py-1 flex items-center gap-2" href="seminario.html"><span class="material-symbols-outlined text-[18px]">school</span> Seminario</a>
<a class="text-on-surface-variant hover:text-primary transition-colors py-1 flex items-center gap-2" href="vida-consagrada.html"><span class="material-symbols-outlined text-[18px]">volunteer_activism</span> Vida Consagrada</a>
<a class="text-on-surface-variant hover:text-primary transition-colors py-1 flex items-center gap-2" href="cancilleria.html"><span class="material-symbols-outlined text-[18px]">signature</span> Cancillería</a>
<a class="text-on-surface-variant hover:text-primary transition-colors py-1 flex items-center gap-2" href="ambientes.html"><span class="material-symbols-outlined text-[18px]">gavel</span> Ambientes Seguros</a>
</div>
</div>
<a class="bg-primary text-on-primary w-full text-center py-3 rounded-full font-bold hover:opacity-80 transition-all block mt-8" href="donaciones.html">Hacer una Donación</a>
</div>
</div>
"""

STITCH_FOOTER = """
<footer class="bg-surface-container-lowest border-t border-outline-variant/20 pt-20 pb-10 px-margin-mobile md:px-margin-desktop">
<div class="max-w-container-max mx-auto grid grid-cols-1 md:grid-cols-4 gap-gutter mb-20">
<div class="space-y-6">
<a href="index.html" class="flex items-center gap-3 hover:opacity-90 transition-opacity w-fit">
<img alt="Arquidiócesis Logo" class="w-auto h-10" src="img/logo-arquidiocesis.webp" onerror="this.src='https://placehold.co/120x40/0a0524/ffffff?text=Arquidiocesis'">
<span class="font-headline-md text-primary tracking-tight font-medium text-lg">Arquidiócesis de Maracaibo</span>
</a>
<p class="text-on-surface-variant font-body-md text-body-md">
"Una Iglesia en salida al encuentro"<br>
Av. 4 con calle 95, frente a la Plaza Bolívar.<br>
Maracaibo, Estado Zulia, Venezuela.
</p>
<div class="flex gap-4">
<a class="w-10 h-10 rounded-full bg-surface-container-high flex items-center justify-center text-primary hover:bg-primary hover:text-white transition-all" href="https://www.instagram.com/arquimcbo/" target="_blank" rel="noopener" aria-label="Instagram">
<span class="material-symbols-outlined text-[20px]">share</span>
</a>
<a class="w-10 h-10 rounded-full bg-surface-container-high flex items-center justify-center text-primary hover:bg-primary hover:text-white transition-all" href="https://www.youtube.com/@arquidicosisdemaracaibo" target="_blank" rel="noopener" aria-label="YouTube">
<span class="material-symbols-outlined text-[20px]">language</span>
</a>
</div>
</div>
<div>
<h5 class="font-bold text-primary mb-8 uppercase tracking-widest text-xs">Enlaces Rápidos</h5>
<ul class="space-y-4 font-label-sm text-label-sm">
<li><a class="text-on-surface-variant hover:text-primary transition-colors" href="directorio.html">Directorio de Parroquias</a></li>
<li><a class="text-on-surface-variant hover:text-primary transition-colors" href="ambientes.html">Ambientes Seguros</a></li>
<li><a class="text-on-surface-variant hover:text-primary transition-colors" href="cancilleria.html">Cancillería</a></li>
<li><a class="text-on-surface-variant hover:text-primary transition-colors" href="donaciones.html">Donaciones</a></li>
<li><a class="text-on-surface-variant hover:text-primary transition-colors" href="noticias.html">Noticias</a></li>
<li><a class="text-on-surface-variant hover:text-primary transition-colors font-bold text-secondary" href="portal-sacerdotes.html">Portal de Sacerdotes</a></li>
</ul>
</div>
<div>
<h5 class="font-bold text-primary mb-8 uppercase tracking-widest text-xs">Instituciones</h5>
<ul class="space-y-4 font-label-sm text-label-sm">
<li><a class="text-on-surface-variant hover:text-primary transition-colors" href="seminario.html">Seminario Conciliar</a></li>
<li><a class="text-on-surface-variant hover:text-primary transition-colors" href="vida-consagrada.html">Vida Consagrada</a></li>
<li><a class="text-on-surface-variant hover:text-primary transition-colors" href="https://tribunaleclesiasticomaracaibo.org/" target="_blank" rel="noopener">Tribunal Eclesiástico</a></li>
<li><a class="text-on-surface-variant hover:text-primary transition-colors" href="pastoral.html">Vicaría de Pastoral</a></li>
<li><a class="text-on-surface-variant hover:text-primary transition-colors" href="arzobispo.html">El Arzobispo</a></li>
</ul>
</div>
<div>
<h5 class="font-bold text-primary mb-8 uppercase tracking-widest text-xs">Atención al Fiel</h5>
<div class="bg-surface-container rounded-2xl p-6 border border-outline-variant/10">
<p class="font-bold text-primary mb-2">Despacho Curia</p>
<p class="text-on-surface-variant text-sm">Lun a Vie: 8:30 AM – 1:00 PM</p>
</div>
</div>
</div>
<div class="max-w-container-max mx-auto pt-10 border-t border-outline-variant/10 flex flex-col md:flex-row justify-between items-center gap-4 text-center">
<p class="font-label-sm text-label-sm text-on-surface-variant">© 2026 Arquidiócesis de Maracaibo. Todos los derechos reservados.</p>
</div>
</footer>
<script src="js/stitch-layout.js"></script>
"""

SKIP_HEAD_PATTERNS = [
    r'<link[^>]*fonts\.googleapis\.com[^>]*>',
    r'<link[^>]*fonts\.gstatic\.com[^>]*>',
    r'<link[^>]*css/styles\.css[^>]*>',
    r'<link rel="preconnect"[^>]*>',
    r'<meta charset[^>]*>',
    r'<meta name="viewport"[^>]*>',
    r'<meta name="description"[^>]*>',
    r'<title>.*?</title>',
    r'<!DOCTYPE html>',
    r'<html[^>]*>',
    r'<head>',
    r'</head>',
]


def extract_meta(html, name):
    m = re.search(rf'<meta\s+name="{name}"\s+content="([^"]*)"', html, re.I)
    if m:
        return m.group(1)
    m = re.search(rf'<meta\s+content="([^"]*)"\s+name="{name}"', html, re.I)
    return m.group(1) if m else ""


def extract_title(html):
    m = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
    return m.group(1).strip() if m else "Arquidiócesis de Maracaibo"


def extract_extra_head(html):
    head_m = re.search(r'<head>(.*?)</head>', html, re.I | re.S)
    if not head_m:
        return ""
    head = head_m.group(1)
    for pat in SKIP_HEAD_PATTERNS:
        head = re.sub(pat, '', head, flags=re.I | re.S)
    return head.strip()


def extract_body_content(html):
    # Remove old navbar
    html = re.sub(r'<!--\s*Navbar\s*-->.*?<header class="navbar".*?</header>', '', html, count=1, flags=re.S)
    html = re.sub(r'<header class="navbar".*?</header>', '', html, count=1, flags=re.S)
    # Remove old footer
    html = re.sub(r'<!--\s*Footer\s*-->.*?<footer class="footer[^"]*".*?</footer>', '', html, count=1, flags=re.S)
    html = re.sub(r'<footer class="footer[^"]*".*?</footer>', '', html, count=1, flags=re.S)
    # Extract body inner
    body_m = re.search(r'<body[^>]*>(.*)</body>', html, re.I | re.S)
    if not body_m:
        return html
    inner = body_m.group(1).strip()
    # Remove app.js script reference (replaced by stitch-layout.js)
    inner = re.sub(r'<script\s+src="js/app\.js"\s*></script>\s*', '', inner)
    return inner.strip()


def migrate_page(filename):
    path = os.path.join(DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    title = extract_title(original)
    description = extract_meta(original, 'description') or title
    extra_head = extract_extra_head(original)
    body_content = extract_body_content(original)

    new_html = STITCH_HEAD.format(title=title, description=description, extra_head=extra_head)
    new_html += STITCH_NAV
    new_html += "\n" + body_content + "\n"
    new_html += STITCH_FOOTER
    new_html += "\n</body>\n</html>\n"

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)

    return len(body_content)


def main():
    print("Aplicando diseño Stitch a páginas locales...\n")
    for page in PAGES:
        path = os.path.join(DIR, page)
        if not os.path.exists(path):
            print(f"  [--] {page} no encontrado")
            continue
        size = migrate_page(page)
        print(f"  [OK] {page} ({size:,} chars de contenido)")

    print("\nMigración completada.")


if __name__ == '__main__':
    main()
