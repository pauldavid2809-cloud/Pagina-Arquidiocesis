# -*- coding: utf-8 -*-
import os
import re

root_dir = r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main"
html_files = [f for f in os.listdir(root_dir) if f.endswith(".html") and not f.endswith("_backup.html") and not f.endswith("_good.html")]

print(f"{'Filename':<30} | {'File Size (KB)':<15} | {'Section Count':<15} | {'Main Tag Count':<15} | {'Div Count':<10}")
print("-" * 95)

for f in sorted(html_files):
    path = os.path.join(root_dir, f)
    size_kb = os.path.getsize(path) / 1024.0
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
    
    # Extract body
    body_m = re.search(r'<body[^>]*>(.*)</body>', content, re.I | re.S)
    if body_m:
        body = body_m.group(1)
    else:
        body = content
        
    sections = len(re.findall(r'<section\b', body, re.I))
    mains = len(re.findall(r'<main\b', body, re.I))
    divs = len(re.findall(r'<div\b', body, re.I))
    
    print(f"{f:<30} | {size_kb:<15.2f} | {sections:<15} | {mains:<15} | {divs:<10}")
