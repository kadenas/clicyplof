#!/bin/bash
# Ejemplo: bash herramientas/cadena_beats.sh ep04 01 02:deseo:124 03:intento:192 04:fallo:192 05:mejora:124 06:prediccion:124 07:solucion:192 08:eco:124
# (el beat 01 se genera antes, a mano, desde assets/epNN_arranque_beat01.png con --tamano 768x1344)
# Encadena beats de un episodio: arranque = último fotograma (fondo limpio + azul corregido) del beat anterior.
# Usa siempre el clip MÁS RECIENTE de cada beat (ComfyUI numera _00001_, _00002_... al repetir).
# Uso: bash herramientas/cadena_beats.sh EP BEAT_ANTERIOR "NN:nombre:fotogramas" ...
cd /d/CLAUDE/PLASTI
PY=D:/ComfyUI/.venv/Scripts/python.exe
ultimo_clip() { ls -t output/${1}_beat${2}_0*_.mp4 2>/dev/null | head -1; }
EP=$1; ANT=$2; shift 2
for item in "$@"; do
  IFS=: read NN NOMBRE FR <<< "$item"
  PREVIO=$(ultimo_clip $EP $ANT); [ -n "$PREVIO" ] || { echo "No encuentro el beat $ANT"; exit 1; }
  $PY herramientas/ultimo_fotograma.py "$PREVIO" assets/${EP}_arranque_beat${NN}.png --limpiar-fondo --corregir-azul > /dev/null || exit 1
  ANTES=$(ultimo_clip $EP $NN); inicio=$(date +%s)
  PYTHONUNBUFFERED=1 py generar_video.py --workflow workflow/clip_i2v.json --prompt prompts/${EP}/beat${NN}_${NOMBRE}.txt \
     --imagen assets/${EP}_arranque_beat${NN}.png --frames $FR --tamano 768x1344 --seed 20260916 --prefix ${EP}_beat${NN} 2>&1 | tr '\r' '\n' | grep -E "Archivo guardado|rror"
  NUEVO=$(ultimo_clip $EP $NN)
  [ -n "$NUEVO" ] && [ "$NUEVO" != "$ANTES" ] || { echo "FALLO beat $NN"; exit 1; }
  echo "beat $NN hecho en $(( ($(date +%s)-inicio)/60 )) min -> $NUEVO (desde $PREVIO)"
  ANT=$NN
done
