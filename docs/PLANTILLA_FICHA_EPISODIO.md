# FICHA DE EPISODIO — plantilla

Rellenar ANTES de generar nada (sección 06 de `TATO_PLOF_VANGUARDIA_EDUCATIVA_PLAN.html`).
Copiar este archivo como `docs/epNN_titulo.md`.

## Datos

- **Episodio:** 
- **Título:** 
- **Dominio del currículo:** (posición · cantidad · forma · causa · emoción · cooperar · creatividad)
- **Motor de historia:** (encontrar · construir · transportar · compartir)
- **Duración objetivo:** ≈ 61 s (careta 2-3 s + rótulo 3 s + 52 s de beats + cierre 3 s)

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** — ¿qué quiere conseguir exactamente el personaje? | |
| **Obstáculo** — ¿qué lo impide de forma visible? | |
| **Concepto** — ¿qué conocimiento desbloquea la solución? | |
| **Error 01** — intuición equivocada | |
| **Error 02** — mejor, pero incompleto | |
| **Pregunta** — ¿qué puede predecir el niño? | |
| **Solución** — aplicación visible del concepto | |
| **Emoción** — ¿qué cambia entre Clic y Plof? | |
| **Transfer** — ¿qué puede hacer fuera de pantalla? | |
| **Callback** — último gag que recompensa volver a verlo | |

## 8 beats (duración fija por beat, decidida el 16/09/2026)

Un clip por beat, nunca dos. El beat 02 puede bajar a 3 s (73 fotogramas) si la ficha lo justifica.

| # | Beat | Segundos | Fotogramas | Acción dominante (una imagen por beat) | Audio / voz |
|---|---|---|---|---|---|
| 01 | Anomalía | 5 | 124 | | |
| 02 | Deseo | 5 | 124 | | |
| 03 | Intento | 8 | 192 | | |
| 04 | Fallo | 8 | 192 | | |
| 05 | Mejora | 5 | 124 | | |
| 06 | Predicción | 5 + 3 de pausa | 124 + `@pausa=3` | | pregunta + pausa real |
| 07 | Solución | 8 | 192 | | |
| 08 | Eco | 5 | 124 | | |

Detrás del beat 08 va siempre el cierre de la serie (`output/v_cierre_final.mp4`, 3 s): no se escribe en la ficha.

## Go / no-go (sección 11)

Rechazar si:
- [ ] el aprendizaje puede quitarse sin afectar a la historia
- [ ] hay más de un problema central
- [ ] la pregunta no se puede responder con lo visto
- [ ] el error existe solo para rellenar tiempo
- [ ] hay estímulo sin función narrativa
- [ ] el final no resuelve lo planteado

Luz verde si:
- [ ] el niño entiende qué quiere el personaje
- [ ] puede anticipar algo antes del final
- [ ] el concepto cambia la acción
- [ ] hay una emoción legible
- [ ] se puede repetir con más dominio
- [ ] existe una pequeña transferencia fuera de pantalla

## Producción

- Focos semánticos en pantalla (máx. 3): 
- Arranque del beat 01 (regla 8, `docs/PERSONAJES.md`): Qwen sobre `assets/personajes_referencia.png` añadiendo este atrezo → `assets/epNN_arranque_beat01.png`; beat 01 con `clip_i2v.json`. Nunca con texto solo. Todos los prompts llevan `BLOQUE_PERSONAJES.txt` y `BLOQUE_PLASTILINA.txt`.
- Objetos que deben mantenerse estables entre clips: 
- Riesgos de generación y plan B: 
