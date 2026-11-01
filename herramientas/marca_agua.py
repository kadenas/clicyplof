"""
marca_agua.py
-------------
Superpone un logo sobre un fotograma con el modo de fusión "diferencia"
(el mismo que en Photoshop): cada píxel del resultado es |fotograma - logo|.

Con un logo de puntos claros sobre fondo negro, como el de JMR:
- el fondo negro del logo no cambia nada (diferencia con 0 = el mismo píxel),
  así que no hace falta recortarlo ni usar transparencia;
- los puntos blancos quedan oscuros sobre el fondo blanco del vídeo y con el
  color invertido si pasa un muñeco por debajo (efecto habitual de "diferencia").

La opacidad rebaja el efecto mezclando el resultado con el fotograma original,
igual que bajar la opacidad de la capa en Photoshop.

Usado por montar_capitulo.py (opción --marca-agua). Requiere Pillow.
"""

from PIL import Image, ImageChops

# Ancho del logo respecto al ancho del vídeo, y margen respecto a los bordes
# (0.08 = discreta; el primer piloto horizontal se montó con 0.12)
PROPORCION_ANCHO = 0.08
MARGEN = 0.02

# Brillo (0-255) por debajo del cual un píxel del logo se considera fondo y se
# vuelve negro puro. El PNG de JMR tiene una cuadrícula gris oscura de fondo que,
# en "diferencia", dejaría un recuadro gris visible alrededor del logo.
UMBRAL_FONDO = 80


def _quitar_fondo(valor):
    """Curva por canal: fondo oscuro → negro puro; el resto se estira hasta el blanco."""
    if valor < UMBRAL_FONDO:
        return 0
    return int((valor - UMBRAL_FONDO) * 255 / (255 - UMBRAL_FONDO))


def preparar_logo(ruta_logo, ancho_video):
    """Carga el logo, lo aplana sobre negro, limpia el fondo y lo escala al vídeo."""
    original = Image.open(ruta_logo).convert("RGBA")
    # Las zonas transparentes deben ser negras: en "diferencia" el negro es neutro
    logo = Image.new("RGB", original.size, "black")
    logo.paste(original, mask=original.split()[3])
    logo = logo.point(_quitar_fondo)

    ancho = int(ancho_video * PROPORCION_ANCHO)
    alto = int(logo.height * ancho / logo.width)
    return logo.resize((ancho, alto), Image.LANCZOS)


def aplicar_marca_agua(imagen, logo, opacidad=0.6):
    """Devuelve una copia (PIL.Image RGB) con el logo fusionado en la esquina inferior derecha."""
    imagen = imagen.convert("RGB")
    margen = int(imagen.width * MARGEN)
    x = imagen.width - logo.width - margen
    y = imagen.height - logo.height - margen

    # Solo se procesa el recuadro donde va el logo; el resto del fotograma no se toca
    region = imagen.crop((x, y, x + logo.width, y + logo.height))
    diferencia = ImageChops.difference(region, logo)
    mezclada = Image.blend(region, diferencia, opacidad)
    imagen.paste(mezclada, (x, y))
    return imagen
