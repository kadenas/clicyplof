# FICHA TÉCNICA — PLASTI / serie "Clic y Plof"

## Información general

- **Nombre:** PLASTI (nombre interno del proyecto). Serie: **"Clic y Plof"** (renombrada el 16/09/2026; antes "Plof", con el personaje A llamado "Tato"). Personajes: **Clic** (alto y delgado; observa, compara y piensa) y **Plof** (bajito y redondo; se lanza, empuja y se cae). La idea de serie es "del plof al clic".
- **Descripción:** Producción local de microepisodios verticales de plastilina (claymation) con audio, mediante ComfyUI y el modelo MiniMax H3, siguiendo el motor narrativo de 8 beats de `docs/TATO_PLOF_VANGUARDIA_EDUCATIVA_PLAN.html`.
- **Objetivo:** Serie infantil educativa (2-6 años) para YouTube (Shorts + recopilaciones), sin depender de servicios externos.
- **Problema que resuelve:** Automatiza el envío de workflows a ComfyUI, el encadenado de clips, los rótulos y el montaje, separando el guion (prompts de texto) del workflow (JSON).

## Arquitectura

- **Frontend:** ninguno; línea de comandos.
- **Backend:** ComfyUI 0.35.1 en local (`http://127.0.0.1:8188`).
- **Base de datos:** no aplica.
- **APIs externas:** ninguna (todo corre en local).
- **Autenticación:** no aplica.
- **Hosting / despliegue:** máquina local con GPU NVIDIA RTX 4060 Ti 16 GB y 64 GB RAM. La biblia de temporada (`web/`) es una página estática publicada en Surge: https://clicyplof.surge.sh

## Stack tecnológico

