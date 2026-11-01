"""
ultimo_fotograma.py
-------------------
Extrae el último fotograma de un mp4 y lo guarda como PNG.
Se usa para encadenar clips: el último fotograma del clip N es la
imagen de arranque (first_frame) del clip N+1.

Opción --corregir-azul: devuelve el azul de los muñecos al de la referencia
(ver fondo.corregir_azul); corta el oscurecimiento progresivo al encadenar.

Opción --limpiar-fondo: empuja hacia el blanco puro los píxeles claros y
poco saturados (el fondo del estudio). Evita que el fondo se vaya
ensuciando de clip en clip al encadenar generaciones. Los muñecos (azul
saturado) y sus sombras (oscuras) no se tocan.

Ejecutar con el Python del entorno de ComfyUI (tiene PyAV, Pillow y numpy):
    D:/ComfyUI/.venv/Scripts/python.exe herramientas/ultimo_fotograma.py output/clip.mp4 assets/arranque.png [--limpiar-fondo]
"""

import sys
from pathlib import Path
import av

# Permite importar fondo.py aunque el script se lance desde otra carpeta
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fondo import limpiar_fondo, corregir_azul


argumentos = [a for a in sys.argv[1:] if not a.startswith("--")]
if len(argumentos) != 2:
    print("Uso: ultimo_fotograma.py <video.mp4> <salida.png> [--limpiar-fondo] [--corregir-azul]")
    sys.exit(1)

ruta_video, ruta_png = argumentos
ultimo = None
with av.open(ruta_video) as contenedor:
    # Recorremos todo el vídeo y nos quedamos con el último fotograma decodificado
    for fotograma in contenedor.decode(video=0):
        ultimo = fotograma

if ultimo is None:
    print("El vídeo no tiene fotogramas")
    sys.exit(1)

imagen = ultimo.to_image()
if "--limpiar-fondo" in sys.argv:
    imagen = limpiar_fondo(imagen)
    print("Fondo limpiado")
if "--corregir-azul" in sys.argv:
    # Devuelve el azul de Clic y Plof al de la referencia (corta la deriva al encadenar)
    imagen = corregir_azul(imagen)
    print("Azul de los muñecos corregido")
imagen.save(ruta_png)
print(f"Último fotograma guardado en: {ruta_png}")
