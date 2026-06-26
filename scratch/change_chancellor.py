import os

paths = [
    r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main\code.html",
    r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main\portal-cancilleria.html"
]

for p in paths:
    if os.path.exists(p):
        print(f"Modifying {p}")
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace Chancellor signatures
        new_content = content.replace("Pbro. Silverio Osorio", "Pbro. Danilo Calderón")
        
        # Also double check if there are other references to Silverio as Chancellor or if we need to replace them
        # Let's save the file back
        with open(p, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Success")
    else:
        print(f"Path not found: {p}")
