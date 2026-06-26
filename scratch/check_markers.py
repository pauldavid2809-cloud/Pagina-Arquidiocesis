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
    "ambientes-escucha.html",
    "ambientes-formacion.html",
    "ambientes-marco-legal.html",
    "ambientes-contacto.html",
]

print(f"{'Page':<27} | {'Navbar Count':<12} | {'Footer Count':<12} | {'Tailwind Config':<15} | {'Style Count':<12}")
print("-" * 88)

for p in pages:
    path = os.path.join(root_dir, p)
    if not os.path.exists(path):
        print(f"{p:<27} : DOES NOT EXIST")
        continue
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # We count Navbar markers
    nav_count = content.count("<!-- TopNavBar -->")
    # We count StitchFooter markers
    foot_count = content.count("<!-- StitchFooter -->")
    # We count tailwind config tags
    tw_count = content.count('id="tailwind-config"')
    # We count total style tags
    style_count = len(re.findall(r'<style\b', content, re.I))
    
    print(f"{p:<27} | {nav_count:<12} | {foot_count:<12} | {tw_count:<15} | {style_count:<12}")
