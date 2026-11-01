"""
generar_video.py
----------------
Envía un workflow a ComfyUI (API HTTP local), espera a que termine
y descarga el vídeo resultante a la carpeta output/ del proyecto.

Uso básico (desde D:\CLAUDE\PLASTI):
    python generar_video.py

Opciones:
    --workflow  ruta al JSON en formato API   (por defecto workflow/tropiezo_t2v.json)
    --prompt    ruta al .txt con el prompt    (por defecto prompts/tropiezo.txt)
    --seed      semilla numérica; si no se indica, se genera una aleatoria
    --prefix    prefijo del archivo de salida en ComfyUI (por defecto el del workflow)
    --solo-encolar   envía el trabajo, imprime su id y termina sin esperar
                     (útil para encolar varias semillas seguidas)
    --esperar ID     no envía nada: espera un trabajo ya encolado (por su id)
                     y descarga su vídeo cuando termine
    --imagen RUTA    sube esa imagen a ComfyUI y la conecta al nodo LoadImage
                     del workflow (marcador __IMAGEN__). Sirve para el rótulo
                     y para encadenar clips (último fotograma → primer fotograma)
    --imagen-final RUTA  igual, para el marcador __IMAGEN_FINAL__: fotograma en el
                     que debe TERMINAR el vídeo (workflow clip_i2v_final.json).
                     Útil para que unas letras desordenadas acaben formando el rótulo.
    --frames N       número de fotogramas del vídeo (24 fps; debe ser 5+17k:
                     73 ≈ 3 s, 124 ≈ 5 s, 192 = 8 s)
    --tamano AxA     tamaño del vídeo o imagen en píxeles, p. ej. 864x480 (horizontal)
                     o 480x864 (vertical). Sin esta opción se usa el del workflow.

Solo usa la librería estándar de Python: no hay nada que instalar.
"""

import argparse
import json
import random
import sys
import time
import urllib.request
import urllib.error
import uuid
from pathlib import Path

# Dirección de la instancia de ComfyUI que ya está en marcha
COMFY_URL = "http://127.0.0.1:8188"

# Carpetas del proyecto (relativas a este archivo, para que funcione desde cualquier cwd)
RAIZ = Path(__file__).resolve().parent
CARPETA_SALIDA = RAIZ / "output"

# Cada cuántos segundos preguntamos a ComfyUI si ha terminado
INTERVALO_SONDEO = 5


def leer_argumentos():
    parser = argparse.ArgumentParser(description="Genera un vídeo con ComfyUI")
    parser.add_argument("--workflow", default=RAIZ / "workflow" / "tropiezo_t2v.json")
    parser.add_argument("--prompt", default=RAIZ / "prompts" / "tropiezo.txt")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--prefix", default=None)
    parser.add_argument("--solo-encolar", action="store_true")
    parser.add_argument("--esperar", default=None, metavar="ID")
    parser.add_argument("--imagen", default=None, metavar="RUTA")
    parser.add_argument("--imagen-final", default=None, metavar="RUTA")
    parser.add_argument("--frames", type=int, default=None, metavar="N")
    parser.add_argument("--tamano", default=None, metavar="ANCHOxALTO")
    return parser.parse_args()


def interpretar_tamano(texto):
    """Convierte '864x480' en la tupla (864, 480). Devuelve None si no se indicó."""
    if not texto:
        return None
    try:
        ancho, alto = texto.lower().split("x")
        return int(ancho), int(alto)
    except ValueError:
        print(f"Tamaño no válido: '{texto}'. Usa el formato ANCHOxALTO, p. ej. 864x480")
        sys.exit(1)


def subir_imagen(ruta_imagen):
    """Sube una imagen a la carpeta input/ de ComfyUI y devuelve el nombre con el que quedó."""
    ruta = Path(ruta_imagen)
    contenido = ruta.read_bytes()
    # Petición multipart/form-data construida a mano (sin librerías externas)
    limite = "----PlastiLimite" + uuid.uuid4().hex
    cuerpo = (
        f"--{limite}\r\n"
        f'Content-Disposition: form-data; name="image"; filename="{ruta.name}"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode("utf-8") + contenido + (
        f"\r\n--{limite}\r\n"
        f'Content-Disposition: form-data; name="overwrite"\r\n\r\ntrue\r\n'
        f"--{limite}--\r\n"
    ).encode("utf-8")
    peticion = urllib.request.Request(
        COMFY_URL + "/upload/image",
        data=cuerpo,
        headers={"Content-Type": f"multipart/form-data; boundary={limite}"},
    )
    with urllib.request.urlopen(peticion, timeout=60) as respuesta:
        return json.loads(respuesta.read().decode("utf-8"))["name"]


