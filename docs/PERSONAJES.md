# PERSONAJES — Clic y Plof

**Fecha:** 01/11/2026
**Fuente de verdad:** la imagen `assets/personajes_referencia.png`, no este texto. Si el texto y la imagen no coinciden, manda la imagen.

## De dónde salen

Los personajes buenos son los de la **intro y el cierre** (`output/v_intro_cp2_00001_.mp4`, `output/v_cierre_final.mp4`). La referencia es el rótulo de la intro (`output/v_rotulo_cp2_00001_.png`) con las letras quitadas por Qwen Image Edit (`prompts/serie/personajes_referencia.txt`, semilla 20260916, 30 s). Comprobado: en la zona de los muñecos la imagen se diferencia del rótulo en 2,3 sobre 255 de media; son los mismos.

## Referencias de pose (añadidas el 01/11/2026 por el usuario)

- `assets/ref_plof_celebrando.png` — **Plof** saltando de alegría: dos bolas (cabeza y barriga), brazos cortos, piernas cortas y gruesas con pies de deditos.
- `assets/ref_clic_celebrando.png` — **Clic** saltando de alegría: cabeza grande, tronco de salchicha, brazos y piernas largos.

Confirman la forma de los personajes de la intro y añaden dos detalles: **al celebrar, abren mucho la boca y se ve una lengua rosa**, y **las manos tienen cinco dedos redondeados**. Son renders "de juguete" con un fondo de cuadros pintado (no es transparencia real): sirven para mirar, no como entrada directa de Qwen (habría que quitar el fondo antes). La imagen de producción sigue siendo `assets/personajes_referencia.png`.

## Por qué existe este documento

Al ver el ep03 (17/09/2026) se vio que los personajes no eran los de la intro: cabezas pequeñas, Clic como un palo de alambre, Plof como un bulto, azul más oscuro y bocas abiertas grandes. Causa: el beat 01 se generó **solo con texto** (`tropiezo_t2v.json`) y el modelo se inventó a los personajes a partir de la descripción; los beats siguientes heredaron esa versión y el azul se oscureció un poco más en cada enlace. La intro y el cierre, en cambio, arrancan de una imagen, y el modelo copia lo que ve.

**Conclusión: la descripción en texto no basta. Los personajes se fijan con una imagen.** El ep03 se queda como está (decisión del 01/11/2026).

## Rasgos comunes

- Plastilina **azul vivo y medio**, mate, con huellas y marcas de dedos. Medido en la referencia: ≈ RGB (17, 129, 211) en la parte iluminada y ≈ (7, 114, 184) en la sombra. **No** azul marino, **no** azul oscuro, **no** brillante.
- **Los dos del mismo azul.** Se distinguen solo por la silueta.
- **Cabeza grande y redonda**, una bola casi perfecta, separada del cuerpo por un cuello apenas marcado.
- **Cara mínima:** dos ojos pequeños de punto negro y una sonrisa fina, curva, de línea negra. Sin nariz, sin orejas, sin pelo, sin cejas, sin ropa.
- En reposo, **boca cerrada en sonrisa fina**. La boca abierta se reserva para momentos de risa o sorpresa, y vuelve a la sonrisa fina.
- Manos redondeadas con dedos cortos; pies pequeños y redondeados, apoyados planos en el suelo.

## Clic (A) — el alto y delgado

| Rasgo | Cómo es |
|---|---|
| Altura | El más alto. Es la referencia: Plof mide unos 2/3 de él |
| Cabeza | Bola grande, ≈ 1/3 de su altura total, **más ancha que su tronco** |
| Tronco | Alargado, como una salchicha estirada, más estrecho que la cabeza |
| Brazos | Largos y finos, le llegan a media pierna |
| Piernas | Largas, rectas y finas, casi la mitad de su altura |
| No es | Un palo o un muñeco de alambre con cabeza pequeña |

## Plof (B) — el bajito y redondo

| Rasgo | Cómo es |
|---|---|
| Altura | ≈ 2/3 de la de Clic (**no** la mitad) |
| Forma | **Dos bolas apiladas** de tamaño parecido: la cabeza encima de una barriga redonda |
| Cabeza | Bola grande, del ancho de la barriga |
| Brazos | Cortos y gorditos, pegados a los lados de la barriga |
| Piernas | Muy cortas y gruesas, con pies pequeños de deditos marcados |
| No es | Un bulto o una masa sin forma; tampoco una bola sola sin cabeza |

## Cómo se usa en producción

1. **Bloque de texto fijo** `prompts/serie/BLOQUE_PERSONAJES.txt`: se copia tal cual en todos los prompts de vídeo, junto al `BLOQUE_PLASTILINA.txt`. Sustituye a cualquier otra descripción de los personajes.
2. **El beat 01 de cada episodio NUNCA arranca de texto solo** (regla 8 de `docs/ep01_los_colores.md` § "Aprendido al generar"):
   - Qwen Image Edit (`workflow/titulo_qwen.json`) parte de `assets/personajes_referencia.png` y **añade el atrezo del episodio** (árbol, balón…) sin tocar a los personajes → `assets/epNN_arranque_beat01.png`.
   - Se comparan los personajes de esa imagen con la referencia antes de seguir.
   - El beat 01 se genera con `clip_i2v.json` desde esa imagen, como los demás beats.
3. **En la cadena de beats:** al sacar cada fotograma de arranque, se pone al lado de la referencia. Si el azul se ha oscurecido o la silueta se ha desviado, se corrige el fotograma de arranque antes de generar el beat siguiente.

## Pendiente de comprobar en el ep02 (primer episodio con este método)

- Que Qwen añada el atrezo sin retocar a los personajes. Si los toca, probar a añadir un objeto cada vez.
- La postura: la referencia los tiene abrazados (Clic apoyado en la cabeza de Plof). Si el beat 01 necesita otra postura, se le puede pedir a Qwen que los separe, pero es otro cambio en la imagen que hay que revisar. Alternativa: que el propio beat 01 empiece con ellos separándose.
- Cómo corregir la deriva del azul en los fotogramas de enlace (ya era un problema conocido; ahora hay un color medido con el que comparar).