- **Lenguajes:** Python 3.11. `generar_video.py` solo usa librería estándar; las herramientas de `herramientas/` usan PyAV, numpy, scipy y Pillow del entorno de ComfyUI (`D:/ComfyUI/.venv/Scripts/python.exe`).
- **Modelos** (en `D:\Comfy-Desktop\ComfyUI-Shared\models\`):
  - `diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors` — vídeo + audio (voz, efectos y música nativos).
  - `loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors` — LoRA turbo: 8 pasos.
  - `text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` — codificador de texto.
  - `vae/minimax_h3_video_vae_fp16.safetensors` y `vae/minimax_h3_audio_vae_fp32.safetensors`.
  - `upscale_models/RealESRGAN_x2plus.pth` (instalado el 16/09/2026) — escalado ×2 para subir la salida a 1080×1920 antes de publicar. Se usa con los nodos `UpscaleModelLoader` e `ImageUpscaleWithModel`, que ya son del núcleo de ComfyUI. **Pendiente de comparar contra un reescalado Lanczos**, que es gratis y en un salto de solo 1,4× puede quedarse muy cerca.
  - Qwen Image Edit 2511 (`qwen_image_edit_2511_int8_convrot` + LoRA Lightning 4 pasos) — **solo para imágenes fijas** de rótulos con texto (los modelos de vídeo escriben mal).
- **Dependencias Python adicionales:** ninguna para generar y montar. Aparte, `.venv-voz/` es un entorno virtual **independiente del de ComfyUI** con `faster-whisper`, para transcribir el audio generado, medir en qué segundo exacto cae la voz de la narradora (llega 1-2 s tarde respecto al prompt) y sacar subtítulos. Se mantiene separado a propósito: arrastra `ctranslate2` con sus propias versiones y no merece la pena arriesgar la instalación de ComfyUI.

## Estructura de carpetas

```
PLASTI/
├── generar_video.py            # envía un workflow a ComfyUI, espera y descarga el resultado
├── agua.png                    # logo JMR para la marca de agua
├── herramientas/               # ejecutar con el Python de ComfyUI (PyAV, numpy, scipy, Pillow)
│   ├── fondo.py                #   limpieza de fondo compartida (empuja el fondo claro al blanco)
│   ├── ultimo_fotograma.py     #   extrae el último fotograma de un mp4 (para encadenar clips)
│   ├── montar_capitulo.py      #   une mp4 con audio: limpieza, marca de agua, pausas y recortes
│   ├── marca_agua.py           #   logo en fusión "diferencia" (usado por montar_capitulo)
│   ├── cerrar_iris.py          #   círculo que se cierra al final de un clip (cierre de la serie), conserva el audio
│   └── desordenar_letras.py    #   recorta las letras de un rótulo y las esparce (arranque de la intro)
├── prompts/
│   ├── serie/                  #   piezas fijas de la serie: rotulo, intro_inicio, intro, cierre, BLOQUE_PLASTILINA
│   ├── ep01/                   #   episodio 01 "Los colores" (vertical): rótulo, título, intro, beat01..08
│   └── *.txt                   #   capítulo 1 y piloto horizontal v1 (históricos)
├── workflow/                   # workflows ComfyUI en formato API con marcadores __PROMPT__, __IMAGEN__, __IMAGEN_FINAL__
│   ├── tropiezo_t2v.json       #   MiniMax H3 texto → vídeo
│   ├── clip_i2v.json           #   MiniMax H3 imagen → vídeo (first_frame)
│   ├── clip_i2v_final.json     #   igual, con fotograma final (last_frame): letras que se montan
│   └── titulo_qwen.json        #   Qwen Image Edit: rótulo a partir de un lienzo blanco
├── assets/                     # lienzos blancos (vertical 720×1296, horizontal 1296×720, vertical 768×1344),
│                               # fotogramas de arranque de cada clip y letras desordenadas
├── docs/                       # guía de la serie (HTML), plantilla de ficha de episodio, fichas por episodio
├── web/                        # biblia de la temporada 0 como página estática (index.html + CNAME), publicada en https://clicyplof.surge.sh
├── output/                     # vídeos e imágenes descargados y capítulos montados
├── README.md · FICHA_TECNICA.md · HANDOFF.md · DESPLIEGUE.md · PLAN_NEGOCIO.md
```

## Flujo de un episodio (motor de 8 beats)

1. **Ficha de episodio** (`docs/PLANTILLA_FICHA_EPISODIO.md` → `docs/epNN_titulo.md`) y go/no-go antes de generar nada.
2. **Intro de la serie**: ya está hecha y se reutiliza tal cual en todos los episodios (`output/v_intro_cp2_00001_.mp4`). No hay que regenerarla por episodio. Los prompts están en `prompts/serie/` y el procedimiento completo, en el `README.md`.
3. *(Histórico, ya no se usa)* La primera intro se hacía recortando las letras del rótulo con `desordenar_letras.py` y esparciéndolas. Se sustituyó por pedirle a **Qwen Image Edit** que convierta las letras del rótulo en pegotes informes de plastilina: mantiene a los personajes idénticos entre el primer y el último fotograma, que es lo que el modelo de vídeo necesita para no cambiarlos.
4. **Título del episodio** con Qwen si el episodio lleva rótulo propio: `titulo_qwen.json` sobre `assets/lienzo_blanco_v768.png`, `--tamano 768x1344`.
5. **Beat 01** (cambiado el 01/11/2026, regla 8): **nunca con texto solo.** Qwen (`titulo_qwen.json`) parte de `assets/personajes_referencia.png` y añade el atrezo del episodio → `assets/epNN_arranque_beat01.png`; luego `clip_i2v.json` (5 s) desde esa imagen. Todos los prompts llevan `prompts/serie/BLOQUE_PERSONAJES.txt`. Motivo y ficha de los personajes en `docs/PERSONAJES.md`. *(Hasta el ep03 se usaba `tropiezo_t2v.json`, y los personajes salían distintos a los de la intro.)*
6. **Beats 02-08**: cada uno arranca del último fotograma del anterior (`ultimo_fotograma.py --limpiar-fondo --corregir-azul` → `--imagen`). **Siempre con `--tamano 768x1344`**: el workflow trae 480×864 por defecto. Los prompts se montan con `herramientas/montar_prompts.py epNN` a partir de `prompts/epNN/guion.py`. **Duración fija por beat** (decidida el 16/09/2026): 5 s (124 fotogramas) para Anomalía, Deseo, Mejora, Predicción y Eco; 8 s (192) para Intento, Fallo y Solución. Un clip por beat, nunca dos. La pausa de 3 s del beat 06 se añade en el montaje.
7. **Cierre de la serie** (una sola vez, se reutiliza): `clip_i2v.json` a 3 s (73 fotogramas) desde `output/v_rotulo_cp2_00001_.png` con `prompts/serie/cierre.txt`, y después `cerrar_iris.py` para el círculo que se cierra → `output/v_cierre_final.mp4`.
8. **Montaje**: `montar_capitulo.py salida.mp4 intro.mp4@saltar=8 titulo.mp4@saltar=8 beat01.mp4 ... beat06.mp4@pausa=3 ... beat08.mp4 v_cierre_final.mp4 --limpiar-fondo --marca-agua agua.png`.

### Opciones de `generar_video.py`

| Opción | Uso |
|---|---|
| `--workflow`, `--prompt`, `--seed`, `--prefix` | workflow JSON, prompt .txt, semilla, prefijo de salida |
| `--solo-encolar` / `--esperar ID` | encolar sin esperar / recoger un trabajo encolado |
| `--imagen RUTA` | fotograma inicial (marcador `__IMAGEN__`) |
| `--imagen-final RUTA` | fotograma final (marcador `__IMAGEN_FINAL__`, workflow `clip_i2v_final.json`) |
| `--frames N` | duración: 73 ≈ 3 s, 124 ≈ 5 s, 192 = 8 s (rejilla 5 + 17k) |
| `--tamano AxA` | resolución: `768x1344` vertical (actual), `864x480` horizontal, `480x864` vertical 480p |

### Ajustes de `montar_capitulo.py`

- `--limpiar-fondo`: blanco uniforme en todo el capítulo (evita la deriva gris al encadenar).
- `--marca-agua logo.png [--opacidad-marca 0.6]`: logo en la esquina inferior derecha con fusión "diferencia" (el fondo negro del logo es neutro; los puntos claros salen oscuros sobre blanco). Tamaño: 8 % del ancho (`PROPORCION_ANCHO` en `marca_agua.py`).
- `clip.mp4@pausa=3`: congela el último fotograma 3 s en silencio (pausa de predicción).
- `clip.mp4@saltar=8`: descarta los 8 primeros fotogramas (oculta el salto cuando el clip arranca de una imagen compuesta).

## Parámetros del modelo

| Parámetro | Valor | Motivo |
|---|---|---|
| Resolución | 768 × 1344 (vertical) | resolución nativa del modelo (1344×768) girada; múltiplos de 32 obligatorios |
| Duración | 5 + 17k fotogramas @ 24 fps | rejilla del modelo; rango entrenado 124-362 |
| Sampler / scheduler | `res_multistep` / `simple`, 8 pasos | LoRA turbo |
| `first_frame` / `last_frame` | opcionales | continuidad entre clips / final garantizado |

### Tiempos medidos (RTX 4060 Ti 16 GB)

| Tamaño | 3 s | 5 s | 8 s |
|---|---|---|---|
| 480×864 / 864×480 | — | ~3,5 min | ~5,7 min |
| 768×1344 | ~5 min | ~13 min | ~21,5 min |
| Rótulo Qwen | 20-35 s | | |

Un episodio de 8 beats a 768×1344 son unas 2,5-3 h de GPU sin retomas.

### Deriva al encadenar clips

Cada generación hereda artefactos del fotograma anterior: el fondo se vuelve gris y el azul de los muñecos se oscurece ligeramente. `--limpiar-fondo` corrige el fondo (en el arranque y en el montaje); el color de los muñecos no se corrige todavía.

## Ejecución local

1. Arrancar ComfyUI y comprobar que responde en el puerto 8188.
2. `python generar_video.py ...` (Python del sistema) para generar; `D:/ComfyUI/.venv/Scripts/python.exe herramientas/...` para las herramientas.
3. El script sondea `/history` cada 5 s y descarga el resultado a `output/`.

## Despliegue

La producción es local. Lo único publicado en internet es la biblia de temporada (`web/`), subida a https://clicyplof.surge.sh con `surge`. Ver `DESPLIEGUE.md`.

## Estado actual

Ver `HANDOFF.md`.

- **Episodio 03 "El balón de arriba" montado** (17/09/2026): `output/ep03_el_balon_de_arriba.mp4` (61,3 s), primer episodio con el sistema nuevo completo (duraciones por beat, careta corta, rótulo, cierre). Pendiente de revisión de audio por el usuario.
- Episodio 01 "Los colores" **terminado y montado**: `output/plof_ep01_v2.mp4` (768×1344, 71,7 s). Validado con un niño real el 15/09/2026: lo vio entero y quiso repetirlo.
- **Intro de la serie terminada** (16/09/2026): `output/v_intro_cp2_00001_.mp4` (8 s). Los dos personajes de cuerpo entero bailando mientras nueve pegotes de plastilina viajan por la pared y se forman en las letras de "CLIC y PLOF".
- **Duración de los beats decidida** (16/09/2026): 5 s los de situación, 8 s los tres de acción; historia de 52 s y Short ≈ 61 s. Análisis en `docs/DECISION_DURACION_CLIPS.md`. El ep. 01 (8 × 8 s) se queda como está.
- **Cierre de la serie generado** (16/09/2026): `output/v_cierre_final.mp4` (3,3 s, con el círculo ya aplicado). Se reutiliza en todos los episodios; no se regenera. Bruto en `output/v_cierre_00001_.mp4`.
- **Careta corta hecha** (17/09/2026): `output/v_careta_corta.mp4` (2,2 s), recorte de la intro con `@saltar=139`.
- Pendiente: volver a montar el episodio 01 con la intro nueva (el montaje actual lleva el rótulo antiguo "PLOF").
- Piloto horizontal v1 en `output/plof_ep01_los_colores.mp4`: referencia visual, no se publica.
