import os
from PIL import Image
from tqdm import tqdm

# --- CONFIGURACIÓN ---
CARPETA_ORIGEN = 'imagenes_originales' # Ponga todos sus JPGs actuales aquí
CARPETA_DESTINO = 'img'      # Aquí saldrán las optimizadas

os.makedirs(CARPETA_DESTINO, exist_ok=True)

def optimizar_web():
    # Buscamos JPG, JPEG y también PNG por si tiene alguno
    archivos = [f for f in os.listdir(CARPETA_ORIGEN) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    print(f"📦 Optimizando {len(archivos)} imágenes para la Parroquia...")

    for archivo in tqdm(archivos, desc="Convirtiendo a WebP"):
        ruta_entrada = os.path.join(CARPETA_ORIGEN, archivo)
        # Cambiamos la extensión a .webp
        nombre_salida = os.path.splitext(archivo)[0] + ".webp"
        ruta_salida = os.path.join(CARPETA_DESTINO, nombre_salida)

        with Image.open(ruta_entrada) as img:
            # Por seguridad, aseguramos que el modo de color sea compatible
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Guardamos como WebP manteniendo las dimensiones intactas
            img.save(ruta_salida, "WEBP", quality=80)

    print(f"\n✨ ¡Sitio web aligerado! Archivos guardados en: {CARPETA_DESTINO}")

if __name__ == "__main__":
    optimizar_web()