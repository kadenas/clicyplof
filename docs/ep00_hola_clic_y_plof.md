# FICHA DE EPISODIO — EP00 "¡Hola, Clic y Plof!" (presentación)

Fecha: 01/11/2026. Pedido por el usuario: un primer capítulo para **conocer a los personajes**, donde se vea a **Clic teniendo una idea** y a **Plof liándola**. Se publica antes del ep01. **Ficha aprobada por el usuario el 01/11/2026** ("me gusta la portería").

## Datos

- **Episodio:** 00 (presentación)
- **Título:** ¡Hola, Clic y Plof!
- **Dominio:** ninguno del currículo a propósito: el aprendizaje es **conocer a los dos y su manera de ser**. Hay un problema pequeño (meter la pelota en la portería) solo para enseñarlos en acción.
- **Resuelve:** Clic (con una idea), después de que Plof la líe
- **Duración objetivo:** ≈ 61 s (careta 2,2 s + rótulo 3 s + 52 s de beats + cierre 3,3 s)

## Lo que tiene que quedar claro al terminar

1. **Clic** es el alto y delgado. **Mira, piensa y tiene ideas.** Cuando tiene una idea, levanta un dedo y suena **"clic"**.
2. **Plof** es el bajito y redondo. **Se lanza sin pensar, con mucha alegría, y la lía.** Cuando se cae, suena **"plof"**.
3. Son amigos y se quieren: Clic no se burla de Plof, se ríe con él; Plof celebra la idea de Clic.
4. El lema de la serie: **"¡Del plof… al clic!"**

## Propuesta: firmas sonoras de la serie

Desde este episodio, en **todos** los episodios:
- **"Clic"**: cuando Clic tiene una idea levanta el dedo índice y suena un "clic" seco, como dos piezas que encajan.
- **"Plof"**: cuando Plof se cae o se aplasta, suena un "plof" blando.

Así los nombres de los personajes son también sonidos que el niño de 2 años reconoce y espera. **Aprobado por el usuario el 01/11/2026**, ya en `TEMPORADA_0.md` § "Reglas de la serie".

## 8 beats

| # | Función | Seg. | Fotogramas | Acción dominante | Audio / voz |
|---|---|---|---|---|---|
| 01 | Presentar a Clic | 5 | 124 | Desde la pose de la intro, Plof se aparta un paso y Clic da un paso adelante y saluda a cámara. Se da unos golpecitos en la cabeza, pensativo, y levanta el dedo índice. | voz: "Este es Clic." + "clic" al levantar el dedo |
| 02 | Presentar a Plof | 5 | 124 | Plof se pone delante de un salto, saluda con los dos brazos, bota de alegría, salta muy alto y cae de culo, aplastándose como una tortita. Se ríe. | voz: "Y este es Plof." + "plof" al caer, risa |
| 03 | Anomalía / Deseo | 5 | 124 | Plof ve la pelota roja en el suelo y, al otro lado, una portería de plastilina (dos postes amarillos). Se le iluminan los ojos, señala la portería y se frota las manos. Clic sonríe. | "¡oh!", risita |
| 04 | Plof la lía (1) | 8 | 192 | Plof coge carrerilla y chuta con todas sus fuerzas: la pelota sale disparada hacia arriba, rebota en la pared y vuelve hacia él, que se agacha justo a tiempo… y le da en el trasero. Plof se cae: plof. La pelota se para lejos de la portería. | "¡bum!", "boing", "plof", risa de Clic |
| 05 | Plof la lía (2) | 8 | 192 | Plof lo intenta otra vez, girando sobre sí mismo como un molinillo para chutar más fuerte: no toca la pelota, se marea, se hace bola y rueda por el suelo hasta quedarse sentado, mareado. La pelota sigue quieta. | giro, "plof", "ooh" mareado; voz: "Plof se lanza…" |
| 06 | La idea de Clic | 5 + 3 | 124 + `@pausa=3` | Clic mira la pelota, mira la portería, se da golpecitos en la cabeza… y levanta el dedo índice: ¡tiene una idea! Mira a cámara. | "clic"; voz: "…y Clic piensa. ¿Qué idea tendrá?" + pausa |
| 07 | Solución | 8 | 192 | Clic coloca la pelota mirando a la portería, apunta con cuidado y le da un toquecito suave con el pie: la pelota rueda despacio, recta, y pasa entre los dos postes. Plof se levanta de un salto y abraza a Clic. Saltan los dos. | rodar, "ping", voz: "¡Gol!", risas |
| 08 | Lema y despedida | 5 | 124 | Los dos, abrazados, miran a cámara. Plof hace como que se cae (sin caerse) y Clic levanta el dedo. Se ríen. | voz: "¡Del plof… al clic!" + "plof" y "clic" suaves, risas |

Detrás va el cierre de la serie (`output/v_cierre_final.mp4`).

## Por qué esta historia

- La **portería** no se repite en la temporada (el ep05 es pasar por un arco **sin** apuntar a nada; aquí es **apuntar**), y es un problema que no necesita explicación.
- Plof la lía **dos veces y de dos formas** (fuerza y torbellino): el niño aprende cómo es antes de ver un episodio "de verdad".
- La idea de Clic no es mágica: **apuntar y empujar suave**. Es la primera lección de la serie: a veces menos fuerza y más mirar.
- La pausa del beat 06 enseña el formato desde el primer día: el niño ya sabe que ahí le toca a él.

## Producción

- **Focos (3):** la pelota, la portería, los personajes.
- **Arranque del beat 01:** Qwen sobre `assets/personajes_referencia.png`, añadiendo una pelota roja en el suelo a un lado y, al otro lado, una portería pequeña de plastilina: dos postes amarillos verticales separados, sin larguero ni red (sin red = nada entra "dentro de" nada).
- **Objetos estables:** una pelota roja y una portería (dos postes) que no se mueve nunca. En los beats 01 y 02 tienen tarea explícita ("se quedan quietos, a la vista").
- **Riesgos y plan B:**
  - (a) **Los beats 01 y 02 tienen que dejar claro quién es quién** con la voz y la silueta. Pedir la voz pronto (0,5 s) porque llega 1-2 s tarde.
  - (b) El sonido "clic" y el "plof": el modelo de audio puede no hacerlos exactos. Si no salen, se añaden en el montaje (necesitaría dos efectos de sonido sueltos; se decidiría entonces).
  - (c) Beat 04: el rebote en la pared puede sacar la pelota de cuadro. "Rebota en la pared del fondo y vuelve, siempre dentro del cuadro".
  - (d) Beat 07: que la pelota no pase "entre" los postes sino que se los lleve. Postes bien separados, el doble de anchos que la pelota.

## Registro de generación

(se rellena clip a clip)
