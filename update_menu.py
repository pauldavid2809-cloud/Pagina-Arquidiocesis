import os
import re
import shutil

dir_path = r"c:\Users\luxmu\OneDrive\Escritorio\Web Arquidiócesis"

# 1. Rename gobierno.html to arquidiocesis.html
gob_path = os.path.join(dir_path, "gobierno.html")
arqui_path = os.path.join(dir_path, "arquidiocesis.html")
if os.path.exists(gob_path):
    os.rename(gob_path, arqui_path)

# 2. Delete tribunal.html
trib_path = os.path.join(dir_path, "tribunal.html")
if os.path.exists(trib_path):
    os.remove(trib_path)

# 3. Create missing pages from pastoral.html template
template_path = os.path.join(dir_path, "pastoral.html")
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

pages_to_create = {
    "arzobispo.html": ("Arzobispo | Arquidiócesis de Maracaibo", "Arzobispo", "Conoce a nuestro pastor, su biografía y mensajes a la comunidad zuliana.", "Arzobispado"),
    "seminario.html": ("Seminario | Arquidiócesis de Maracaibo", "Seminario", "Formando a los futuros pastores de nuestra iglesia local.", "Formación Sacerdotal"),
    "donaciones.html": ("Donaciones | Arquidiócesis de Maracaibo", "Donaciones", "Apoya nuestra labor pastoral y social con tu aporte generoso.", "Tu aporte hace la diferencia")
}

for filename, (title_tag, h2_text, p_text, feature_h2) in pages_to_create.items():
    filepath = os.path.join(dir_path, filename)
    if not os.path.exists(filepath):
        html = re.sub(r'<title>.*?</title>', f'<title>{title_tag}</title>', template)
        html = re.sub(r'<h2>Secretariados Pastorales</h2>', f'<h2>{h2_text}</h2>', html)
        html = re.sub(r'<p>La Iglesia en salida.*?<\/p>', f'<p>{p_text}</p>', html)
        html = re.sub(r'<h2>Nuestra Vida Pastoral</h2>', f'<h2>{feature_h2}</h2>', html)
        html = re.sub(r'<img src="img/pastoral.webp".*?>', f'<img src="https://placehold.co/600x400/e6e6e6/999?text={h2_text}" alt="{h2_text}">', html)
        # remove the tags
        html = re.sub(r'<div class="pastoral-tags">.*?</div>', '', html, flags=re.DOTALL)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

# 4. Update the nav menu everywhere
nav_html_new = """            <nav class="nav-links">
                <a href="arzobispo.html">Arzobispo</a>
                <a href="arquidiocesis.html">Arquidiócesis</a>
                <a href="pastoral.html">Pastoral</a>
                <a href="directorio.html">Directorio Parroquial</a>
                <a href="seminario.html">Seminario</a>
                <a href="vida-consagrada.html">Vida Consagrada</a>
                <a href="cancilleria.html">Cancillería</a>
                <a href="https://tribunal-arquidiocesis.org" target="_blank" title="Visitar la web del Tribunal Eclesiástico">Tribunal Eclesiástico</a>
                <a href="donaciones.html" class="btn btn-primary">Donaciones</a>
            </nav>"""

nav_regex = re.compile(r'<nav class="nav-links">.*?</nav>', re.DOTALL)

for f_name in os.listdir(dir_path):
    if f_name.endswith('.html'):
        f_path = os.path.join(dir_path, f_name)
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = nav_regex.sub(nav_html_new, content)
        
        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

# 5. Fix index.html cards
index_path = os.path.join(dir_path, "index.html")
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

new_cards = """        <div class="grid axes-grid">
            <a href="arzobispo.html" class="card glass-card">
                <img src="img/icon_arzobispo.webp" class="card-img-circle" alt="Arzobispo" onerror="this.src='https://placehold.co/80x80/e6e6e6/999?text=A'">
                <h4>Arzobispo</h4>
                <p>Conozca a nuestro pastor y sus enseñanazs.</p>
            </a>
            <a href="arquidiocesis.html" class="card glass-card">
                <img src="img/icon_gobierno.webp" class="card-img-circle" alt="Arquidiócesis" onerror="this.src='https://placehold.co/80x80/e6e6e6/999?text=Aq'">
                <h4>Arquidiócesis</h4>
                <p>Nuestra curia, historia y organización.</p>
            </a>
            <a href="pastoral.html" class="card glass-card">
                <img src="img/icon_pastoral.webp" class="card-img-circle" alt="Pastoral" onerror="this.src='https://placehold.co/80x80/e6e6e6/999?text=P'">
                <h4>Pastoral</h4>
                <p>Acción evangelizadora y social en el Zulia.</p>
            </a>
            <a href="directorio.html" class="card glass-card highlight">
                <img src="img/icon_directorio.webp" class="card-img-circle" alt="Directorio Parroquial" onerror="this.src='https://placehold.co/80x80/ffcc00/003366?text=DP'">
                <h4>Directorio Parroquial</h4>
                <p>Encuentre su parroquia, horarios y contactos.</p>
            </a>
            <a href="seminario.html" class="card glass-card">
                <img src="img/icon_seminario.webp" class="card-img-circle" alt="Seminario" onerror="this.src='https://placehold.co/80x80/e6e6e6/999?text=S'">
                <h4>Seminario</h4>
                <p>Formación de nuestros futuros sacerdotes.</p>
            </a>
            <a href="vida-consagrada.html" class="card glass-card">
                <img src="img/icon_vida.webp" class="card-img-circle" alt="Vida Consagrada" onerror="this.src='https://placehold.co/80x80/e6e6e6/999?text=VC'">
                <h4>Vida Consagrada</h4>
                <p>Conozca las distintas órdenes religiosas.</p>
            </a>
            <a href="cancilleria.html" class="card glass-card">
                <img src="img/icon_cancilleria.webp" class="card-img-circle" alt="Cancillería" onerror="this.src='https://placehold.co/80x80/e6e6e6/999?text=C'">
                <h4>Cancillería</h4>
                <p>Trámites, decretos y archivo arquidiocesano.</p>
            </a>
            <a href="https://tribunal-arquidiocesis.org" target="_blank" class="card glass-card">
                <img src="img/icon_tribunal.webp" class="card-img-circle" alt="Tribunal Eclesiástico" onerror="this.src='https://placehold.co/80x80/e6e6e6/999?text=TE'">
                <h4>Tribunal Eclesiástico</h4>
                <p>Procesos de nulidad y asesoría canónica.</p>
            </a>
            <a href="donaciones.html" class="card glass-card">
                <img src="img/icon_donaciones.webp" class="card-img-circle" alt="Donaciones" onerror="this.src='https://placehold.co/80x80/e6e6e6/999?text=D'">
                <h4>Donaciones</h4>
                <p>Apoye nuestra labor pastoral y de caridad.</p>
            </a>
        </div>"""

cards_regex = re.compile(r'<div class="grid axes-grid">.*?</div>\s*</main>', re.DOTALL)
index_content = cards_regex.sub(f'{new_cards}\n    </main>', index_content)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Done adjusting files.")
