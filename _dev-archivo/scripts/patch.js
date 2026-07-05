const fs = require('fs');

const staticCards = fs.readFileSync('static_cards.html', 'utf8');
let html = fs.readFileSync('directorio.html', 'utf8');

// Replace the grid content
html = html.replace(/<div id="parishGrid" class="parish-grid">[\s\S]*?<\/main>/, `<div id="parishGrid" class="parish-grid">\n${staticCards}\n        </div>\n    </main>`);
// Remove loading
html = html.replace(/<div id="loading" class="text-center">[\s\S]*?<\/div>\s*<div id="parishGrid"/, '<div id="parishGrid"');

const newScript = `
    <script src="js/app.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const searchInput = document.getElementById('searchInput');
            const zoneFilter = document.getElementById('zoneFilter');
            const cards = document.querySelectorAll('.parish-card');

            const filterParishes = () => {
                const query = searchInput.value.toLowerCase();
                const zone = zoneFilter.value;

                let visibleCount = 0;
                cards.forEach(card => {
                    const name = card.getAttribute('data-name') || '';
                    const details = card.getAttribute('data-details') || '';
                    const code = card.getAttribute('data-code') || '';
                    
                    const matchesQuery = name.includes(query) || details.includes(query);
                    const matchesZone = zone === 'all' || code.startsWith(zone);
                    
                    if (matchesQuery && matchesZone) {
                        card.style.display = ''; // Reset display to stylesheet default (flex row/col media queries will work)
                        visibleCount++;
                    } else {
                        card.style.display = 'none';
                    }
                });

                let noResultsMsg = document.getElementById('noResultsMsg');
                if (visibleCount === 0) {
                    if (!noResultsMsg) {
                        noResultsMsg = document.createElement('p');
                        noResultsMsg.id = 'noResultsMsg';
                        noResultsMsg.className = 'text-center';
                        noResultsMsg.style.gridColumn = '1 / -1';
                        noResultsMsg.textContent = 'No se encontraron parroquias con esos criterios.';
                        document.getElementById('parishGrid').appendChild(noResultsMsg);
                    }
                    noResultsMsg.style.display = 'block';
                } else if (noResultsMsg) {
                    noResultsMsg.style.display = 'none';
                }
            };

            searchInput.addEventListener('input', filterParishes);
            zoneFilter.addEventListener('change', filterParishes);
        });
    </script>`;

html = html.replace(/<script src="js\/parishes\.js"><\/script>[\s\S]*?<\/body>/, `${newScript}\n</body>`);

fs.writeFileSync('directorio.html', html, 'utf8');
