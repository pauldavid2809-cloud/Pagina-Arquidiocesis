# -*- coding: utf-8 -*-
import subprocess
import os

root_dir = r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main"
pages = [
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
]

for p in pages:
    # Get the file content in ef0b714
    try:
        content_good = subprocess.check_output(
            ["git", "show", f"ef0b714:{p}"],
            cwd=root_dir,
            stderr=subprocess.DEVNULL
        ).decode("utf-8", errors="ignore")
    except Exception:
        print(f"{p:<25} : Could not fetch version from ef0b714")
        continue

    # Get the current content
    path = os.path.join(root_dir, p)
    if not os.path.exists(path):
        print(f"{p:<25} : Missing on disk")
        continue
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content_current = f.read()

    # Compare sizes of the body (excluding nav and footer to focus on page content)
    def clean_page(html):
        # Remove nav, mobile menu, footer
        import re
        html = re.sub(r'<!--\s*TopNavBar\s*-->.*?<!--\s*End\s*TopNavBar\s*-->', '', html, flags=re.S)
        html = re.sub(r'<!--\s*TopNavBar\s*-->\s*<nav class="bg-surface/80[^"]*".*?</nav>', '', html, count=1, flags=re.S)
        html = re.sub(r'<!--\s*Mobile Drawer\s*-->.*?<!--\s*End\s*Mobile\s*Drawer\s*-->', '', html, flags=re.S)
        html = re.sub(r'<!--\s*Mobile Drawer\s*-->\s*<div id="mobileDrawer"[^>]*>.*?Hacer una Donación</a>\s*</div>\s*</div>', '', html, flags=re.S)
        html = re.sub(r'<!--\s*StitchFooter\s*-->.*?<!--\s*End\s*StitchFooter\s*-->', '', html, flags=re.S)
        html = re.sub(r'<footer class="bg-surface-container-lowest[^"]*".*?</footer>', '', html, count=1, flags=re.S)
        html = re.sub(r'<!--\s*Navbar\s*-->.*?<header class="navbar".*?</header>', '', html, count=1, flags=re.S)
        html = re.sub(r'<header class="navbar".*?</header>', '', html, count=1, flags=re.S)
        html = re.sub(r'<!--\s*Footer\s*-->.*?<footer class="footer[^"]*".*?</footer>', '', html, count=1, flags=re.S)
        html = re.sub(r'<footer class="footer[^"]*".*?</footer>', '', html, count=1, flags=re.S)
        
        # Remove common scripts and whitespace
        html = re.sub(r'<script.*?</script>', '', html, flags=re.S)
        html = re.sub(r'<style.*?</style>', '', html, flags=re.S)
        return "".join(html.split())

    cleaned_good = clean_page(content_good)
    cleaned_current = clean_page(content_current)
    
    diff_len = len(cleaned_good) - len(cleaned_current)
    ratio = len(cleaned_current) / (len(cleaned_good) or 1)
    
    print(f"{p:<25} : Good Len: {len(cleaned_good):<8} | Current Len: {len(cleaned_current):<8} | Diff: {diff_len:<8} | Ratio: {ratio:.2%}")
