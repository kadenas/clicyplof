"""
montar_capitulo.py
------------------
Une varios mp4 (vídeo + audio) en uno solo, en orden.
Recodifica todo a H.264 + AAC con el mismo formato que genera ComfyUI
(480x864, 24 fps, audio estéreo 32 kHz), así los cortes quedan limpios.

Opción --limpiar-fondo: aplica a cada fotograma la limpieza de fondo de
fondo.py, para que todo el capítulo tenga el mismo blanco y no se noten
saltos de brillo en los cortes entre clips encadenados.

Opción --marca-agua RUTA: superpone ese logo en la esquina inferior derecha
de todos los fotogramas con fusión "diferencia" (ver marca_agua.py).
Opción --opacidad-marca N: intensidad de la marca de agua, de 0 a 1 (0.6 por defecto).

Ajustes por clip (tras una arroba, separados por comas):
    clip.mp4@pausa=3    mantiene el último fotograma 3 s más, en silencio (pausa de predicción)
    clip.mp4@saltar=8   descarta los 8 primeros fotogramas y su audio

Ejecutar con el Python del entorno de ComfyUI (tiene PyAV):
    D:/ComfyUI/.venv/Scripts/python.exe herramientas/montar_capitulo.py output/capitulo.mp4 intro.mp4@saltar=8 clip1.mp4 clip2.mp4@pausa=3 ... [--limpiar-fondo] [--marca-agua logo.png] [--opacidad-marca 0.6]
"""

import sys
from fractions import Fraction
from pathlib import Path
import av

# Permite importar fondo.py y marca_agua.py aunque el script se lance desde otra carpeta
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fondo import limpiar_fondo
from marca_agua import preparar_logo, aplicar_marca_agua

FPS = 24
FRECUENCIA_AUDIO = 32000

# Lectura de la línea de comandos. Hay dos tipos de opciones:
# - sin valor (--limpiar-fondo): basta con comprobar si están;
# - con valor (--marca-agua RUTA): el valor que las sigue no es un clip.
OPCIONES_CON_VALOR = ("--marca-agua", "--opacidad-marca")
opciones = {}
argumentos = []
lista = sys.argv[1:]
i = 0
while i < len(lista):
    if lista[i] in OPCIONES_CON_VALOR:
        if i + 1 >= len(lista):
            print(f"Falta el valor de {lista[i]}")
            sys.exit(1)
        opciones[lista[i]] = lista[i + 1]
        i += 2
    elif lista[i].startswith("--"):
        i += 1
    else:
        argumentos.append(lista[i])
        i += 1

limpiar = "--limpiar-fondo" in sys.argv
ruta_marca = opciones.get("--marca-agua")
opacidad_marca = float(opciones.get("--opacidad-marca", "0.6"))
if len(argumentos) < 2:
    print("Uso: montar_capitulo.py <salida.mp4> <clip1.mp4> <clip2.mp4> ... [--limpiar-fondo] [--marca-agua logo.png] [--opacidad-marca 0.6]")
    sys.exit(1)

ruta_salida = argumentos[0]

# Cada clip puede llevar ajustes tras una arroba, separados por comas:
#   ruta.mp4@pausa=3    el último fotograma se mantiene congelado 3 s, en silencio
#                       (pausa de predicción del guion, que el modelo no respeta solo)
#   ruta.mp4@saltar=8   se descartan los 8 primeros fotogramas (y su audio)
#                       (oculta el salto inicial cuando el clip arranca de una imagen compuesta)
clips = []
for texto in argumentos[1:]:
    ruta, ajustes = (texto.rsplit("@", 1) + [""])[:2] if "@" in texto else (texto, "")
    pausa, saltar = 0.0, 0
    for ajuste in filter(None, ajustes.split(",")):
        clave, valor = ajuste.split("=")
        if clave == "pausa":
            pausa = float(valor)
        elif clave == "saltar":
            saltar = int(valor)
        else:
            print(f"Ajuste desconocido '{clave}' en {texto} (admitidos: pausa, saltar)")
            sys.exit(1)
    clips.append((ruta, pausa, saltar))

# Tomamos el tamaño del primer clip; los demás deben coincidir
with av.open(clips[0][0]) as primero:
    ancho, alto = primero.streams.video[0].width, primero.streams.video[0].height

# El logo se prepara una sola vez, ya escalado al ancho del vídeo
logo = preparar_logo(ruta_marca, ancho) if ruta_marca else None

