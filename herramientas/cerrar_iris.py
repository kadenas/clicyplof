"""
cerrar_iris.py
--------------
Cierra un clip con un círculo que se encoge (el "iris" clásico de los dibujos
animados): la imagen solo se ve dentro de un círculo cada vez más pequeño,
hasta que todo el cuadro queda de un color liso. El audio se conserva.

Pensado para el clip de cierre de la serie: se genera una vez con MiniMax H3
(Clic y Plof abrazados), se le aplica este cierre y el resultado se reutiliza
en todos los episodios. El círculo NO se le pide al modelo de vídeo: hecho
aquí sale idéntico siempre y no cuesta GPU.

Ejecutar con el Python del entorno de ComfyUI (tiene PyAV y numpy):
    D:/ComfyUI/.venv/Scripts/python.exe herramientas/cerrar_iris.py entrada.mp4 salida.mp4 [opciones]

Opciones:
    --duracion S           segundos que tarda el círculo en cerrarse, al final del clip (1.0)
    --cola S               segundos de color liso que se añaden después, en silencio (0.25)
    --color negro|blanco   color de fuera del círculo (negro)
    --centro X,Y           centro del círculo en fracción del ancho y del alto (0.5,0.7:
                           donde quedan los muñecos en el plano fijo de la serie)
"""

import argparse
from fractions import Fraction
import numpy as np
import av

FPS = 24
FRECUENCIA_AUDIO = 32000
COLORES = {"negro": (0, 0, 0), "blanco": (255, 255, 255)}

# ── Línea de comandos ────────────────────────────────────────────────────────
parser = argparse.ArgumentParser(description="Cierra un clip con un círculo que se encoge.")
parser.add_argument("entrada", help="mp4 de entrada")
parser.add_argument("salida", help="mp4 de salida")
parser.add_argument("--duracion", type=float, default=1.0, metavar="S")
parser.add_argument("--cola", type=float, default=0.25, metavar="S")
parser.add_argument("--color", choices=COLORES, default="negro")
parser.add_argument("--centro", default="0.5,0.7", metavar="X,Y")
args = parser.parse_args()

centro_x, centro_y = (float(v) for v in args.centro.split(","))
color = np.array(COLORES[args.color], dtype=np.float32)

# ── Datos del clip: tamaño y número de fotogramas ────────────────────────────
# Hace falta saber cuántos fotogramas hay ANTES de procesarlos, para calcular
# en cuál empieza el cierre. Se abre el archivo aparte para contarlos.
with av.open(args.entrada) as entrada:
    flujo = entrada.streams.video[0]
    ancho, alto = flujo.width, flujo.height
    total_fotogramas = flujo.frames
    if not total_fotogramas:   # algunos contenedores no lo declaran: se cuenta a mano
        total_fotogramas = sum(1 for _ in entrada.decode(video=0))

fotogramas_iris = min(round(args.duracion * FPS), total_fotogramas)
primer_fotograma_iris = total_fotogramas - fotogramas_iris

# ── Geometría del círculo ────────────────────────────────────────────────────
# Distancia de cada píxel al centro, calculada una sola vez.
# El radio inicial llega a la esquina más lejana, así el primer fotograma del
# cierre muestra el cuadro entero y el círculo empieza a "morder" por las esquinas.
cx, cy = centro_x * ancho, centro_y * alto
ys, xs = np.mgrid[0:alto, 0:ancho]
distancia = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2).astype(np.float32)
radio_maximo = max(np.hypot(cx - x, cy - y) for x in (0, ancho) for y in (0, alto))


def aplicar_iris(imagen_rgb, progreso):
    """Deja ver la imagen solo dentro del círculo. progreso: 0 = abierto, 1 = cerrado."""
    radio = radio_maximo * (1.0 - progreso)
    # Borde suavizado de ~2 px para que el círculo no salga dentado
    mascara = np.clip((radio - distancia) / 2.0 + 0.5, 0.0, 1.0)[..., None]
    mezcla = imagen_rgb.astype(np.float32) * mascara + color * (1.0 - mascara)
    return mezcla.astype(np.uint8)


# ── Salida: mismo formato que genera ComfyUI y que espera montar_capitulo.py ─
salida = av.open(args.salida, "w")
flujo_video = salida.add_stream("libx264", rate=FPS)
flujo_video.width, flujo_video.height = ancho, alto
flujo_video.pix_fmt = "yuv420p"
flujo_video.options = {"crf": "18", "preset": "medium"}
flujo_audio = salida.add_stream("aac", rate=FRECUENCIA_AUDIO)
flujo_audio.layout = "stereo"
remuestreador = av.AudioResampler(format="fltp", layout="stereo", rate=FRECUENCIA_AUDIO)

indice_fotograma = 0
muestras_audio = 0


def escribir_fotograma(imagen_rgb):
    """Codifica una imagen RGB (numpy) con el siguiente pts global."""
    global indice_fotograma
    fotograma = av.VideoFrame.from_ndarray(imagen_rgb, format="rgb24").reformat(format="yuv420p")
    fotograma.pts = indice_fotograma
    fotograma.time_base = Fraction(1, FPS)
    for paquete in flujo_video.encode(fotograma):
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


def escribir_cola(segundos):
    """Añade N segundos de color liso con silencio, para que el cierre respire."""
    lienzo = np.empty((alto, ancho, 3), dtype=np.uint8)
    lienzo[:] = color.astype(np.uint8)
    for _ in range(round(segundos * FPS)):
        escribir_fotograma(lienzo)
    pendientes = round(segundos * FRECUENCIA_AUDIO)
    while pendientes > 0:
        silencio = av.AudioFrame(format="fltp", layout="stereo", samples=min(1024, pendientes))
        silencio.sample_rate = FRECUENCIA_AUDIO
        for plano in silencio.planes:
            plano.update(bytes(plano.buffer_size))
        escribir_audio(silencio)
        pendientes -= silencio.samples


# ── Proceso ──────────────────────────────────────────────────────────────────
print(f"{args.entrada}: {total_fotogramas} fotogramas ({total_fotogramas / FPS:.2f} s); "
      f"el círculo se cierra en los últimos {fotogramas_iris} ({args.duracion:g} s)")

with av.open(args.entrada) as entrada:
    # Vídeo y audio se decodifican en UNA sola pasada: si se leyera primero
    # todo el vídeo, el audio saldría vacío (aprendido en montar_capitulo.py).
    flujos = [entrada.streams.video[0]] + list(entrada.streams.audio[:1])
    leidos = 0
    for fotograma in entrada.decode(*flujos):
        if isinstance(fotograma, av.VideoFrame):
            imagen = fotograma.to_ndarray(format="rgb24")
            if leidos >= primer_fotograma_iris:
                # progreso de 1/n en el primer fotograma del cierre a 1 en el último
                progreso = (leidos - primer_fotograma_iris + 1) / fotogramas_iris
                imagen = aplicar_iris(imagen, progreso)
            escribir_fotograma(imagen)
            leidos += 1
        else:
            for convertido in remuestreador.resample(fotograma):
                escribir_audio(convertido)

if args.cola > 0:
    escribir_cola(args.cola)

for paquete in flujo_video.encode():
    salida.mux(paquete)
for paquete in flujo_audio.encode():
    salida.mux(paquete)
salida.close()

print(f"Cierre aplicado: {args.salida} ({indice_fotograma} fotogramas = {indice_fotograma / FPS:.2f} s)")
