import json

with open("parishes.json", "r", encoding="utf-8") as file:
    parishes = json.load(file)

with open("lista_templos.txt", "w", encoding="utf-8") as out:
    for p in parishes:
        code = p["code"]
        name = p["name"].replace('\n', ' ').strip()
        out.write(f"- `img/templos/{code}.webp` para {name}\n")
