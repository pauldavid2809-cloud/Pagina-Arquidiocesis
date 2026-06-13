import json
import re

def clean_html_attr(text):
    return text.replace('"', '&quot;')

def generate():
    with open('parishes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    html_cards = []
    
    for p in data:
        raw = p.get('raw_details', '')
        lines = [ln.strip() for ln in raw.split('\n')]
        
        detail_start = False
        title_lines = []
        detail_lines = []
        
        for line in lines:
            if not detail_start and (
                re.match(r'^(Fundada|Pbro|Rif|R\.?P\.|Párroco|Secretari[oa]|Tel[eé]f|Email|-|Z-?P\d|Di[aá]c|Jorge Enrique|Naranjo Flores|Andrés de Jesús)', line, re.I) or
                re.search(r'\d{4}-\d{7}', line) or
                re.match(r'^[0-9/]+$', line) or
                "erección" in line.lower()
            ):
                detail_start = True
                
            if not detail_start and title_lines and line.lower() == line:
                detail_start = True
                
            if not detail_start and line:
                title_lines.append(line)
            elif line:
                detail_lines.append(line)
                
        extracted = {
            "Párroco": [],
            "Dirección": [],
            "Secretario(a)": [],
            "Teléfonos": [],
            "Página Web o Redes": []
        }
        active_field = None
        
        for line in detail_lines:
            line = line.replace('\\n', '').strip()
            
            phones = re.findall(r'0(?:2|4)\d{2}[-.\s]?\d{7}', line)
            if phones:
                extracted["Teléfonos"].extend(phones)
                line = re.sub(r'0(?:2|4)\d{2}[-.\s]?\d{7}', '', line).strip()
                
            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', line)
            if emails:
                extracted["Página Web o Redes"].extend(emails)
                line = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', line).strip()
                
            line = re.sub(r'^(tel[eé]fonos?|telf)\.?\s*:?\s*', '', line, flags=re.I)
            line = re.sub(r'^(email|correo):?\s*', '', line, flags=re.I)
            
            if not line: continue
            lower = line.lower()
            
            if (lower.startswith("fundada") or "toma de posesión" in lower or
                lower.startswith("rif") or lower.startswith("j-") or lower.startswith("-") or
                lower.startswith("rectoría") or lower.startswith("zp-") or
                "administrador parroquial" in lower or "vicario" in lower or
                "diác" in lower or "diácono" in lower or "erección" in lower or
                re.match(r'^\d+$', lower) or lower.startswith("desde:") or
                lower.startswith("zona ") or lower.startswith("n°") or lower.startswith("cód") or
                lower == "parroquia" or lower == "parroco" or lower == "párroco" or
                "actualizado por" in lower or "iglesias filiales" in lower):
                active_field = None
                continue
                
            if re.match(r'^(pbro\.?|r\.?p\.?|párroco:?)', lower):
                active_field = "Párroco"
                line = re.sub(r'^(Pbro\.?|R\.?P\.?|Párroco:?)\s*', '', line, flags=re.I)
            elif re.match(r'^secretari[oa]?\s*\(?a?\)?\s*:', lower):
                active_field = "Secretario(a)"
                line = re.sub(r'^secretari[oa]?\s*\(?a?\)?\s*:\s*', '', line, flags=re.I)
            elif re.match(r'^direcci[oó]n:', lower):
                active_field = "Dirección"
                line = re.sub(r'^direcci[oó]n:\s*', '', line, flags=re.I)
            elif "facebook" in lower or "instagram" in lower or "redes" in lower or "@" in lower:
                active_field = "Página Web o Redes"
            elif not active_field and not extracted["Párroco"] and re.match(r'^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+ [A-ZÁÉÍÓÚÑ]', line):
                active_field = "Párroco"
                
            if active_field and line:
                extracted[active_field].append(line)
        
        full_name = " ".join(title_lines) if title_lines else p.get('name', 'Parroquia Desconocida')
        
        details_html_lines = []
        raw_details_str = ""
        for col, lines_list in extracted.items():
            if lines_list:
                val = " ".join(lines_list)
                details_html_lines.append(f'                        <p style="margin: 0; padding-bottom: 0.3rem;"><strong>{col}:</strong> {val}</p>')
                raw_details_str += col + " " + val + " "
                
        if not details_html_lines:
            details_html_lines = [f'                        <p style="margin: 0; padding-bottom: 0.3rem;">{ln}</p>' for ln in detail_lines]
            raw_details_str = " ".join(detail_lines)
            
        details_html = "\n".join(details_html_lines)
        img_src = p.get('image', 'https://placehold.co/600x400/eeeeee/999999?text=Foto+del+Templo')
        if not img_src: img_src = 'https://placehold.co/600x400/eeeeee/999999?text=Foto+del+Templo'
        
        card_html = f'''            <div class="parish-card animate-fade-in-up" data-name="{clean_html_attr(full_name).lower()}" data-code="{p.get('code','')}" data-details="{clean_html_attr(raw_details_str).lower()}">
                <img src="{img_src}" alt="{clean_html_attr(full_name)}" class="parish-card-img" onerror="this.src=\'https://placehold.co/600x400/eeeeee/999999?text=Foto+del+Templo\'">
                <div class="parish-card-content">
                    <h3 class="parish-name">{full_name}</h3>
                    <!-- prettier-ignore -->
                    <div class="parish-details" style="line-height: 1.4;">
{details_html}
                    </div>
                    <!-- Descomenta y edita el enlace de abajo para agregar la pagina web o red social de la parroquia -->
                    <!-- <a href="ENLACE_AQUI" target="_blank" class="btn" style="margin-top: 1rem; display: inline-block; background: var(--color-primary); color: white; padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none;">Visitar Sitio Web</a> -->
                </div>
            </div>'''
        html_cards.append(card_html)
        
    return "\n".join(html_cards)

def main():
    cards_html = generate()
    
    with open('directorio.html', 'r', encoding='utf-8') as f:
        doc = f.read()
        
    # Replace `<div id="parishGrid">...</div>`
    pattern_grid = re.compile(r'<div id="parishGrid" class="parish-grid">.*?</main>', re.DOTALL)
    replacement_grid = f'<div id="parishGrid" class="parish-grid">\n{cards_html}\n        </div>\n    </main>'
    doc = pattern_grid.sub(replacement_grid, doc)
    
    with open('directorio.html', 'w', encoding='utf-8') as f:
        f.write(doc)

if __name__ == '__main__':
    main()
