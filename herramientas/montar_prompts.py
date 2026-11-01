"""
montar_prompts.py
-----------------
Escribe los prompts completos de los 8 beats de un episodio a partir de:
  - los bloques fijos de la serie (prompts/serie/BLOQUE_PERSONAJES.txt y BLOQUE_PLASTILINA.txt),
  - el guion del episodio (prompts/epNN/guion.py), que solo contiene lo propio del episodio.

Por qué existe: los bloques fijos van copiados al pie de la letra en todos los
prompts. Copiarlos a mano en ~200 prompts es la forma segura de que alguno se
quede desactualizado. Los .txt resultantes se guardan igualmente: son el
registro exacto de lo que se le pidió al modelo en cada clip.

Uso (Python de ComfyUI o del sistema, solo usa la librería estándar):
    python herramientas/montar_prompts.py ep04

El guion.py debe definir:
    OBJETOS  -> texto con los objetos de la escena (en inglés)
    BEATS    -> dict {"beat01_anomalia": {"timeline": ..., "audio": ..., "inventario": ...,
                                          "escena": "" (opcional, se añade a OBJETOS),
                                          "objetos": "" (opcional, sustituye a OBJETOS)}, ...}
"""

import sys
import runpy
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SERIE = RAIZ / "prompts" / "serie"

# Texto común a todos los beats de todos los episodios
CABECERA = ("Vertical hyper-realistic macro claymation video for a preschool show, continuing exactly from the first frame. "
            "A seamless pure white studio: white floor, plain smooth white back wall, no horizon line, soft even studio lighting "
            "with gentle contact shadows. Smooth 24fps motion, not choppy.")

CAMARA = ("Camera: static wide shot, eye level with the figures, vertical 9:16 framing, no cuts, no zoom, no camera shake. "
          "Both figures are seen in full body with their feet on the floor, and all the objects stay fully inside the frame.")

FINAL_COMUN = "No other figures, no other objects, no text on screen. The clay stays solid and consistent, no melting, no extra limbs."


def leer_bloque(nombre):
    """Lee un bloque fijo quitando las líneas de comentario (las que empiezan por ###)."""
    lineas = (SERIE / nombre).read_text(encoding="utf-8").splitlines()
    return "\n".join(l for l in lineas if not l.startswith("###")).strip()


def montar(episodio):
    carpeta = RAIZ / "prompts" / episodio
    guion = runpy.run_path(str(carpeta / "guion.py"))
    personajes = leer_bloque("BLOQUE_PERSONAJES.txt")
    plastilina = leer_bloque("BLOQUE_PLASTILINA.txt")

    for nombre, beat in guion["BEATS"].items():
        # Objetos: los del episodio, salvo que el beat los sustituya (p. ej. cuando ya se han transformado)
        escena = beat.get("objetos", guion["OBJETOS"])
        if beat.get("escena"):
            escena += " " + beat["escena"]
        partes = [CABECERA, personajes, escena, plastilina,
                  "Timeline:\n" + beat["timeline"].strip(),
                  beat.get("camara", CAMARA),
                  beat["audio"],
                  beat["inventario"] + " " + FINAL_COMUN]
        (carpeta / f"{nombre}.txt").write_text("\n\n".join(partes) + "\n", encoding="utf-8")
        print("escrito", carpeta.name + "/" + nombre + ".txt")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python herramientas/montar_prompts.py epNN")
        sys.exit(1)
    montar(sys.argv[1])
