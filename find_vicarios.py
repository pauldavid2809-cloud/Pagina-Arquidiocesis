import json
with open('parishes.json', 'r', encoding='utf-8') as f:
    parishes = json.load(f)
for p in parishes:
    rd = p['raw_details'].lower()
    if 'vicario' in rd or 'diácono' in rd or 'diacono' in rd:
        print(f"{p['code']}: {p['name'][:40]}")
