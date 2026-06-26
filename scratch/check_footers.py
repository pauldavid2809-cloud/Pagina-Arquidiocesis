# -*- coding: utf-8 -*-
import os
import re

root_dir = r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main"
html_files = [f for f in os.listdir(root_dir) if f.endswith(".html") and not f.endswith("_backup.html") and not f.endswith("_good.html")]

print(f"{'Filename':<30} | {'Footer Tag Count':<20} | {'bg-surface-container-lowest':<30}")
print("-" * 85)

for f in sorted(html_files):
    path = os.path.join(root_dir, f)
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        
    footers = len(re.findall(r'<footer\b', content, re.I))
    lowest_surface = content.count("bg-surface-container-lowest")
    
    print(f"{f:<30} | {footers:<20} | {lowest_surface:<30}")
