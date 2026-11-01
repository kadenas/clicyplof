# FICHA DE EPISODIO — EP02 "El morado"

Fecha: 01/11/2026. Primer episodio con los personajes fijados por imagen (`docs/PERSONAJES.md`, regla 8).

## Datos

- **Episodio:** 02
- **Título:** El morado
- **Dominio del currículo:** causa / efecto (rojo + azul = morado). Repite la casilla del ep01 a propósito: **repetir para dominar**.
- **Motor de historia:** construir (llenar el anillo)
- **Duración objetivo:** ≈ 61 s (careta 2,2 s + rótulo 3 s + 52 s de beats + cierre 3,3 s)
- **Formato:** vertical 768×1344, MiniMax H3 en ComfyUI
- **Paga la promesa del ep01**, que termina con Plof cogiendo una ficha roja y otra azul: "¿Y rojo con azul?"

## La idea del episodio

En el ep01 lo resolvieron los dos juntos. Aquí **lo resuelve Plof**, que ya ha visto el truco una vez, pero no a la primera: con la emoción se le olvida y vuelve a la fuerza bruta. La pista se la da **Clic sin querer**, al sostener la roja junto a la azul mientras piensa. Es la mecánica de la serie al revés: esta vez el que lía es Clic (pensando de más) y el que ve la pista es Plof.

El niño que vio el ep01 sabe la respuesta antes que los personajes. **Ese es el premio del episodio**: en el beat 06 grita "¡morado!" antes que nadie.

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** | Llenar el anillo morado vacío que hay en el suelo. |
| **Obstáculo** | Solo hay una ficha roja y una azul; ninguna es morada. |
| **Concepto** | Rojo + azul = morado. |
| **Error 01** | Plof, emocionado, coge la azul y la mete a la fuerza (empuja, se sube, salta): sale disparada y él acaba hecho bola. |
| **Error 02** | Clic prueba la roja con cuidado, la compara con el borde y la apoya: tampoco entra. Se queda pensando con la roja en una mano y la azul en la otra. |
| **Pregunta** | Plof ve a Clic con las dos fichas juntas y se le ilumina la cara. Coge las dos y mira a cámara: "¿Qué pasará si las juntamos?" (la misma pregunta que en el ep01, a propósito). Pausa real de 3 s. |
| **Solución** | Plof aplasta las dos fichas él solo → ficha morada → la encaja en el anillo. "¡Morado!" |
| **Emoción** | Plof pasa del atolondramiento al orgullo de saberlo; Clic, de pensar de más a celebrar el acierto de Plof. |
| **Transfer** | Mezclar plastilina o pintura roja y azul en casa. Descripción del vídeo: "¿Qué pasa si mezcláis rojo y azul?" |
| **Callback** | Clic imita a Plof: se frota las manos con cara de pillo, como hacía Plof en el ep01. Plof le choca la mano. |

## 8 beats

| # | Beat | Seg. | Fotogramas | Acción dominante | Audio / voz |
|---|---|---|---|---|---|
| 01 | Anomalía | 5 | 124 | Arrancan como acaba la intro (Clic apoyado en la cabeza de Plof), se sueltan y se ponen a botar y bailar. Frenan en seco al ver en el suelo un anillo morado vacío y dos fichas, roja y azul. Ladean la cabeza. | jingle suave, "¿mmm?" curioso. Sin palabras |
| 02 | Deseo | 5 | 124 | Plof señala el hueco del anillo, se frota las manos y coge la ficha azul. Clic observa. | risitas |
| 03 | Intento | 8 | 192 | Plof deja caer la azul en el anillo: queda torcida, no entra. Empuja, se sube encima y salta para meterla. Clic se tapa los ojos. | golpes blandos, boings |
| 04 | Fallo | 8 | 192 | La azul sale disparada como un muelle y se para lejos del anillo; Plof cae, rueda hecho bola y se queda sentado, mareado. El anillo sigue vacío. Clic se ríe. | "boing", "plof", risa de Clic |
| 05 | Mejora | 5 | 124 | Clic coge la roja, la compara con el borde morado y la apoya encima: es más ancha que el hueco y no entra. La retira, recoge también la azul y se queda pensando, una ficha en cada mano. | silencio curioso, "mmm" |
| 06 | Predicción | 5 + 3 | 124 + `@pausa=3` | Plof mira las dos fichas en las manos de Clic, abre mucho los ojos, las coge, una en cada mano, y mira a cámara sin juntarlas. **Último fotograma congelado 3 s.** | voz: "¿Qué pasará si las juntamos?" + pausa en silencio |
| 07 | Solución | 8 | 192 | Plof aplasta las dos fichas entre las manos → una sola ficha morada, la amasa al tamaño del hueco y la encaja en el anillo: entra a ras. Clic aplaude y los dos saltan de alegría. | "squish", "ping", voz: "¡Morado!", risas |
| 08 | Eco | 5 | 124 | Clic se frota las manos con cara de pillo, imitando a Plof. Plof se ríe y le choca la mano. El anillo sigue lleno. | palmada, risas |

