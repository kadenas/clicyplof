"""
desordenar_letras.py
--------------------
A partir de un rótulo generado con Qwen (letras de plastilina de colores sobre
fondo blanco), crea otra imagen con LAS MISMAS letras tiradas por el suelo:
cada letra recortada por su color, girada y colocada en una posición aleatoria.

Sirve como fotograma INICIAL de una intro: el vídeo arranca con las letras
desordenadas y termina (fotograma final = el rótulo original) con la palabra
bien escrita. Se hace con Pillow y no con el modelo de imagen porque el modelo
tiende a inventar letras de más al pedirle que las desordene.

Cómo separa las letras: cada píxel saturado se asigna al color de referencia
más parecido (rojo, naranja, amarillo, verde, azul, morado) y esa asignación
se suaviza por mayoría en un entorno de unos píxeles, para que las sombras y
brillos dentro de una letra no la partan. Después se buscan regiones conexas
de cada color: dos letras pegadas de distinto color quedan separadas. Los
muñecos azules que asoman por abajo se descartan por estar en la franja inferior.

Ejecutar con el Python del entorno de ComfyUI (tiene numpy, scipy y Pillow):
    D:/ComfyUI/.venv/Scripts/python.exe herramientas/desordenar_letras.py rotulo.png desordenado.png [--seed N]
"""

import random
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

# Píxel "de letra": saturado (max-min RGB) por encima de este valor
UMBRAL_SATURACION = 40
# Tonos de referencia de los colores de plastilina, en la escala 0-255 de Pillow
# (grados * 255 / 360): rojo 0°, naranja 30°, amarillo 58°, verde 120°, azul 215°, morado 275°
TONOS_REFERENCIA = [0, 21, 41, 85, 152, 195]
# Radio (píxeles) del suavizado por mayoría de la clasificación de color
SUAVIZADO = 6
# Una región menor que este porcentaje del área de la imagen es ruido, no una letra
AREA_MINIMA = 0.002
# Las regiones cuyo centro cae en esta franja inferior (fracción de la altura) se
# ignoran: ahí asoman los muñecos, que no son letras
FRANJA_FIGURAS = 0.15

semilla = 1
argumentos = []
lista = sys.argv[1:]
i = 0
while i < len(lista):
    if lista[i] == "--seed":
        semilla = int(lista[i + 1])
        i += 2
    else:
        argumentos.append(lista[i])
        i += 1
if len(argumentos) != 2:
    print("Uso: desordenar_letras.py <rotulo.png> <salida.png> [--seed N]")
    sys.exit(1)
ruta_entrada, ruta_salida = argumentos
random.seed(semilla)

original = Image.open(ruta_entrada).convert("RGB")
ancho, alto = original.size
rgb = np.asarray(original).astype(np.int32)
hsv = np.asarray(original.convert("HSV")).astype(np.int32)

saturado = (rgb.max(axis=2) - rgb.min(axis=2)) > UMBRAL_SATURACION
tono = hsv[..., 0]

# Clasificación de cada píxel saturado por el tono de referencia más cercano
# (distancia circular, porque el rojo está en los dos extremos de la escala)
distancias = np.stack([np.minimum(np.abs(tono - r), 256 - np.abs(tono - r)) for r in TONOS_REFERENCIA])
clase = distancias.argmin(axis=0)

# Suavizado por mayoría: cada clase "vota" en su entorno y gana la más presente.
# Así las sombras rojizas de una letra naranja siguen contando como naranja.
votos = np.stack([
    ndimage.gaussian_filter((saturado & (clase == c)).astype(np.float32), SUAVIZADO)
    for c in range(len(TONOS_REFERENCIA))
])
clase = votos.argmax(axis=0)

# Regiones conexas por color: cada letra queda en su propia región
letras = []
for c in range(len(TONOS_REFERENCIA)):
    etiquetas, n = ndimage.label(saturado & (clase == c))
    for k in range(1, n + 1):
        mascara = etiquetas == k
        if mascara.sum() < AREA_MINIMA * ancho * alto:
            continue
        filas, columnas = np.where(mascara)
        if filas.mean() > alto * (1 - FRANJA_FIGURAS):
            continue   # muñecos asomando por abajo
        # Los brillos poco saturados dejan huecos dentro de la letra: se rellenan,
        # y se dilata un poco para no comerse el borde antialiasado
        mascara = ndimage.binary_fill_holes(mascara)
        mascara = ndimage.binary_dilation(mascara, iterations=2)
        filas, columnas = np.where(mascara)
        y0, y1, x0, x1 = filas.min(), filas.max() + 1, columnas.min(), columnas.max() + 1
        # Recorte de la letra con canal alfa suavizado para no dejar bordes duros
        alfa = Image.fromarray((mascara[y0:y1, x0:x1] * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1))
        letra = original.crop((x0, y0, x1, y1)).copy()
        letra.putalpha(alfa)
        letras.append(letra)

if not letras:
    print("No se ha encontrado ninguna letra (¿fondo blanco y letras de colores?)")
    sys.exit(1)
print(f"{len(letras)} letras encontradas")

# Colocación aleatoria sin solaparse, en la zona central e inferior (el "suelo")
salida = Image.new("RGB", (ancho, alto), "white")
ocupados = []
for letra in letras:
    # Giro grande para que se vean caídas: de lado, boca abajo, inclinadas
    angulo = random.choice([random.uniform(-40, 40), random.uniform(60, 120), random.uniform(150, 210)])
    girada = letra.rotate(angulo, expand=True, resample=Image.BICUBIC)
    for _ in range(200):
        x = random.randint(0, max(0, ancho - girada.width))
        y = random.randint(int(alto * 0.25), max(int(alto * 0.25), int(alto * 0.9) - girada.height))
        caja = (x, y, x + girada.width, y + girada.height)
        if all(caja[2] <= o[0] or caja[0] >= o[2] or caja[3] <= o[1] or caja[1] >= o[3] for o in ocupados):
            break
    ocupados.append(caja)
    salida.paste(girada, (x, y), girada)

salida.save(ruta_salida)
print(f"Letras desordenadas guardadas en: {ruta_salida}")
