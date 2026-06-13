import re
with open('static_cards.html','r',encoding='utf-8') as f:
    content = f.read()
m = re.search(r'data-code="PZ4-2".*?</div>\s*</div>', content, re.DOTALL)
if m:
    print(m.group(0)[:600])
else:
    print('Not found')

# Also check PZ6-2
m2 = re.search(r'data-code="PZ6-2".*?</div>\s*</div>', content, re.DOTALL)
if m2:
    print('\n---PZ6-2---')
    print(m2.group(0)[:600])

# Check if any vicario exists
if 'Vicarios' in content:
    print('\nVicarios FOUND in output!')
else:
    print('\nVicarios NOT found in output')
