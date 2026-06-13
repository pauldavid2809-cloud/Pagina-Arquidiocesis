import fitz
import glob

pdfs = glob.glob('*Parroquial*.pdf')
if not pdfs:
    print("PDF not found!")
    exit(1)

doc = fitz.open(pdfs[0])

text = ""
for page in doc:
    text += page.get_text()

lines = text.split('\n')
for i, line in enumerate(lines):
    if "INCARDINADO" in line.upper() or "SACERDOTE" in line.upper():
        print(f"Line {i}: {line}")

with open('pdf_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)
