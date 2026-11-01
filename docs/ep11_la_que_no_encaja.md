# FICHA DE EPISODIO — EP11 "La que no encaja"

Fecha: 01/11/2026. Tanda 2 (ep08-11). Personajes fijados por imagen (`docs/PERSONAJES.md`, regla 8).

## Datos

- **Episodio:** 11
- **Título:** La que no encaja
- **Dominio del currículo:** forma (reconocer por la forma, no por el color)
- **Motor de historia:** encontrar
- **Resuelve:** Clic
- **Duración objetivo:** ≈ 61 s

## Cambio sobre la escaleta

La escaleta dice "entre muchas piezas iguales hay una distinta escondida". Se concreta así: **un cubo rojo está solo y busca pareja; la pareja es el único cubo entre un grupo de bolas, todas naranjas**. Como todas las naranjas son del mismo color, buscar por el color no sirve: hay que mirar la forma. "Escondida" se cumple porque está mezclada entre piezas del mismo color, **no tapada** (lo que se tapa, el modelo lo borra). Cinco piezas en total, que es el máximo de la escaleta.

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** | Encontrarle pareja al cubo rojo, que está solo. |
| **Obstáculo** | Las piezas del grupo son todas naranjas: tres bolas y un cubo. Por el color no se distinguen. |
| **Concepto** | La pareja es la que tiene la misma forma, aunque sea de otro color. |
| **Error 01** | Plof coge una bola naranja y la pone junto al cubo rojo: la bola rueda y se va. Prueba con otra: igual. |
| **Error 02** | Plof se sienta encima de una bola para que no se escape: la bola rueda debajo de él y Plof se cae. |
| **Pregunta** | Clic, con el cubo rojo en la mano, señala el grupo de piezas naranjas y mira a cámara: "¿Cuál es igual?" Pausa de 3 s. |
| **Solución** | Clic coge el cubo naranja y lo pone junto al rojo: los dos se quedan quietos, plantados, iguales de forma. "¡Igual de forma!" |
| **Emoción** | Plof pasa de la prisa a la sorpresa; Clic, de la duda a la satisfacción. |
| **Transfer** | En casa: buscar cosas con la misma forma (redondas, cuadradas) aunque sean de distinto color. |
| **Callback** | Plof coge una bola naranja y se la pone junto a su cabeza redonda, mirando a cámara: los dos redondos. Clic se ríe. |

## La pista (mecánica de la serie)

Cuando Plof se cae en el beat 04, **choca con el grupo de piezas naranjas: las bolas ruedan y el cubo naranja se queda quieto**, igual que el rojo. Clic lo ve.

## 8 beats

| # | Beat | Seg. | Fotogramas | Acción dominante | Audio / voz |
|---|---|---|---|---|---|
| 01 | Anomalía | 5 | 124 | Se sueltan de la pose de la intro, bailan y frenan en seco: a un lado, solo, un cubo rojo; al otro, un grupo de cuatro piezas naranjas juntas: tres bolas y un cubo. | jingle, "¿mmm?" |
| 02 | Deseo | 5 | 124 | Plof abraza el cubo rojo con cara de pena: está solito. Señala el grupo de piezas naranjas: hay que buscarle un amigo. Clic asiente. | "ooh" tierno, "¡sí!" |
| 03 | Intento | 8 | 192 | Plof coge una bola naranja y la pone junto al cubo rojo: la bola rueda y se aleja. Coge otra bola y la pone: también rueda. Plof se rasca la cabeza. | "toc", rodar, "¿eh?" |
| 04 | Fallo | 8 | 192 | Plof se sienta encima de una bola naranja para que no se escape: la bola rueda debajo de él, Plof cae de espaldas y choca con el grupo. Las bolas ruedan un poco; **el cubo naranja se queda quieto**. Clic lo mira. | rodar, "plof", "¡ay!" |
| 05 | Mejora | 5 | 124 | Clic coge el cubo rojo y pasa el dedo por sus caras planas y sus esquinas. Luego mira las piezas naranjas una a una. | "mmm" pensativo |
| 06 | Predicción | 5 + 3 | 124 + `@pausa=3` | Clic, con el cubo rojo en la mano, señala las piezas naranjas y mira a cámara. Plof también mira a cámara. Quietos. | voz: "¿Cuál es igual?" + pausa |
| 07 | Solución | 8 | 192 | Clic coge el cubo naranja y lo pone junto al rojo: los dos cubos quedan quietos, uno al lado del otro. Plof los abraza a los dos. Saltan de alegría. | "toc", "ping", voz: "¡Igual de forma!", risas |
| 08 | Eco | 5 | 124 | Plof coge una bola naranja y la pone junto a su cabeza redonda, mirando a cámara con una gran sonrisa. Clic se ríe. | risita, risas |

## Go / no-go

- [x] ~~el aprendizaje puede quitarse~~ → sin mirar la forma no encuentran la pareja
- [x] ~~más de un problema central~~ → uno: la pareja
- [x] ~~la pregunta no se puede responder~~ → el niño ha visto qué pieza no rueda
- [x] ~~error de relleno~~ → las bolas ruedan, y esa es justo la diferencia
- [x] ~~estímulo sin función~~ → la caída de Plof separa las bolas del cubo
- [x] ~~final sin resolver~~ → el cubo rojo tiene pareja

Luz verde: "rueda / no rueda" es una diferencia de forma que se ve sin palabras.

## Producción

- **Focos (3):** el cubo rojo, el grupo naranja, los personajes.
- **Arranque del beat 01:** Qwen sobre la referencia: cubo rojo solo a la izquierda; a la derecha, cuatro piezas naranjas juntas pero sin taparse (tres bolas y un cubo del mismo tamaño que el rojo).
- **Objetos estables:** exactamente un cubo rojo, un cubo naranja y tres bolas naranjas.
- **Riesgos y plan B:**
  - (a) Que el modelo pinte el cubo naranja de otro color o lo convierta en bola: repetir en cada tramo "un cubo naranja, con caras planas y esquinas".
  - (b) Que las bolas rueden fuera del cuadro: "ruedan un poco y se paran, dentro del cuadro".
  - (c) Beat 08: que la bola se funda con la cabeza de Plof. Es naranja; pedir "la sostiene junto a la cabeza, sin tocarla".

## Registro de generación

(se rellena clip a clip)
