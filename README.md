# PLASTI — serie "Clic y Plof", microepisodios de plastilina con ComfyUI

Produce en local microepisodios verticales de dos muñecos de plastilina de diseño propio,
**Clic** (alto y delgado: observa, compara y piensa) y **Plof** (bajito y redondo: se lanza,
empuja y se cae), sobre fondo blanco y con audio, usando **MiniMax H3** en **ComfyUI**.

Cada episodio sigue el motor narrativo de 8 beats de `docs/TATO_PLOF_VANGUARDIA_EDUCATIVA_PLAN.html`.
La idea de la serie es **"del plof al clic"**: cada episodio va de un error blando a una pieza que encaja.

## Para quién es

Para JMR Studio: serie infantil educativa (2-6 años) para YouTube. Ver `PLAN_NEGOCIO.md`.

## Cómo arrancarlo

1. Arranca ComfyUI (debe quedar escuchando en `http://127.0.0.1:8188`).
2. Rellena la ficha del episodio (`docs/PLANTILLA_FICHA_EPISODIO.md`) y escribe un prompt por beat en `prompts/epNN/`.
3. Genera y monta desde esta carpeta.

### Intro de la serie (se hace una vez y se reutiliza en todos los episodios)

Ya está hecha: `output/v_intro_cp2_00001_.mp4` (8 s). Los prompts están en `prompts/serie/`.
Para rehacerla:

```
# 1. Rótulo: el fotograma FINAL, con el título y los dos personajes de cuerpo entero
python generar_video.py --workflow workflow/titulo_qwen.json --prompt prompts/serie/rotulo.txt \
  --imagen assets/lienzo_blanco_v768.png --tamano 768x1344 --prefix clicplof/v_rotulo_cp --seed 20260916

# 2. Fotograma INICIAL: el mismo rótulo con las letras convertidas en pegotes de plastilina
python generar_video.py --workflow workflow/titulo_qwen.json --prompt prompts/serie/intro_inicio.txt \
  --imagen output/v_rotulo_cp2_00001_.png --tamano 768x1344 --prefix clicplof/v_intro_inicio --seed 20260916

# 3. Intro animada: los pegotes viajan y se forman en letras mientras los dos bailan
python generar_video.py --workflow workflow/clip_i2v_final.json --prompt prompts/serie/intro.txt \
  --imagen output/v_intro_inicio2_00001_.png --imagen-final output/v_rotulo_cp2_00001_.png \
  --tamano 768x1344 --frames 192 --prefix clicplof/v_intro_cp --seed 20260916
```

### Cierre de la serie (se hace una vez y se reutiliza en todos los episodios)

Clic y Plof abrazados saludando a cámara, y un círculo que se cierra sobre ellos. Arranca del
fotograma final de la intro (título en la pared y los dos en su pose), así salen idénticos. El
círculo no se le pide al modelo: lo pone `cerrar_iris.py`, que sale igual siempre y no cuesta GPU.

```
python generar_video.py --workflow workflow/clip_i2v.json --prompt prompts/serie/cierre.txt \
  --imagen output/v_rotulo_cp2_00001_.png --tamano 768x1344 --frames 73 --prefix clicplof/v_cierre --seed 20260916
D:/ComfyUI/.venv/Scripts/python.exe herramientas/cerrar_iris.py output/v_cierre_00001_.mp4 output/v_cierre_final.mp4 \
  --duracion 1 --cola 0.25 --centro 0.5,0.7
```

### Beats de un episodio

Duración fija por beat (`docs/TEMPORADA_0.md`): **124 fotogramas (5 s)** para Anomalía, Deseo, Mejora,
Predicción y Eco; **192 (8 s)** para Intento, Fallo y Solución. Un clip por beat, nunca dos.

```
# Beat 01 (texto → vídeo); los siguientes arrancan del último fotograma del anterior
python generar_video.py --workflow workflow/tropiezo_t2v.json --prompt prompts/ep01/beat01_anomalia.txt \
  --tamano 768x1344 --frames 124 --prefix video/plof/v_beat01
D:/ComfyUI/.venv/Scripts/python.exe herramientas/ultimo_fotograma.py output/v_beat01_00001_.mp4 \
  assets/ep01_arranque_beat02.png --limpiar-fondo
python generar_video.py --workflow workflow/clip_i2v.json --prompt prompts/ep01/beat02_deseo.txt \
  --imagen assets/ep01_arranque_beat02.png --tamano 768x1344 --frames 124 --prefix video/plof/v_beat02
```

### Careta corta (se hace una vez)

```
D:/ComfyUI/.venv/Scripts/python.exe herramientas/montar_capitulo.py output/v_careta_corta.mp4 output/v_intro_cp2_00001_.mp4@saltar=139
```

### Montaje

```
D:/ComfyUI/.venv/Scripts/python.exe herramientas/montar_capitulo.py output/epNN.mp4 \
  output/v_careta_corta.mp4 output/epNN_rotulo_clip_00001_.mp4 output/epNN_beat01_00001_.mp4 ... output/epNN_beat06_00001_.mp4@pausa=3 ... \
  output/epNN_beat08_00001_.mp4 output/v_cierre_final.mp4 \
  --limpiar-fondo --marca-agua agua.png
```

Para repetir un resultado exacto, usa `--seed <número>`; para encolar varios trabajos seguidos,
`--solo-encolar` y luego `--esperar <id>`.

## Reglas de prompt (importante)

Antes de escribir los prompts de un episodio nuevo, lee la sección **"Aprendido al generar"**
de `docs/ep01_los_colores.md`. Son las reglas que evitan que el modelo pierda o invente objetos,
y cada una salió de un clip que hubo que repetir.

Todas las opciones están en `FICHA_TECNICA.md`.
