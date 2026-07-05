import os
import re

dir_path = r"c:\Users\luxmu\OneDrive\Escritorio\Web Arquidiócesis"

# 1. Update the nav menu everywhere
tribunal_link = '<a href="https://tribunaleclesiasticomaracaibo.org/" target="_blank" title="Visitar la web del Tribunal Eclesiástico">Tribunal Eclesiástico</a>'
ambientes_link = '                <a href="ambientes.html">Ambientes Seguros</a>'

count = 0
for f_name in os.listdir(dir_path):
    if f_name.endswith('.html'):
        f_path = os.path.join(dir_path, f_name)
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if tribunal_link in content and 'href="ambientes.html">Ambientes Seguros' not in content:
            new_nav_part = tribunal_link + "\n" + ambientes_link
            new_content = content.replace(tribunal_link, new_nav_part)
            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

print(f"Updated menus in {count} files.")

# 2. Fix index.html cards
index_path = os.path.join(dir_path, "index.html")
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()

    donaciones_card = """            <a href="donaciones.html" class="card glass-card">"""
    ambientes_card = """            <a href="ambientes.html" class="card glass-card danger-card">
                <img src="img/icon_ambientes.webp" class="card-img-circle" alt="Ambientes Seguros" onerror="this.src='https://placehold.co/80x80/B23A48/fff?text=AS'">
                <h4>Ambientes Seguros</h4>
                <p>Protección a menores y prevención.</p>
            </a>\n"""

    if donaciones_card in index_content and 'href="ambientes.html" class="card' not in index_content:
        index_content = index_content.replace(donaciones_card, ambientes_card + donaciones_card)
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print("Updated index.html cards.")
