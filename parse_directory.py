import re
import json

def parse_directory():
    input_file = "Directorio Parroquial 2026 Enero22.pdf.txt"
    output_file = "parishes.json"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We will use Regex to extract parish blocks. 
    # The format seems to be: PZ<Zone>-<Num> PARROQUIA ...
    pattern = re.compile(r'(PZ\d+-\d+)\s+PARROQUIA\s+(.*?)\n(.*?)PZ\d+-', re.DOTALL)
    
    # A simplified parsing approach just to grab the raw data chunks
    parishes = []
    
    # Actually, a better way is splitting by PZ
    blocks = re.split(r'(PZ\d+-\d+)', content)
    
    current_zone = ""
    for line in content.split('\n'):
        if line.startswith('ZONA '):
            current_zone = line.strip()

    if len(blocks) > 1:
        for i in range(1, len(blocks), 2):
            code = blocks[i].strip()
            details = blocks[i+1].strip() # Full block
            # Remove trailing page numbers (single or double digits standing alone on the last line)
            details = re.sub(r'\n\s*\d+\s*$', '', details)

            # For the last parish, filter out the "Actualizado por..." footer and the rest of the document
            idx = details.find("Actualizado")
            if idx != -1:
                details = details[:idx].strip()

            # extract names
            name_match = re.search(r'([A-ZÁÉÍÓÚÑ ]+)', details.split('\n')[0])
            name = name_match.group(1).strip() if name_match else code
            
            parishes.append({
                "code": code,
                "name": name,
                "raw_details": details
            })
            
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(parishes, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(parishes)} parishes.")

if __name__ == "__main__":
    parse_directory()
