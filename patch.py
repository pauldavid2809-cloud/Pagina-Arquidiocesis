import re
import os

# Update generate_static.js
with open('generate_static.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace placeholder with specific image
js = js.replace(
    "const imgSrc = p.image ? p.image : 'https://placehold.co/600x400/eeeeee/999999?text=Foto+del+Templo';",
    "const imgSrc = p.image ? p.image : `img/templos/${p.code}.webp`;"
)
# Update onerror
js = js.replace(
    "onerror=\"this.src='https://placehold.co/600x400/eeeeee/999999?text=Foto+del+Templo'\"",
    "onerror=\"this.src='img/foto_templo.webp'\""
)

with open('generate_static.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Read directorio.html
with open('directorio.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replacer(match):
    name = match.group(1)
    code = match.group(2)
    details = match.group(3)
    src = match.group(4)
    alt = match.group(5)
    
    if "img/templos/" in src: return match.group(0)
    
    new_src = f"img/templos/{code}.webp"
    err = "this.src='img/foto_templo.webp'"
    
    return f"""<div class="parish-card animate-fade-in-up" data-name="{name}" data-code="{code}" data-details="{details}">
            <img src="{new_src}" alt="{alt}" class="parish-card-img" onerror="{err}">"""

# Regex properly captures the structure of each parish card
pattern = re.compile(r'<div class="parish-card animate-fade-in-up" data-name="([^"]*)" data-code="([^"]*)" data-details="([^"]*)">\s*<img src="([^"]*)" alt="([^"]*)" class="parish-card-img" onerror="[^"]*">')

# Perform substitution
html = pattern.sub(replacer, html)

with open('directorio.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated HTML successfully")