salida = av.open(ruta_salida, "w")
flujo_video = salida.add_stream("libx264", rate=FPS)
flujo_video.width, flujo_video.height = ancho, alto
flujo_video.pix_fmt = "yuv420p"
flujo_video.options = {"crf": "18", "preset": "medium"}   # calidad alta, tamaño razonable
flujo_audio = salida.add_stream("aac", rate=FRECUENCIA_AUDIO)
flujo_audio.layout = "stereo"

# Convierte cualquier audio de entrada al formato común antes de codificar
remuestreador = av.AudioResampler(format="fltp", layout="stereo", rate=FRECUENCIA_AUDIO)

# Contadores de tiempo globales: los pts deben seguir creciendo de un clip al siguiente
indice_fotograma = 0
muestras_audio = 0

def escribir_fotograma(fotograma_yuv):
    """Codifica un fotograma (ya en yuv420p) con el siguiente pts global."""
    global indice_fotograma
    fotograma_yuv.pts = indice_fotograma
    fotograma_yuv.time_base = Fraction(1, FPS)
    for paquete in flujo_video.encode(fotograma_yuv):
        salida.mux(paquete)
    indice_fotograma += 1


def escribir_audio(fotograma_audio):
    """Codifica un fotograma de audio (fltp estéreo 32 kHz) con el siguiente pts global."""
    global muestras_audio
    fotograma_audio.pts = muestras_audio
    fotograma_audio.time_base = Fraction(1, FRECUENCIA_AUDIO)
    muestras_audio += fotograma_audio.samples
    for paquete in flujo_audio.encode(fotograma_audio):
        salida.mux(paquete)


def escribir_pausa(fotograma_yuv, segundos):
    """Repite el fotograma dado durante N segundos y rellena el audio con silencio."""
    for _ in range(round(segundos * FPS)):
        escribir_fotograma(fotograma_yuv)
    pendientes = round(segundos * FRECUENCIA_AUDIO)
    while pendientes > 0:
        silencio = av.AudioFrame(format="fltp", layout="stereo", samples=min(1024, pendientes))
        silencio.sample_rate = FRECUENCIA_AUDIO
        for plano in silencio.planes:
            plano.update(bytes(plano.buffer_size))
        escribir_audio(silencio)
        pendientes -= silencio.samples


for ruta_clip, pausa, saltar in clips:
    detalles = (f" (salta {saltar} fotogramas)" if saltar else "") + (f" (+ pausa de {pausa:g} s)" if pausa else "")
    print(f"Añadiendo {ruta_clip}{detalles}")
    ultimo_fotograma = None
    fotogramas_saltados = 0
    muestras_a_saltar = round(saltar / FPS * FRECUENCIA_AUDIO)   # audio equivalente a los fotogramas saltados
    with av.open(ruta_clip) as entrada:
        if (entrada.streams.video[0].width, entrada.streams.video[0].height) != (ancho, alto):
            print(f"  Tamaño distinto al primer clip ({ancho}x{alto}); aborta")
            sys.exit(1)

        # Vídeo y audio se decodifican en UNA sola pasada: si se leyera primero
        # todo el vídeo, el archivo quedaría al final y el audio saldría vacío.
        flujos = [entrada.streams.video[0]] + list(entrada.streams.audio[:1])
        for fotograma in entrada.decode(*flujos):
            if isinstance(fotograma, av.VideoFrame):
                if fotogramas_saltados < saltar:
                    fotogramas_saltados += 1
                    continue
                if limpiar or logo:
                    # Pasamos por PIL para retocar el fotograma y volvemos a fotograma de vídeo.
                    # Primero la limpieza y después la marca de agua, para que la limpieza no la altere.
                    imagen = fotograma.to_image()
                    if limpiar:
                        imagen = limpiar_fondo(imagen)
                    if logo:
                        imagen = aplicar_marca_agua(imagen, logo, opacidad_marca)
                    fotograma = av.VideoFrame.from_image(imagen)
                ultimo_fotograma = fotograma.reformat(format="yuv420p")
                escribir_fotograma(ultimo_fotograma)
            else:
                for convertido in remuestreador.resample(fotograma):
                    # Se descartan muestras enteras de audio hasta cubrir el tiempo saltado
                    if muestras_a_saltar > 0:
                        muestras_a_saltar -= convertido.samples
                        continue
                    escribir_audio(convertido)

    if pausa and ultimo_fotograma is not None:
        escribir_pausa(ultimo_fotograma, pausa)

# Vaciar los codificadores y cerrar
for paquete in flujo_video.encode():
    salida.mux(paquete)
for paquete in flujo_audio.encode():
    salida.mux(paquete)
salida.close()

print(f"Capítulo montado: {ruta_salida} ({indice_fotograma} fotogramas = {indice_fotograma / FPS:.1f} s)")
