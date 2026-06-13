import re

# Read the current directorio.html
with open('directorio.html', 'r', encoding='utf-8') as f:
    dir_html = f.read()

# Read the new static cards
with open('static_cards.html', 'r', encoding='utf-8') as f:
    new_cards = f.read()

# Find the parish grid container and replace its contents
# The grid starts after <div id="parishGrid" class="parish-grid">
# and ends before the closing </div> that matches it (before the search script)

start_marker = '<div id="parishGrid" class="parish-grid">'
start_idx = dir_html.find(start_marker)

if start_idx == -1:
    print("ERROR: Could not find parishGrid start marker")
    exit(1)

content_start = start_idx + len(start_marker)

# Find the end - the closing </div> for the grid
# It's right before the </main> or the <script> for search
# Let's find the </main> tag
end_marker = '</main>'
end_idx = dir_html.find(end_marker, content_start)

if end_idx == -1:
    print("ERROR: Could not find </main> end marker")
    exit(1)

# The grid div closes with </div> right before </main>
# We need to find the last </div> before </main>
# Actually, let's look for the closing pattern: </div>\n    </main>
close_pattern = dir_html[content_start:end_idx]
# Find the last </div> which closes the parishGrid
last_close = close_pattern.rfind('</div>')
if last_close == -1:
    print("ERROR: Could not find closing </div> for grid")
    exit(1)

# The content between start marker and last </div> is the cards
old_cards_end = content_start + last_close

# Now check for any custom website links we need to preserve
# Santa Lucia has a custom link
custom_links = {}
# Parse existing cards for data-code and check if they have uncommented <a href links
card_pattern = re.compile(r'data-code="(PZ[\d-]+)"[\s\S]*?(?=data-code="|$)')
for m in card_pattern.finditer(dir_html[content_start:old_cards_end]):
    code = m.group(1)
    block = m.group(0)
    # Check for non-commented website links
    link_match = re.search(r'(?<!<!-- )<a href="(https?://[^"]+)" target="_blank" class="btn"', block)
    if link_match:
        custom_links[code] = link_match.group(1)

print(f"Found {len(custom_links)} custom website links: {custom_links}")

# Inject custom links into new_cards
for code, url in custom_links.items():
    # Replace the commented link with an active one for this code
    old_comment = f'data-code="{code}"'
    idx = new_cards.find(old_comment)
    if idx != -1:
        # Find the comment block after this code
        comment_start = new_cards.find('<!-- <a href="ENLACE_AQUI"', idx)
        if comment_start != -1:
            comment_end = new_cards.find('-->', comment_start) + 3
            active_link = f'<a href="{url}" target="_blank" class="btn" style="margin-top: 1rem; display: inline-block; background: var(--color-primary); color: white; padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none;">Visitar Sitio Web</a>'
            new_cards = new_cards[:comment_start] + active_link + new_cards[comment_end:]

# Build new HTML
new_html = dir_html[:content_start] + '\n' + new_cards + '\n        </div>\n    ' + dir_html[end_idx:]

with open('directorio.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully rebuilt directorio.html!")
