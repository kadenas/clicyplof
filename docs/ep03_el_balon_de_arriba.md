# FICHA DE EPISODIO — EP03 "El balón de arriba"

Fecha: 16/09/2026. Primer episodio con las duraciones nuevas por beat (`docs/DECISION_DURACION_CLIPS.md`) y con la descripción nueva de los personajes (la de la intro y el cierre: Clic alto y delgado, Plof bajito y redondo, cuerpo entero).

## Datos

- **Episodio:** 03
- **Título:** El balón de arriba
- **Dominio del currículo:** posición (arriba / abajo)
- **Motor de historia:** encontrar (recuperar el balón)
- **Duración objetivo:** ≈ 61 s (careta 2-3 s + rótulo 3 s + 52 s de beats + cierre 3 s)
- **Formato:** vertical 768×1344, MiniMax H3 en ComfyUI, semilla 20260916
- **Resuelve:** Clic (Plof salta y no llega)

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** | Recuperar el balón rojo, que se ha quedado en lo alto del árbol de plastilina. |
| **Obstáculo** | Está muy arriba: ninguno de los dos llega. |
| **Concepto** | Arriba / abajo. Para llegar más arriba no sirve saltar más fuerte: hay que subirse a algo. |
| **Error 01** | Plof salta cada vez más fuerte (fuerza bruta). No llega ni de lejos y acaba estampándose contra el tronco. |
| **Error 02** | Clic se estira de puntillas con los brazos arriba: llega mucho más cerca que los saltos de Plof (la altura importa más que la fuerza), pero le faltan unos dedos. |
| **Pregunta** | Clic señala a Plof hecho bola en el suelo, señala el balón, mira a cámara: "¿Cómo puede llegar Clic al balón?" Pausa real de 3 s. |
| **Solución** | Plof, hecho bola, se pega al tronco; Clic se sube encima de Plof, se estira y coge el balón. "¡Arriba!" |
| **Emoción** | Plof pasa de la fuerza bruta al mareo, y luego al orgullo de servir de escalón. Clic pasa de mirar a actuar. Lo resuelve Clic, pero sin Plof no llega. |
| **Transfer** | **Cuidado:** "súbete a algo para llegar a lo alto" no es un mensaje para mandar a casa a un niño de dos años. Lo que se lleva es el vocabulario: *arriba* y *abajo*. Frase para la descripción del vídeo: "¿Qué hay arriba en tu casa? ¿Y abajo?". |
| **Callback** | Recuperado el balón, Plof lo chuta otra vez y vuelve a aterrizar en lo alto del árbol. Se miran; Plof cara de pillo, Clic se da con la mano en la frente. |

## 8 beats (duración fija por beat)

| # | Beat | Segundos | Fotogramas | Acción dominante (una imagen por beat) | Audio / voz |
|---|---|---|---|---|---|
| 01 | Anomalía | 5 | 124 | Entran por la izquierda jugando con el balón rojo. Plof chuta, el balón vuela y aterriza **encima** de la copa del árbol. Frenan al pie del árbol y miran arriba, perplejos. | pasos, risas, "boing", "plop", "¿mmm?" |
| 02 | Deseo | 5 | 124 | Plof señala el balón, da saltitos de impaciencia, se frota las manos y se planta bajo la copa. Clic mide la altura con la mirada. | "¡oh!", risitas |
| 03 | Intento | 8 | 192 | Plof salta a por el balón tres veces, cada vez más fuerte, aplastándose en cada aterrizaje. No se acerca ni de lejos. Patalea. Clic observa. | boings, "splat", esfuerzo |
| 04 | Fallo | 8 | 192 | Carrerilla y salto enorme: Plof se estampa contra el tronco, el árbol tiembla (el balón sigue arriba), Plof resbala, rueda hecho bola y se queda hecho bola junto al tronco, mareado. Clic se ríe y luego mira arriba. | "boing", golpe blando, risa de Clic |
| 05 | Mejora | 5 | 124 | Clic se pone de puntillas bajo el balón y se estira: llega mucho más cerca, pero le falta un palmo. Mira el hueco, mira abajo a Plof-bola: idea. | estiramiento, "mmm", "ping" |
| 06 | Predicción | 5 + 3 | 124 + `@pausa=3` | Clic señala a Plof-bola, señala el balón, mira a cámara. Plof también. **Último fotograma congelado 3 s.** | voz a 1,5 s: "¿Cómo puede llegar Clic al balón?" + silencio |
| 07 | Solución | 8 | 192 | Plof-bola rueda hasta pegarse al tronco. Clic se sube encima con los dos pies, se estira y coge el balón con las dos manos. Lo levanta. Los dos celebran. | "ta-da", voz a 5 s: "¡Arriba!", risas |
| 08 | Eco | 5 | 124 | Clic baja de un salto y deja el balón en el suelo. Plof, feliz, le pega otro chute enorme: el balón vuelve a aterrizar en la copa. Se miran; Plof cara de pillo, Clic mano en la frente. | "plop", "boing", "plop", risita, quejido cómico |

