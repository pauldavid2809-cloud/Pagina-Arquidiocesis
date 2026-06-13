with open('directorio.html','r',encoding='utf-8') as f:
    c = f.read()

old = "onerror=\"this.src='img/foto_templo.webp'\""
new = "onerror=\"this.onerror=null;this.src='img/foto_templo.webp'\""
c = c.replace(old, new)

with open('directorio.html','w',encoding='utf-8') as f:
    f.write(c)

print('Fixed', c.count('this.onerror=null'), 'onerror handlers in directorio.html')

# Also fix static_cards.html
with open('static_cards.html','r',encoding='utf-8') as f:
    s = f.read()
s = s.replace(old, new)
with open('static_cards.html','w',encoding='utf-8') as f:
    f.write(s)

print('Fixed', s.count('this.onerror=null'), 'onerror handlers in static_cards.html')

# Also fix generate_static.js for future
with open('generate_static.js','r',encoding='utf-8') as f:
    j = f.read()
j = j.replace(old, new)
with open('generate_static.js','w',encoding='utf-8') as f:
    f.write(j)

print('Fixed generate_static.js')
