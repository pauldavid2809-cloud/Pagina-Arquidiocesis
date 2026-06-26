import os

files = [
    r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main\directorio.html",
    r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main\index.html",
    r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main\stitch_arquidi_cesis_de_maracaibo_digital\directorio_parroquial_arquidi_cesis_de_maracaibo\code.html"
]

replacements = [
    ("Todas las Zonas Pastorales", "Todos los Arciprestazgos"),
    ("Todas las zonas pastorales", "Todos los arciprestazgos"),
    ("Zonas Pastorales", "Arciprestazgos"),
    ("zonas pastorales", "arciprestazgos"),
    ("zona pastoral", "arciprestazgo"),
    ("Zona Pastoral", "Arciprestazgo"),
    ("Zona 1", "Arciprestazgo 1"),
    ("Zona 2", "Arciprestazgo 2"),
    ("Zona 3", "Arciprestazgo 3"),
    ("Zona 4", "Arciprestazgo 4"),
    ("Zona 5", "Arciprestazgo 5"),
    ("Zona 6", "Arciprestazgo 6"),
    ("Zona 7", "Arciprestazgo 7"),
    ("Zona 8", "Arciprestazgo 8"),
    ("Zona 9", "Arciprestazgo 9"),
]

for filepath in files:
    if os.path.exists(filepath):
        print(f"Modifying {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        original = content
        for target, replacement in replacements:
            content = content.replace(target, replacement)
        
        if content != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully updated.")
        else:
            print("No changes made (no matching patterns found).")
    else:
        print(f"File not found: {filepath}")