Detrás del beat 08 va el cierre de la serie (`output/v_cierre_final.mp4`).

## Go / no-go

Rechazar si:
- [x] ~~el aprendizaje puede quitarse sin afectar a la historia~~ → sin rojo + azul = morado no se llena el anillo
- [x] ~~hay más de un problema central~~ → uno: llenar el anillo
- [x] ~~la pregunta no se puede responder con lo visto~~ → ninguna ficha sola vale y el borde es morado; y quien vio el ep01 ya sabe que mezclar funciona
- [x] ~~el error existe solo para rellenar tiempo~~ → la fuerza (01) y la prueba de una sola ficha (02) descartan lo que no sirve
- [x] ~~estímulo sin función narrativa~~ → la bola de Plof es la consecuencia del fallo
- [x] ~~el final no resuelve lo planteado~~ → el anillo queda lleno

Luz verde: deseo claro, anticipación en el beat 06 (más fácil que en el ep01: es la segunda vez), el concepto cambia la acción, emoción legible (atolondrado → orgulloso), replay, transferencia.

## Producción

- **Focos (3):** anillo morado, las dos fichas, los personajes.
- **Arranque del beat 01 (regla 8):** Qwen sobre `assets/personajes_referencia.png` añadiendo el anillo y las dos fichas en el suelo → `assets/ep02_arranque_beat01.png`; beat 01 con `clip_i2v.json`. Todos los prompts llevan `BLOQUE_PERSONAJES.txt` y `BLOQUE_PLASTILINA.txt`.
- **Objetos estables entre clips:** el anillo morado (plano, en el suelo, a un lado) y las dos fichas hasta el beat 07; desde el 07, el anillo lleno con la ficha morada.
- **Riesgos de generación y plan B:**
  - (a) **La ficha azul se confunde con los muñecos** (pasó en el ep01). Ver decisión pendiente 1.
  - (b) **Sitio en el suelo:** en la referencia los muñecos ocupan la parte de abajo y casi no queda suelo libre. Puede que Qwen tenga que abrir un poco el plano (muñecos algo más pequeños). Se acepta si conservan la forma y el color; se comprueba con la referencia.
  - (c) La ficha morada se estira como un chicle o aparecen dos (fallo del beat 05 del ep01): deformación elástica del bloque de plastilina; la ficha **se apoya encima** del anillo y **la retira un personaje** (reglas 1 y 3).
  - (d) La azul que sale disparada en el beat 04 se pierde de cuadro: pedir que "rueda y se para en el suelo, a la vista, lejos del anillo".
  - (e) La voz llega 1-2 s tarde: pedirla a 1,5 s en el beat 06 y a 5 s en el 07.
  - (f) Deriva del azul de los muñecos en la cadena: comparar cada fotograma de arranque con la referencia.

## Decisiones tomadas (01/11/2026)

1. **La ficha azul es azul marino oscuro**, muy distinta del azul vivo de los muñecos. Descartados el celeste (morado demasiado rosado) y el mismo azul con otra forma (se sigue confundiendo en la mano).
2. **El beat 01 arranca en la postura del final de la intro** (Clic apoyado en la cabeza de Plof) y se sueltan a jugar desde ahí. Ya no "entran" desde fuera del cuadro, porque el modelo se inventaría a los personajes. Regla actualizada en `TEMPORADA_0.md`.

