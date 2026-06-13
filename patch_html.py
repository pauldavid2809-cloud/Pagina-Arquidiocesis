import re
import json

with open('directorio.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('parishes.json', 'r', encoding='utf-8') as f:
    parishes = json.load(f)

for p in parishes:
    code = p['code']
    alt_text = p['name'].replace('"', '&quot;')
    # regex to find the block
    pattern_str = rf'(data-code="{code}"[\s\S]*?)<img[\s\S]*?class="parish-card-img"[^>]*>'
    
    def replacer(m):
        prefix = m.group(1)
        new_img = f'<img src="img/templos/{code}.webp" alt="{alt_text}" class="parish-card-img" onerror="this.src=\'img/foto_templo.webp\'">'
        return prefix + new_img

    html = re.sub(pattern_str, replacer, html, count=1)

with open('directorio.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated directorio.html!")

try:
    with open('static_cards.html', 'r', encoding='utf-8') as f:
        html_static = f.read()

    for p in parishes:
        code = p['code']
        alt_text = p['name'].replace('"', '&quot;')
        pattern_str = rf'(data-code="{code}"[\s\S]*?)<img[\s\S]*?class="parish-card-img"[^>]*>'
        
        def replacer_static(m):
            prefix = m.group(1)
            new_img = f'<img src="img/templos/{code}.webp" alt="{alt_text}" class="parish-card-img" onerror="this.src=\'img/foto_templo.webp\'">'
            return prefix + new_img

        html_static = re.sub(pattern_str, replacer_static, html_static, count=1)

    with open('static_cards.html', 'w', encoding='utf-8') as f:
        f.write(html_static)
        
    print("Updated static_cards.html!")
except Exception as e:
    print("could not update static_cards.html", e)
