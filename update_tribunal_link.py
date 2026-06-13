import os
import re

dir_path = r"c:\Users\luxmu\OneDrive\Escritorio\Web Arquidiócesis"
old_url = "https://tribunal-arquidiocesis.org"
new_url = "https://tribunaleclesiasticomaracaibo.org/"

count = 0
for f_name in os.listdir(dir_path):
    if f_name.endswith('.html'):
        f_path = os.path.join(dir_path, f_name)
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if old_url in content:
            new_content = content.replace(old_url, new_url)
            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

print(f"Updated {count} files.")
