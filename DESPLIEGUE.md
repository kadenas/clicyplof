# DESPLIEGUE — PLASTI

La producción de vídeo no se despliega en un servidor: se ejecuta en local. Requisitos y pasos para reproducirlo en otra máquina. La única pieza publicada en internet es la biblia de temporada (ver el último apartado).

## Requisitos de máquina

- GPU NVIDIA con ≥ 16 GB VRAM (probado en RTX 4060 Ti 16 GB) y **64 GB de RAM** (el modelo int8 pesa 19,5 GB y ComfyUI descarga parte a RAM). Medido el 16/09/2026 durante una generación a 768×1344: quedan **menos de 5 GB de RAM libres de 64**, y 1,8 GB de VRAM libres de 16. Con 32 GB iría muy justo. **No lanzar instalaciones ni otros trabajos pesados mientras se genera**: el sistema mata procesos por falta de memoria.
- Python 3.11 o superior en el PATH.
- ComfyUI ≥ 0.35 con los nodos nativos de MiniMax H3 (`MiniMaxH3ImageToVideo`, `VAEDecodeAudio`, `CreateVideo`, `SaveVideo`).

## Modelos necesarios

Descargar desde `https://huggingface.co/Comfy-Org/MiniMax-H3` y colocar en la carpeta de modelos de ComfyUI. En esta máquina es `D:\Comfy-Desktop\ComfyUI-Shared\models\` (carpeta compartida, no la de dentro de la instalación):

| Carpeta | Archivo |
|---|---|
| `diffusion_models/` | `minimax_h3_fl2va_pruned_int8_convrot.safetensors` |
| `loras/` | `minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors` |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` |
| `vae/` | `minimax_h3_video_vae_fp16.safetensors`, `minimax_h3_audio_vae_fp32.safetensors` |
| `upscale_models/` | `RealESRGAN_x2plus.pth` — desde `https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth` |

## Configuración

- `generar_video.py` asume ComfyUI en `http://127.0.0.1:8188`. Si cambia el puerto, editar la constante `COMFY_URL`.
- No hay claves ni secretos: todo corre en local.

## Intérpretes

- `python` (el del sistema, 3.11) para `generar_video.py`: solo usa librería estándar.
- `D:/ComfyUI/.venv/Scripts/python.exe` para todo lo de `herramientas/`: necesita PyAV, numpy, scipy y Pillow, que vienen con ComfyUI.
- `.venv-voz/Scripts/python.exe` para `faster-whisper` (transcripción y subtítulos). Se crea con `python -m venv .venv-voz` y `pip install faster-whisper`. **Aparte del entorno de ComfyUI a propósito.**

## Comandos

No hay un comando único: cada paso se lanza por separado. El procedimiento completo, con los comandos reales de la intro, los beats y el montaje, está en el `README.md`.

> Aviso: `python generar_video.py` sin argumentos **no** genera un episodio. Los valores por defecto apuntan a `workflow/tropiezo_t2v.json` y `prompts/tropiezo.txt`, que son la prueba horizontal antigua.

## Web pública: biblia de la temporada 0

Página estática en `web/`, publicada en Surge. Se abre desde cualquier dispositivo sin cuenta ni sesión.

- **URL:** https://clicyplof.surge.sh
- **Fuente:** `web/index.html`. Sin dependencias propias: solo carga las fuentes de Google Fonts. `web/CNAME` guarda el dominio para que Surge lo recuerde.
- **Cuenta:** la sesión de Surge ya abierta en esta máquina (`surge whoami`), plan gratuito.

Para volver a publicar después de editar `index.html`:

```
cd D:\CLAUDE\PLASTI\web
surge . clicyplof.surge.sh
```

Comprobación: `curl -s -o NUL -w "%{http_code}" https://clicyplof.surge.sh/` debe devolver `200`.

Por qué no basta con el artefacto de claude.ai: el artefacto (https://claude.ai/artifact/6S3nrhaehtpWFz612o3rfN) es privado y solo se abre con la sesión del propietario, así que desde otro dispositivo o para otra persona sale bloqueado. Surge lo sirve como una URL pública normal. El HTML del artefacto se guardó en `web/index.html` recolocando `<title>`, fuentes y estilos dentro de `<head>` (el visor de claude.ai los devuelve dentro del `<body>`), y añadiendo `lang="es"` y el favicon.
