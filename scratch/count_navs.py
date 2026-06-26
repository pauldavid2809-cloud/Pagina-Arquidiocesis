# -*- coding: utf-8 -*-
import os
import re

root_dir = r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main"
html_files = [f for f in os.listdir(root_dir) if f.endswith(".html") and not f.endswith("_backup.html") and not f.endswith("_good.html")]

for p in sorted(html_files):
    path = os.path.join(root_dir, p)
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    nav_count = len(re.findall(r'<nav\b', content, re.I))
    print(f"{p:<30} has {nav_count} <nav> tags")
