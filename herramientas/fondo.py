"""
fondo.py
--------
Función compartida por ultimo_fotograma.py y montar_capitulo.py:
empuja hacia el blanco puro los píxeles claros y poco saturados (el fondo
del estudio), sin tocar los muñecos (azul saturado) ni las zonas oscuras.

Sirve para corregir la deriva que aparece al encadenar clips: cada
generación hereda los artefactos de la anterior y el fondo se va
volviendo gris y manchado.
"""

import numpy as np
from PIL import Image, ImageFilter

# Parámetros de la limpieza de fondo
UMBRAL_BRILLO = 150      # a partir de este brillo (0-255) un píxel puede ser "fondo"
UMBRAL_SATURACION = 25   # por debajo de esta saturación (max-min RGB) un píxel puede ser "fondo"
FUERZA = 0.85            # cuánto se acerca el fondo al blanco (1 = blanco puro)


def limpiar_fondo(imagen):
    """Devuelve una copia (PIL.Image RGB) con el fondo claro empujado hacia el blanco."""
    rgb = np.asarray(imagen.convert("RGB")).astype(np.float32)
    brillo = rgb.mean(axis=2)
    saturacion = rgb.max(axis=2) - rgb.min(axis=2)

    # Máscara suave (0-1): 1 = claramente fondo, 0 = muñeco/sombra.
    # Las transiciones graduales evitan bordes duros alrededor de las figuras.
    mascara = np.clip((brillo - UMBRAL_BRILLO) / 40.0, 0, 1) * np.clip((UMBRAL_SATURACION - saturacion) / 15.0, 0, 1)
    mascara = Image.fromarray((mascara * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(5))
    mascara = np.asarray(mascara).astype(np.float32) / 255.0

    limpio = rgb + (255.0 - rgb) * mascara[..., None] * FUERZA
    return Image.fromarray(np.clip(limpio, 0, 255).astype(np.uint8))


# --- Corrección de la deriva del azul de los muñecos (añadido el 01/11/2026) ---
# Al encadenar clips el azul de Clic y Plof se oscurece un poco en cada enlace
# (medido en el ep02: de B=202 a B=163 en siete enlaces). Esta función devuelve
# el azul de los muñecos al de la referencia (assets/personajes_referencia.png)
# en el fotograma de arranque, antes de generar el clip siguiente.
AZUL_REFERENCIA = np.array([25.0, 128.0, 202.0])   # medido en la referencia


def mascara_munecos(rgb):
    """Máscara suave (0-1) del azul vivo de los muñecos.

    Deja fuera el azul marino (G muy bajo), el morado (R alto) y el fondo.
    """
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    return (np.clip((b - r - 70) / 30, 0, 1)
            * np.clip((g - 60) / 20, 0, 1)
            * np.clip((b - 100) / 30, 0, 1))


def corregir_azul(imagen):
    """Devuelve una copia (PIL.Image RGB) con el azul de los muñecos llevado al de la referencia."""
    rgb = np.asarray(imagen.convert("RGB")).astype(np.float32)
    mascara = mascara_munecos(rgb)
    nucleo = mascara > 0.9          # píxeles que son muñeco seguro: con ellos se mide el azul actual
    if nucleo.sum() < 500:          # no hay muñecos a la vista: no se toca nada
        return imagen.convert("RGB")
    ganancia = AZUL_REFERENCIA / rgb[nucleo].mean(axis=0)
    # Suavizar el borde de la máscara para que no se note el recorte
    mascara = Image.fromarray((mascara * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.5))
    mascara = np.asarray(mascara).astype(np.float32) / 255.0
    corregido = rgb * (1 + (ganancia - 1) * mascara[..., None])
    return Image.fromarray(np.clip(corregido, 0, 255).astype(np.uint8))
