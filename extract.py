import pypdf
import os

pdf_files = ["Propuesta Web Arquidiócesis Maracaibo - Documentos de Google.pdf", "Directorio Parroquial 2026 Enero22.pdf"]

for file in pdf_files:
    if os.path.exists(file):
        try:
            reader = pypdf.PdfReader(file)
            text = ""
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            
            with open(file + ".txt", "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Extracted {file} to {file}.txt")
        except Exception as e:
            print(f"Error with {file}: {e}")
    else:
        print(f"File not found: {file}")