## Registro de generación

(se rellena clip a clip: semilla, tiempo, aceptado o repetido y por qué)

- **Arranque del beat 01 (Qwen, `prompts/ep02/arranque_beat01.txt`, sobre `assets/personajes_referencia.png`):**
  - v1, semilla 20260916 → ✗ pared con rayas grises; anillo enorme con agujero pequeño, pegado al borde.
  - v2 (prompt con pared lisa, agujero grande y objetos dentro del cuadro), semillas 20260916 y 20260917 → 20260916 ✗ pared muy rayada; 20260917 casi buena, pero las fichas me salieron del tamaño del agujero (error mío en el prompt: las pedí *más pequeñas*).
  - **v3, semilla 20260917 → ✓** fichas más anchas que el agujero, pared limpia, ficha marino bien distinta de los muñecos, personajes idénticos a la referencia (Qwen abrió un poco el plano, como se preveía). → `assets/ep02_arranque_beat01.png`.
  - Aprendido: Qwen tiende a rayar la pared al editar; pedir explícitamente "pared lisa, sin textura ni marcas".
- **Beat 01:** `clip_i2v.json` desde `assets/ep02_arranque_beat01.png`, 124 fotogramas, semilla 20260916, **3 min 40 s**. Cumple el guion (se sueltan, bailan, frenan, se miran, Plof se rasca la cabeza); objetos estables. **Personajes mucho más cerca de la intro que en el ep03**: cabezas grandes, Plof de dos bolas, azul estable (medido 25,128,202 → 24,126,198). Defectos: el tronco de Clic adelgaza al estirarse; la cara final se lee como pena más que como duda. **Aceptado por el usuario** ("se ve bien").
- **Primera pasada (01/11/2026) DESCARTADA por resolución:** los 8 beats se generaron a **480×864** porque `clip_i2v.json` trae ese tamaño por defecto y no se pasó `--tamano 768x1344` (por eso tardaban 3-6 min). Guardados como `output/ep02_beatNN_480p.mp4`. Lo que enseñaron: beats 01, 02, 04-07 buenos; **beat 03** la ficha marino se colaba plana en el agujero; **beat 08** Clic se encogía y parecía otro Plof; y **el azul se oscurecía al encadenar** (B de 202 a 163).
- **Correcciones para la segunda pasada:** `--tamano 768x1344` en todos los clips; `ultimo_fotograma.py --corregir-azul` en cada enlace (nueva, `fondo.corregir_azul`); prompt del beat 03 reforzado (la ficha cae torcida sobre el borde, nunca plana dentro); prompt del beat 08 reforzado (no intercambian formas).
- **Segunda pasada (01/11/2026), 768×1344, semilla 20260916, con `--corregir-azul` en cada enlace:** beats 01 (12 min) a 08 generados **sin repetir ninguno**, todos aceptados. Azul estable en todo el episodio (B entre 196 y 208; referencia 202). Beat 03: la ficha marino cae torcida sobre el borde (corregido). Beat 08: Clic sigue alto y delgado (corregido). Tiempos: 5 s ≈ 12 min, 8 s ≈ 23-24 min.
- **Rótulo:** Qwen "EL MORADO" (`prompts/ep02/rotulo.txt`, semilla 20260916) bueno a la primera → `assets/ep02_rotulo.png`; clip de 3 s (`prompts/ep02/rotulo_clip.txt`, 5 min 38 s) bueno: letras intactas, bote, audio presente.
- **Montaje (01/11/2026):** `output/ep02_el_morado.mp4`, **61,4 s**, 768×1344. Orden: careta corta, rótulo, beats 01-05, beat 06 `@pausa=3`, beats 07-08, cierre; con `--limpiar-fondo --marca-agua agua.png`. **Pendiente de que el usuario lo vea y oiga** (voces: "El morado", "¿Qué pasará si las juntamos?", "¡Morado!").
