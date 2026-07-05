import os, re

images = {}
for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, encoding='utf-8') as file:
            content = file.read()
            # find all src attributes in img tags
            for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', content):
                src = m.group(1)
                images.setdefault(src, []).append(f)

with open('temp_img_list.txt', 'w', encoding='utf-8') as out:
    for src in sorted(images.keys()):
        files = images[src]
        out.write(f"{src} (usado en: {', '.join(set(files))})\n")
