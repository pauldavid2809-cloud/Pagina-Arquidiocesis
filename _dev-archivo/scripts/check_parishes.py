import json

with open('parishes.json', 'r', encoding='utf-8') as f:
    parishes = json.load(f)

# Build full name from raw_details
for p in parishes:
    raw = p['raw_details']
    lines = raw.split('\n')
    title_parts = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        low = line.lower()
        if any(low.startswith(x) for x in ['fundada', 'pbro', 'rif', 'r.p', 'parroco', 'secretari', 'email', '-']):
            break
        if any(c.isdigit() for c in line[:4]):
            break
        title_parts.append(line)
    full_name = ' '.join(title_parts) if title_parts else p['name']
    print(f"{p['code']}: {full_name}")

print(f"\nTotal: {len(parishes)} parroquias")

# Check zones
zones = {}
for p in parishes:
    zone = p['code'].split('-')[0]
    if zone not in zones:
        zones[zone] = []
    zones[zone].append(p['code'])

print("\nPor zona:")
for z in sorted(zones.keys()):
    print(f"  {z}: {len(zones[z])} parroquias -> {sorted(zones[z])}")
