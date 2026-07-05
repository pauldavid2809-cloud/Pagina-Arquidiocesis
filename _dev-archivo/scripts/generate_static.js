const fs = require('fs');
const parishesData = JSON.parse(fs.readFileSync('parishes.json', 'utf8'));

let html = '';

parishesData.forEach((p) => {
    let formatBlocks = [];
    
    if (p.parroco) {
        formatBlocks.push(`<p style="margin: 0; padding-bottom: 0.3rem;"><strong>Párroco:</strong> ${p.parroco}</p>`);
    }
    if (p.vicario) {
        formatBlocks.push(`<p style="margin: 0; padding-bottom: 0.3rem;"><strong>Vicarios / Diáconos:</strong> ${p.vicario}</p>`);
    }
    if (p.direccion) {
        formatBlocks.push(`<p style="margin: 0; padding-bottom: 0.3rem;"><strong>Dirección:</strong> ${p.direccion}</p>`);
    }
    if (p.phone) {
        formatBlocks.push(`<p style="margin: 0; padding-bottom: 0.3rem;"><strong>Teléfonos:</strong> ${p.phone}</p>`);
    }
    if (p.email) {
        formatBlocks.push(`<p style="margin: 0; padding-bottom: 0.3rem;"><strong>Redes:</strong> ${p.email}</p>`);
    }

    const fullName = p.name;
    const details = formatBlocks.length > 0 ? formatBlocks.join('\n                        ') : '';
    
    // Build searchable data-details (all text, lowercase)
    const searchDetails = [p.parroco, p.vicario, p.direccion, p.phone, p.email, p.code].filter(Boolean).join(' ').toLowerCase().replace(/"/g, '&quot;');
    
    const imgSrc = p.image ? p.image : `img/templos/${p.code}.webp`;
    const webLink = p.web ? `<a href="${p.web}" target="_blank" class="btn" style="margin-top: 1rem; display: inline-block; background: var(--color-primary); color: white; padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none;">Visitar Sitio Web</a>` : '';
    
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