def cargar_workflow(ruta_workflow, ruta_prompt, seed, prefix, nombre_imagen=None, frames=None, tamano=None,
                    nombre_imagen_final=None):
    """Carga el JSON del workflow e inserta prompt, semilla, prefijo, imágenes, duración y tamaño."""
    workflow = json.loads(Path(ruta_workflow).read_text(encoding="utf-8"))
    texto_prompt = Path(ruta_prompt).read_text(encoding="utf-8").strip()

    for nodo in workflow.values():
        entradas = nodo["inputs"]
        tipo = nodo["class_type"]
        # El marcador __PROMPT__ se sustituye por el texto del archivo .txt
        if entradas.get("prompt") == "__PROMPT__":
            entradas["prompt"] = texto_prompt
        # El marcador __IMAGEN__ se sustituye por la imagen subida con --imagen
        if entradas.get("image") == "__IMAGEN__":
            if not nombre_imagen:
                print("Este workflow necesita una imagen: pásala con --imagen RUTA")
                sys.exit(1)
            entradas["image"] = nombre_imagen
        # El marcador __IMAGEN_FINAL__ se sustituye por la imagen subida con --imagen-final
        if entradas.get("image") == "__IMAGEN_FINAL__":
            if not nombre_imagen_final:
                print("Este workflow necesita una imagen final: pásala con --imagen-final RUTA")
                sys.exit(1)
            entradas["image"] = nombre_imagen_final
        # Semilla: si el usuario no da una, usamos una aleatoria para que cada
        # ejecución produzca un resultado distinto (RandomNoise en vídeo, KSampler en imagen)
        if tipo == "RandomNoise":
            entradas["noise_seed"] = seed if seed is not None else random.randint(0, 2**53)
        if tipo == "KSampler":
            entradas["seed"] = seed if seed is not None else random.randint(0, 2**53)
        # Duración en fotogramas (solo nodos de vídeo MiniMax)
        if frames and tipo == "MiniMaxH3ImageToVideo":
            entradas["length"] = frames
        # Tamaño en píxeles: el nodo de vídeo MiniMax y el reescalado final del
        # workflow de rótulos (ImageScale) llevan width/height fijos en el JSON;
        # con --tamano se sobrescriben los dos para cambiar de vertical a horizontal
        if tamano and tipo in ("MiniMaxH3ImageToVideo", "ImageScale"):
            entradas["width"], entradas["height"] = tamano
        # Prefijo de salida opcional (vídeo o imagen)
        if prefix and tipo in ("SaveVideo", "SaveImage"):
            entradas["filename_prefix"] = prefix

    return workflow


def peticion_json(ruta, datos=None):
    """GET (sin datos) o POST (con datos) contra la API de ComfyUI. Devuelve el JSON."""
    cuerpo = json.dumps(datos).encode("utf-8") if datos is not None else None
    cabeceras = {"Content-Type": "application/json"} if datos is not None else {}
    peticion = urllib.request.Request(COMFY_URL + ruta, data=cuerpo, headers=cabeceras)
    with urllib.request.urlopen(peticion, timeout=30) as respuesta:
        return json.loads(respuesta.read().decode("utf-8"))


def encolar(workflow):
    """Envía el workflow a la cola de ComfyUI y devuelve el id del trabajo."""
    respuesta = peticion_json("/prompt", {"prompt": workflow, "client_id": str(uuid.uuid4())})
    if respuesta.get("node_errors"):
        print("ComfyUI ha rechazado el workflow:")
        print(json.dumps(respuesta["node_errors"], indent=2, ensure_ascii=False))
        sys.exit(1)
    return respuesta["prompt_id"]


