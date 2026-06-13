import json

with open('parishes.json', 'r', encoding='utf-8') as f:
    parishes = json.load(f)

# Build full name from raw_details title lines
results = []
for p in parishes:
    raw = p['raw_details']
    lines = raw.split('\n')
    title_parts = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        low = line.lower()
        # Stop when we hit detail content
        if any(low.startswith(x) for x in ['fundada', 'pbro', 'rif', 'r.p', 'secretari', 'email', '-']):
            break
        if any(c.isdigit() for c in line[:4]):
            break
        title_parts.append(line)
    full_name = ' '.join(title_parts) if title_parts else p['name']
    results.append((p['code'], full_name))

# Print organized by zone
zones = {}
for code, name in results:
    z = code.split('-')[0]
    if z not in zones:
        zones[z] = []
    zones[z].append((code, name))

zone_names = {
    'PZ1': 'Zona 1: Chiquinquirá',
    'PZ2': 'Zona 2: Sagrado Corazón',
    'PZ3': 'Zona 3: La Sagrada Familia',
    'PZ4': 'Zona 4: Nuestra Señora de Coromoto',
    'PZ5': 'Zona 5: San Francisco',
    'PZ6': 'Zona 6: Fátima',
    'PZ7': 'Zona 7: San Bartolomé Apóstol',
    'PZ8': 'Zona 8: La Inmaculada Concepción',
}

with open('lista_completa_templos.txt', 'w', encoding='utf-8') as out:
    total = 0
    for z in sorted(zones.keys()):
        zname = zone_names.get(z, z)
        items = zones[z]
        out.write(f"\n**{zname}** ({len(items)} parroquias)\n")
        for code, name in items:
            out.write(f"- `img/templos/{code}.webp` → {name}\n")
            total += 1
    out.write(f"\n**TOTAL: {total} imágenes de templos**\n")
    out.write(f"+ `img/foto_templo.webp` → Imagen genérica de respaldo\n")

print(f"Lista generada con {total} entradas")

# Also print zone counts
for z in sorted(zones.keys()):
    print(f"  {zone_names.get(z, z)}: {len(zones[z])} parroquias")