Detrás del beat 08 va el cierre de la serie (`output/v_cierre_final.mp4`).

## Go / no-go

Rechazar si:
- [x] ~~el aprendizaje puede quitarse sin afectar a la historia~~ → sin "subirse a algo" el balón no baja
- [x] ~~hay más de un problema central~~ → uno: el balón está arriba
- [x] ~~la pregunta no se puede responder con lo visto~~ → el niño ha visto que saltar no sirve, que Clic casi llega, y a Plof hecho bola en el suelo
- [x] ~~el error existe solo para rellenar tiempo~~ → error 01 (fuerza) y error 02 (altura) llevan al concepto
- [x] ~~hay estímulo sin función narrativa~~ → el árbol sostiene el balón, la bola de Plof es el escalón
- [x] ~~el final no resuelve lo planteado~~ → el balón baja (y vuelve a subir de gag)

Luz verde si:
- [x] el niño entiende qué quiere el personaje → el balón, señalado desde el beat 02
- [x] puede anticipar algo antes del final → "¡súbete a Plof!" en la pausa
- [x] el concepto cambia la acción → de saltar a subirse
- [x] hay una emoción legible → frustración → idea → orgullo
- [x] se puede repetir con más dominio → la segunda vez el niño grita la solución antes
- [x] existe una pequeña transferencia fuera de pantalla → arriba / abajo

## Producción

- **Focos semánticos (máx. 3):** árbol, balón rojo, personajes.
- **Objetos estables entre clips:** el árbol (tronco marrón, copa verde redonda y maciza, en el tercio derecho del cuadro, unas dos veces la altura de Clic) y el balón rojo (tamaño de una cabeza), que está **encima** de la copa desde el beat 01 hasta el 07. Ningún objeto azul.
- **Riesgos de generación y plan B:**
  - (a) Que el balón se hunda en la copa o desaparezca al aterrizar (beats 01 y 08): pedido explícitamente "encima, visible, como una cereza en un pastel". Si falla, otra semilla; si sigue fallando, que el balón quede **enganchado en una rama** en vez de encima.
  - (b) Que el balón desaparezca en los beats 02-06, donde no hace nada: cada tramo del *timeline* lleva la frase "el balón sigue encima del árbol, visible, sin moverse" (regla 7).
  - (c) Que Clic y Plof se fundan en uno cuando Clic se sube encima (beat 07): pedido "dos figuras separadas, los pies de A encima de B, nunca se funden". Si falla, plan B: Plof a cuatro patas en vez de hecho bola.
  - (d) Que el árbol se mueva o cambie de tamaño al recibir el golpe (beat 04): pedido "tiembla y vuelve a su sitio".
  - (e) La voz llega 1-2 s tarde: pedida a 1,5 s en el beat 06 y a 5 s en el 07.
  - (f) Cinco segundos son pocos para el beat 08 (bajar, chutar, aterrizar, reacción): si el modelo lo atropella, pasar el 08 a 6 s (141 fotogramas).
- **Cadena:** beat 01 con `tropiezo_t2v.json`; del 02 al 08 con `clip_i2v.json` desde el último fotograma del anterior (`ultimo_fotograma.py --limpiar-fondo` → `assets/ep03_arranque_beatNN.png`). El beat 06 se monta con `@pausa=3`.
- **Rótulo:** imagen con Qwen (`prompts/ep03/rotulo.txt`, letras "EL BALÓN / DE ARRIBA" pegadas a la pared) y clip de 3 s con la voz (`prompts/ep03/rotulo_clip.txt`).

## Registro de generación

(se rellena clip a clip: semilla, tiempo, aceptado o repetido y por qué)