def esperar_resultado(prompt_id):
    """Sondea /history hasta que el trabajo aparece como terminado. Devuelve sus outputs."""
    inicio = time.time()
    while True:
        historial = peticion_json(f"/history/{prompt_id}")
        if prompt_id in historial:
            entrada = historial[prompt_id]
            estado = entrada.get("status", {})
            if estado.get("status_str") == "error":
                print("\nComfyUI ha devuelto un error durante la ejecución:")
                for mensaje in estado.get("messages", []):
                    print("  ", mensaje)
                sys.exit(1)
            return entrada["outputs"]
        transcurrido = int(time.time() - inicio)
        print(f"\r  generando... {transcurrido // 60:02d}:{transcurrido % 60:02d}", end="", flush=True)
        time.sleep(INTERVALO_SONDEO)


def descargar_videos(outputs):
    """Busca los vídeos en los outputs y los descarga a output/ del proyecto."""
    CARPETA_SALIDA.mkdir(exist_ok=True)
    descargados = []
    for salida_nodo in outputs.values():
        # SaveVideo publica sus archivos bajo la clave "images" (con formato mp4)
        # o "videos" según la versión; comprobamos ambas
        for clave in ("videos", "images", "gifs"):
            for archivo in salida_nodo.get(clave, []):
                nombre = archivo["filename"]
                subcarpeta = archivo.get("subfolder", "")
                consulta = f"/view?filename={nombre}&subfolder={subcarpeta}&type=output"
                destino = CARPETA_SALIDA / nombre
                with urllib.request.urlopen(COMFY_URL + consulta, timeout=120) as origen:
                    destino.write_bytes(origen.read())
                descargados.append(destino)
    return descargados


def esperar_y_descargar(prompt_id):
    """Espera a que termine el trabajo indicado y descarga su vídeo a output/."""
    inicio = time.time()
    outputs = esperar_resultado(prompt_id)
    duracion = int(time.time() - inicio)
    print(f"\nTerminado en {duracion // 60} min {duracion % 60} s")

    videos = descargar_videos(outputs)
    if not videos:
        print("El trabajo terminó pero no se encontró ningún archivo en los outputs:")
        print(json.dumps(outputs, indent=2, ensure_ascii=False))
        sys.exit(1)
    for ruta in videos:
        print(f"Archivo guardado en: {ruta}")


def main():
    args = leer_argumentos()

    # Comprobación previa: ¿está ComfyUI encendido?
    try:
        peticion_json("/system_stats")
    except (urllib.error.URLError, OSError):
        print(f"No hay ComfyUI escuchando en {COMFY_URL}. Arráncalo y vuelve a intentarlo.")
        sys.exit(1)

    # Modo "esperar": el trabajo ya está en ComfyUI, solo recogemos el resultado
    if args.esperar:
        print(f"Esperando al trabajo {args.esperar}")
        esperar_y_descargar(args.esperar)
        return

    # Si hay imagen de entrada, primero la subimos a ComfyUI
    nombre_imagen = None
    if args.imagen:
        nombre_imagen = subir_imagen(args.imagen)
        print(f"Imagen subida a ComfyUI como: {nombre_imagen}")
    nombre_imagen_final = None
    if args.imagen_final:
        nombre_imagen_final = subir_imagen(args.imagen_final)
        print(f"Imagen final subida a ComfyUI como: {nombre_imagen_final}")

    workflow = cargar_workflow(
        args.workflow, args.prompt, args.seed, args.prefix,
        nombre_imagen, args.frames, interpretar_tamano(args.tamano),
        nombre_imagen_final,
    )
    semilla = next(
        n["inputs"].get("noise_seed", n["inputs"].get("seed"))
        for n in workflow.values() if n["class_type"] in ("RandomNoise", "KSampler")
    )
    print(f"Enviando workflow a ComfyUI (seed = {semilla})")

    prompt_id = encolar(workflow)
    print(f"Trabajo encolado: {prompt_id}")

    # Modo "solo encolar": terminamos aquí; se recoge después con --esperar
    if args.solo_encolar:
        return

    esperar_y_descargar(prompt_id)


if __name__ == "__main__":
    main()
