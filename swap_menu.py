import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to match:
    #                 <a href="arzobispo.html">Arzobispo</a>
    #                 <a href="arquidiocesis.html">Arquidiócesis</a>
    
    # Use re.sub with function to do the swap
    pattern = r'([ \t]*<a\s+href="arzobispo\.html"[^>]*>Arzobispo</a>)([\r\n]+)([ \t]*<a\s+href="arquidiocesis\.html"[^>]*>Arquidiócesis</a>)'
    
    def replacer(match):
        # We put the second link first, then the whitespace, then the first link
        return match.group(3) + match.group(2) + match.group(1)
        
    new_content, count = re.subn(pattern, replacer, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Swapped in {filepath}')
