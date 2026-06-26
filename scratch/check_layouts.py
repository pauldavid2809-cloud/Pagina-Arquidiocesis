# -*- coding: utf-8 -*-
import os

root_dir = r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main"
html_files = [f for f in os.listdir(root_dir) if f.endswith(".html")]

print(f"{'Filename':<30} | {'Has Navbar Comm':<15} | {'Has Navbar Place':<16} | {'Has Footer Comm':<15} | {'Has Footer Place':<16}")
print("-" * 105)

for f in html_files:
    path = os.path.join(root_dir, f)
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        has_nav_comm = "<!-- TopNavBar -->" in content
        has_nav_place = 'id="stitch-navbar"' in content
        has_foot_comm = "<!-- StitchFooter -->" in content
        has_foot_place = 'id="stitch-footer"' in content
        print(f"{f:<30} | {str(has_nav_comm):<15} | {str(has_nav_place):<16} | {str(has_foot_comm):<15} | {str(has_foot_place):<16}")
