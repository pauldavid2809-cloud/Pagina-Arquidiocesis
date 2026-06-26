# -*- coding: utf-8 -*-
import os
import re

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
    path = os.path.join(root_dir, p)
    if not os.path.exists(path):
        print(f"{p:<25} : DOES NOT EXIST")
        continue
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    h1s = re.findall(r'<h1\b[^>]*>(.*?)</h1>', content, re.I | re.S)
    h1_text = [h.strip() for h in h1s]
    
    # Check for hero section class or id or section
    has_hero = "hero" in content.lower() or "page-header" in content.lower()
    
    print(f"{p:<25} : H1s: {h1_text} | Has 'hero' text: {has_hero}")
