import os
import re

dir_path = r"c:\Users\luxmu\OneDrive\Escritorio\Web Arquidiócesis"

nav_html_new = """            <nav class="nav-links">
                <a href="arquidiocesis.html">Arquidiócesis</a>
                <a href="arzobispo.html">Arzobispo</a>
                <a href="pastoral.html">Pastoral</a>
                <a href="directorio.html">Directorio Parroquial</a>
                <div class="dropdown">
                    <button class="dropbtn">Instituciones &#9662;</button>
                    <div class="dropdown-content">
                        <a href="seminario.html">Seminario</a>
                        <a href="vida-consagrada.html">Vida Consagrada</a>
                        <a href="cancilleria.html">Cancillería</a>
                        <a href="https://tribunaleclesiasticomaracaibo.org/" target="_blank" title="Visitar la web del Tribunal Eclesiástico">Tribunal Eclesiástico</a>
                    </div>
                </div>
                <a href="ambientes.html">Ambientes Seguros</a>
                <a href="donaciones.html" class="btn btn-primary">Donaciones</a>
            </nav>"""

nav_regex = re.compile(r'<nav class="nav-links">.*?</nav>', re.DOTALL)

updated_files = 0
for f_name in os.listdir(dir_path):
    if f_name.endswith('.html'):
        f_path = os.path.join(dir_path, f_name)
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if nav_regex.search(content):
            new_content = nav_regex.sub(nav_html_new, content)
            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files += 1

print(f"Done. Updated {updated_files} files.")
