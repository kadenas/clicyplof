# FICHA DE EPISODIO — EP09 "Una para cada uno"

Fecha: 01/11/2026. Tanda 2 (ep08-11). Personajes fijados por imagen (`docs/PERSONAJES.md`, regla 8).

## Datos

- **Episodio:** 09
- **Título:** Una para cada uno
- **Dominio del currículo:** cantidad (repartir igual: una para ti, una para mí; la que sobra, por la mitad)
- **Motor de historia:** compartir
- **Resuelve:** Clic
- **Duración objetivo:** ≈ 61 s

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** | Comerse las galletas de plastilina. |
| **Obstáculo** | Hay cinco galletas y son dos. Los dos las quieren. |
| **Concepto** | Repartir igual: una para ti, una para mí, hasta que no queden. Si sobra una, se parte por la mitad. |
| **Error 01** | Plof se lanza y abraza todas las que puede: se lleva cuatro y a Clic le deja una. Clic se queda triste. |
| **Error 02** | Con tantas en brazos, a Plof se le caen y ruedan por el suelo. Clic las coloca en fila y empieza a repartir: una para Plof, una para él, otra para Plof, otra para él… y sobra una. Los dos alargan la mano hacia la misma. |
| **Pregunta** | Clic coge la galleta que sobra, la levanta y mira a cámara: "¿Y esta, para quién?" Pausa de 3 s. |
| **Solución** | Clic parte la galleta en dos mitades iguales y le da una a Plof. Cada uno tiene dos galletas y media. "¡Mitad para cada uno!" |
| **Emoción** | Plof pasa de la glotonería a la alegría de compartir; Clic, de la tristeza a la justicia. |
| **Transfer** | En la merienda: repartir "una para ti, una para mí". |
| **Callback** | Los dos chocan sus medias galletas como si brindaran. |

## La pista (mecánica de la serie)

Plof la lía (lo acapara todo y se le cae). **Al caer, las galletas quedan sueltas por el suelo y se pueden contar y repartir una a una**: eso es lo que hace Clic.

## 8 beats

| # | Beat | Seg. | Fotogramas | Acción dominante | Audio / voz |
|---|---|---|---|---|---|
| 01 | Anomalía | 5 | 124 | Se sueltan de la pose de la intro, bailan y frenan en seco: en el suelo, una fila de cinco galletas redondas de plastilina marrón clara con puntitos de colores. | jingle, "¡oh!" |
| 02 | Deseo | 5 | 124 | Los dos se frotan la barriga, se relamen y miran las galletas con hambre. | "ñam", "mmm" glotón |
| 03 | Intento | 8 | 192 | Plof se lanza y recoge en brazos todas las que puede: cuatro galletas apretadas contra la barriga. Queda una en el suelo. Clic la coge y mira a Plof, triste. | risita glotona, suspiro de Clic |
| 04 | Fallo | 8 | 192 | Plof echa a andar con su montón: las galletas se le escurren de los brazos una a una y ruedan por el suelo. Plof intenta atraparlas, tropieza y cae de bruces, aplastándose. Las cinco galletas quedan sueltas por el suelo. | "plof", rodar, "¡ay!" |
| 05 | Mejora | 5 | 124 | Clic coloca las cinco galletas en fila y reparte: una delante de Plof, una delante de él, otra delante de Plof, otra delante de él. Sobra una en el medio. Los dos alargan la mano hacia ella. | voz: "Una para ti, una para mí…" |
| 06 | Predicción | 5 + 3 | 124 + `@pausa=3` | Clic coge la galleta que sobra, la levanta y mira a cámara. Plof también mira a cámara. Quietos. | voz: "¿Y esta, para quién?" + pausa |
| 07 | Solución | 8 | 192 | Clic parte la galleta en dos mitades iguales y le da una a Plof. Cada uno junta su montón: dos galletas y media cada uno. Se abrazan. | "crac" blandito, "ping", voz: "¡Mitad para cada uno!", risas |
| 08 | Eco | 5 | 124 | Los dos levantan su media galleta y las chocan como si brindaran. Se ríen. | "chin", risas |

## Go / no-go

- [x] ~~el aprendizaje puede quitarse~~ → sin repartir de una en una no saben que sobra una
- [x] ~~más de un problema central~~ → uno: repartir
- [x] ~~la pregunta no se puede responder~~ → han visto sobrar una
- [x] ~~error de relleno~~ → acaparar sale mal; repartir de una en una funciona pero deja el problema de la que sobra
- [x] ~~estímulo sin función~~ → la caída esparce las galletas
- [x] ~~final sin resolver~~ → los dos tienen lo mismo

Luz verde: conflicto universal (la merienda); la tristeza de Clic en el beat 03 es la emoción que el niño reconoce.

## Producción

- **Focos (2):** las galletas y los personajes.
- **Arranque del beat 01:** Qwen sobre la referencia, añadiendo una fila de cinco galletas redondas, planas, marrón claro con puntitos de colores, separadas, en el suelo delante de ellos.
- **Objetos estables:** **exactamente cinco galletas** hasta el beat 07; desde el 07, cuatro galletas enteras y dos mitades.
- **Riesgos y plan B:**
  - (a) **Contar cinco** es el máximo que admite la escaleta. Enumerarlas en todos los prompts.
  - (b) **Partir la galleta choca con el bloque de plastilina** ("nunca se rompe en trozos"). En el beat 07 se añade una excepción explícita: "esta galleta, y solo esta, se parte en exactamente dos mitades iguales". Si el modelo la parte mal o en más trozos, otra semilla; si sigue fallando, plan B: **la estiran entre los dos hasta que se parte** (tirando cada uno de un lado), que es más natural para la plastilina.
  - (c) Que comerse las galletas desaparezca objetos: **nadie se come nada en el episodio**; el brindis del beat 08 las conserva.
  - (d) Cuatro galletas en brazos de Plof (beat 03): que no se fundan con su barriga. Son marrón claro, nada que ver con el azul.

## Registro de generación

(se rellena clip a clip)
