import json
import re

with open('parishes.json', 'r', encoding='utf-8') as f:
    parishes = json.load(f)

priests = set()
for p in parishes:
    raw = p['raw_details']
    lines = raw.split('\n')
    for line in lines:
        line = line.strip()
        lower = line.lower()
        if lower.startswith("pbro.") or lower.startswith("r.p.") or lower.startswith("diác") or lower.startswith("diac"):
            # Clean up the name
            name = line
            name = re.sub(r'^\s*(Pbro\.|R\.P\.|Diác\.|Diac\.|Párroco:?|Padre\s+)', '', name, flags=re.IGNORECASE)
            name = re.sub(r'\(.*?\)', '', name) # Remove anything in parens
            name = re.sub(r'\d.*', '', name) # Remove numbers
            name = name.split('Email:')[0]
            name = name.split('Telf')[0]
            name = name.split('–')[0]
            name = name.split('- ')[0]
            name = name.replace('O Carm.', '')
            name = name.replace('MSC', '')
            name = name.replace('SCHP', '')
            name = name.replace('IC', '')
            name = name.replace('Fray', '')
            name = name.strip(', ')
            name = name.strip()
            if name and len(name) > 3:
                priests.add(name)

# Handle some specific names known to be grouped
cleaned_priests = set()
for p in priests:
    # Split if there are multiple names in one line separated by dots or something, not common
    p_clean = ' '.join(p.split())
    if p_clean:
        cleaned_priests.add(p_clean)

sorted_priests = sorted(list(cleaned_priests))

html_list = ""
for p in sorted_priests:
    html_list += f'                        <li style="list-style: none; padding-bottom: 0.5rem; border-bottom: 1px solid rgba(0,0,0,0.05); margin-bottom: 0.5rem;"><strong>{p}</strong><br><span style="color: var(--color-text-light); font-size: 0.9rem;">Fecha de ordenación: Por definir</span></li>\n'

print(f"Extracted {len(sorted_priests)} priests.")
with open('priests_html.txt', 'w', encoding='utf-8') as f:
    f.write(html_list)
