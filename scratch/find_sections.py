# -*- coding: utf-8 -*-
with open(r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main\arquidiocesis.html", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

# Let's search for tags or comments after line 1100
for idx in range(1100, len(lines)):
    line = lines[idx].strip()
    if line.startswith("<!--") or "<section" in line or "</main>" in line:
        print(f"Line {idx+1}: {line}")
