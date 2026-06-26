# -*- coding: utf-8 -*-
import os

path = r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main\donaciones.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if "bg-surface-container-lowest" in line:
        print(f"Line {idx+1}: {line.strip()[:100]}")