- **Beat 01:** semilla 20260916, 11 min 21 s. **Aceptado** a la primera: entran por la izquierda, chute, el balón aterriza encima de la copa y se queda; Plof se rasca la cabeza. El árbol salió grande (la copa mide más que Clic): se ajustaron los prompts del 05 ("sigue claramente por debajo") y del 07 (Clic se estira como plastilina al subirse).
- **Rótulo (Qwen, texto solo):** semilla 20260916 → **rechazado**: "EL BALÓ-N" y "DE ARRIBATA". Se prueban dos vías: A) prompt con recuento exacto de letras (semillas 20260916 y 20260917); B) lienzo con el título escrito con una fuente redondeada (`assets/ep03_rotulo_lienzo.png`) y Qwen convierte las letras en plastilina conservando la ortografía (`prompts/ep03/rotulo_desde_lienzo.txt`).
- **Rótulo, segunda ronda:** A1 (texto endurecido, semilla 20260916) → ✓ "EL / BALÓN / DE / ARRIBA" en cuatro líneas, letras gordas; A2 (20260917) → ✗ "BALÖN"; B (desde lienzo en mayúsculas) → ✓ ortografía, pero letras finas y pared con textura; C (desde lienzo en minúsculas) → ✗ el modelo cambió "de arriba" por "De Arriba". **Elegido A1** (`output/ep03_rotuloA_00001_.png`); su clip de 3 s con la voz, encolado (`clicplof/ep03_rotulo_clip`).
- **Beat 02:** semilla 20260916, 12 min 23 s. **Aceptado**: Plof señala el balón, se frota las manos, se agacha y estira los brazos hacia arriba; Clic observa; balón y árbol quietos. Detalle: el suelo queda con un reflejo azulado tenue donde pisa Plof; se limpió en el fotograma de arranque del 03 (píxeles claros con tinte azul → blanco). Posible mejora para `fondo.py`.
- **Beat 03:** semilla 20260916, 24 min 6 s. **Aceptado**: tres saltos, cada uno más alto (134 → 212 → 234 px medidos), en el tercero toca la parte baja de la copa y aterriza como una tortita; Clic con la mano en la boca. Balón y árbol quietos. Mismo reflejo azulado en el suelo, limpiado en el arranque del 04.
- **Clip del rótulo:** semilla 20260916, 5 min 11 s → `output/ep03_rotulo_clip_00001_.mp4`. **Aceptado** (pendiente de oír la voz): letras intactas, bote a 1,5 s, audio de 0,25 a 2,5 s.
- **Beat 04:** semilla 20260916, 32 min 51 s (lento: recarga de MiniMax tras Qwen). **Aceptado**: carrerilla, estampada contra el tronco a la altura de la copa, resbala, y queda hecho bola junto al tronco, mareado; Clic se ríe y luego mira el balón. Balón y árbol quietos.
- **Beat 05:** semilla 20260916, 15 min 42 s. **Aceptado**: Clic se estira como plastilina hasta doblar su altura, la mano se queda a un palmo del balón, vuelve a su tamaño y mira a Plof-bola (la idea). Balón y árbol quietos.
- **Beat 06:** semilla 20260916, 21 min 38 s. **Aceptado** (voz pendiente de oír): Clic señala a Plof, Plof asoma la cabeza, Clic señala el balón, y desde el segundo 3,4 los dos miran a cámara quietos. Audio: tramo corto a 1,3-2 s y tramo largo de 2,5 a 5 s (la pregunta, probablemente).
- **Beat 07:** semilla 20260916, ≈ 70 min en vez de 25: **el sistema se quedó sin RAM** (un juego abierto, Timberborn, con 7,3 GB, más Steam, Epic y un capturador) y mandó el modelo al archivo de paginación; el proceso de espera murió a los 20 min y hubo que recoger el vídeo después con `--esperar`. **Aceptado**: Plof-bola rueda hasta el tronco, Clic se sube encima sin fundirse con él, se estira, coge el balón y lo levanta; los dos sonríen a cámara. Copa vacía.
- **Beat 08:** semilla 20260916, ≈ 13 min. **Aceptado con reserva**: Clic baja de un salto, deja el balón, Plof lo chuta y vuelve a aterrizar en la copa; Plof cara de pillo, Clic mano en la frente. Punto flojo: entre los fotogramas 14 y 17 Clic se agacha detrás de Plof para soltar el balón y durante un tercio de segundo se ven como un solo bulto. Si molesta, otra semilla (13 min).
- **Careta corta:** `output/v_careta_corta.mp4` (2,2 s), recorte de la intro con `@saltar=139`. Sin GPU.
- **Montaje (17/09/2026, 02:22):** `output/ep03_el_balon_de_arriba.mp4`, **61,3 s** (1472 fotogramas). Orden: careta, rótulo, beats 01-05, beat 06 `@pausa=3`, beat 07 `@saltar=1` (el fotograma de arranque limpiado difería un poco del primero del modelo), beat 08, cierre; con `--limpiar-fondo --marca-agua agua.png`. Ningún clip necesitó `@saltar=8` (salto inicial medido en todos: máximo 6,2 en el 07).
- **Balance:** 8 beats + rótulo + cierre generados **sin repetir ninguno**. GPU: ≈ 2 h 50 min de reloj, de los que ≈ 45 min fueron el beat 07 arrastrándose por falta de RAM (con la máquina libre habrían sido ≈ 2 h 10 min).
- **Personajes desviados, aceptado (01/11/2026):** Clic y Plof no son los de la intro (cabezas pequeñas, Clic como un palo, Plof como un bulto, azul más oscuro), porque el beat 01 arrancó de texto solo. **El usuario decide dejar el episodio así.** A partir del ep02 se aplica la regla 8 (`docs/PERSONAJES.md`).
- **Pendiente de oído (el usuario):** careta ("¡Clic y Plof!"), rótulo ("El balón de arriba"), beat 06 (la pregunta), beat 07 ("¡Arriba!") y cierre ("¡Adiós!").
