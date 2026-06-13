const fs = require('fs');
const parishesData = JSON.parse(fs.readFileSync('parishes.json', 'utf8'));

let html = '';

parishesData.forEach((p, index) => {
    let rawLines = p.raw_details.split('\n');
    let titleLines = [];
    let detailLines = [];
    let foundDetailStart = false;

    for (let i = 0; i < rawLines.length; i++) {
        let line = rawLines[i].trim();
        if (!foundDetailStart && (
            line.match(/^(Fundada|Pbro|Rif|R\.?P\.|Párroco|Secretari[oa]|Tel[eé]f|Email|-|Z-?P\d|Di[aá]c|Jorge Enrique|Naranjo Flores|Andrés de Jesús)/i) || 
            line.match(/\d{4}-\d{7}/) ||
            line.match(/^[0-9\/]+$/) ||
            line.includes("erección")
        )) {
            foundDetailStart = true;
        }

        if (!foundDetailStart && titleLines.length > 0 && line.toLowerCase() === line) {
            foundDetailStart = true;
        }

        if (!foundDetailStart && line !== '') {
            titleLines.push(line);
        } else if (line !== '') {
            detailLines.push(line);
        }
    }

    let extracted = {
        "Párroco": [],
        "Vicarios / Diáconos": [],
        "Dirección": [],
        "Teléfonos": [],
        "Redes": []
    };
    let activeField = null;

    for (let i = 0; i < detailLines.length; i++) {
        let line = detailLines[i].replace(/\n/g, '').trim();
        
        // Extract phone numbers
        let linePhones = line.match(/0(?:2|4)\d{2}[-.\s]?\d{7}/g);
        if (linePhones) {
            extracted["Teléfonos"].push(...linePhones);
            line = line.replace(/0(?:2|4)\d{2}[-.\s]?\d{7}/g, '').trim();
        }
        
        // Extract emails -> Redes
        let lineEmails = line.match(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g);
        if (lineEmails) {
            extracted["Redes"].push(...lineEmails);
            line = line.replace(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g, '').trim();
        }

        line = line.replace(/^(tel[eé]fonos?|telf)\.?\s*:?\s*/i, '');
        line = line.replace(/^(email|correo):?\s*/i, '');

        if (!line) continue;
        let lower = line.toLowerCase();
        
        // Detect Vicarios / Diáconos FIRST (before skip block)
        if (lower.includes("vicario") || lower.includes("diác") || lower.includes("diácono") || lower.startsWith("diac")) {
            activeField = "Vicarios / Diáconos";
            line = line.replace(/^(Vicario:?\s*|Vicario Parroquial:?\s*|Diácono[s]?:?\s*|Diác\.\s*|Diac\.\s*permanente\s*)/i, '').trim();
            if (line) extracted["Vicarios / Diáconos"].push(line);
            continue;
        }

        // Skip irrelevant lines
        if (lower.startsWith("fundada") || 
            lower.includes("toma de posesión") || 
            lower.startsWith("rif") || 
            lower.startsWith("j-") || 
            lower.startsWith("-") || 
            lower.startsWith("rectoría") || 
            lower.startsWith("zp-") || 
            lower.includes("administrador parroquial") || 
            lower.includes("erección") ||
            lower.match(/^\d+$/) ||
            lower.startsWith("desde:") ||
            lower.startsWith("zona ") ||
            lower.startsWith("n°") ||
            lower.startsWith("cód") ||
            lower === "parroquia" ||
            lower === "parroco" ||
            lower === "párroco" ||
            lower.includes("actualizado por") ||
            lower.includes("iglesias filiales") ||
            lower.match(/^secretari[oa]?\s*\(?a?\)?\s*:/i)) {
            // If it's secretario, skip the field entirely
            if (lower.match(/^secretari[oa]?\s*\(?a?\)?\s*:/i)) {
                activeField = "_skip";
            } else {
                activeField = null;
            }
            continue;
        }

        // Detect Dirección
        if (lower.match(/^direcci[oó]n:/i)) {
            activeField = "Dirección";
            line = line.replace(/^direcci[oó]n:\s*/i, '').trim();
        }
        // Detect Párroco
        else if (lower.match(/^(pbro\.?|r\.?p\.?\s|párroco:?|padre\s)/i)) {
            activeField = "Párroco";
            line = line.replace(/^(Pbro\.?|R\.?P\.?\s*|Párroco:?|Padre\s)\s*/i, '').trim();
        } else if (lower.includes("facebook") || lower.includes("instagram") || lower.includes("redes") || lower.includes("@")) {
            activeField = "Redes";
        } else if (!activeField && extracted["Párroco"].length === 0 && line.match(/^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+ [A-ZÁÉÍÓÚÑ]/)) {
            activeField = "Párroco";
        }

        if (activeField && activeField !== "_skip" && line) {
            extracted[activeField].push(line);
        }
    }

    // Extract Instagram handles from Redes
    for (let i = 0; i < detailLines.length; i++) {
        let line = detailLines[i].trim();
        let igMatch = line.match(/@[\w.]+/g);
        if (igMatch) {
            igMatch.forEach(handle => {
                // Don't add email-looking handles
                if (!handle.includes('.com') && !handle.includes('.net') && !handle.includes('.es') &&
                    !extracted["Redes"].some(r => r.includes(handle))) {
                    extracted["Redes"].push(`Instagram: ${handle}`);
                }
            });
        }
    }

    // Build HTML blocks - only show fields that have data
    let formatBlocks = [];
    
    if (extracted["Párroco"].length > 0) {
        formatBlocks.push(`<p style="margin: 0; padding-bottom: 0.3rem;"><strong>Párroco:</strong> ${extracted["Párroco"].join(' ')}</p>`);
    }
    if (extracted["Vicarios / Diáconos"].length > 0) {
        formatBlocks.push(`<p style="margin: 0; padding-bottom: 0.3rem;"><strong>Vicarios / Diáconos:</strong> ${extracted["Vicarios / Diáconos"].join(' ')}</p>`);
    }
    if (extracted["Dirección"].length > 0) {
        formatBlocks.push(`<p style="margin: 0; padding-bottom: 0.3rem;"><strong>Dirección:</strong> ${extracted["Dirección"].join(' ')}</p>`);
    }
    if (extracted["Teléfonos"].length > 0) {
        formatBlocks.push(`<p style="margin: 0; padding-bottom: 0.3rem;"><strong>Teléfonos:</strong> ${extracted["Teléfonos"].join(' ')}</p>`);
    }
    if (extracted["Redes"].length > 0) {
        formatBlocks.push(`<p style="margin: 0; padding-bottom: 0.3rem;"><strong>Redes:</strong> ${extracted["Redes"].join(', ')}</p>`);
    }

    let fullName = titleLines.length > 0 ? titleLines.join(' ') : p.name;
    let details = formatBlocks.length > 0 ? formatBlocks.join('\n                        ') : '';
    
    // Build searchable data-details (all text, lowercase)
    let searchDetails = Object.values(extracted).flat().join(' ').toLowerCase().replace(/"/g, '&quot;').replace(/<[^>]+>/g, ' ');
    
    const imgSrc = p.image ? p.image : `img/templos/${p.code}.webp`;
    const webLink = p.website ? `<a href="${p.website}" target="_blank" class="btn" style="margin-top: 1rem; display: inline-block; background: var(--color-primary); color: white; padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none;">Visitar Sitio Web</a>` : '';
    
    html += `
        <div class="parish-card animate-fade-in-up" data-name="${fullName.toLowerCase().replace(/"/g, '&quot;')}" data-code="${p.code}" data-details="${searchDetails}">
            <img src="${imgSrc}" alt="${fullName.replace(/"/g, '&quot;')}" class="parish-card-img" onerror="this.onerror=null;this.src='img/foto_templo.webp'">
            <div class="parish-card-content">
                <h3 class="parish-name">${fullName}</h3>
                <div class="parish-details" style="line-height: 1.4;">
                    ${details}
                </div>
                <!-- Descomenta y edita el enlace de abajo para agregar la pagina web o red social de la parroquia -->
                ${webLink ? webLink : `<!-- <a href="ENLACE_AQUI" target="_blank" class="btn" style="margin-top: 1rem; display: inline-block; background: var(--color-primary); color: white; padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none;">Visitar Sitio Web</a> -->`}
            </div>
        </div>`;
});

fs.writeFileSync('static_cards.html', html, 'utf8');
console.log('Generated static_cards.html with ' + parishesData.length + ' cards');
