# FICHA DE EPISODIO — EP10 "Un solo viaje"

Fecha: 01/11/2026. Tanda 2 (ep08-11). Personajes fijados por imagen (`docs/PERSONAJES.md`, regla 8).

## Datos

- **Episodio:** 10
- **Título:** Un solo viaje
- **Dominio del currículo:** cantidad (muchos en uno: juntar para llevar de una vez)
- **Motor de historia:** transportar
- **Resuelve:** Clic (Plof está agotado)
- **Duración objetivo:** ≈ 61 s

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** | Llevar las cuatro bolas hasta la marca verde del otro lado. |
| **Obstáculo** | De una en una, el viaje es largo y no acaban nunca. |
| **Concepto** | Muchos en uno: si las metes todas en el plato, las llevas en un solo viaje. |
| **Error 01** | Plof las lleva corriendo de una en una: primera, segunda… cada viaje más lento. |
| **Error 02** | Clic intenta llevar las dos que quedan a la vez, abrazadas contra el cuerpo: se le escurren y ruedan de vuelta. |
| **Pregunta** | Clic ve el plato hondo que hay junto a las bolas, lo señala y mira a cámara: "¿Cómo las llevamos todas de una vez?" Pausa de 3 s. |
| **Solución** | Clic mete las dos bolas en el plato y lo lleva hasta la marca verde en un solo viaje. "¡Todas a la vez!" |
| **Emoción** | Plof pasa del entusiasmo al agotamiento cómico; Clic, de la torpeza a la idea. |
| **Transfer** | En casa: recoger los juguetes en una caja en lugar de uno a uno. |
| **Callback** | Plof, agotado, se mete él también en el plato hondo… no cabe: queda sentado encima, desbordando. Clic intenta arrastrarlo y no puede. Se ríen. |

## La pista (mecánica de la serie)

El plato hondo está **junto a las bolas desde el primer fotograma**, sin que nadie le haga caso. Cuando a Clic se le escurren las bolas en el beat 05, **una cae dentro del plato y se queda quieta**: esa es la pista que ve Clic.

## 8 beats

| # | Beat | Seg. | Fotogramas | Acción dominante | Audio / voz |
|---|---|---|---|---|---|
| 01 | Anomalía | 5 | 124 | Se sueltan de la pose de la intro, bailan y frenan en seco: a la izquierda, cuatro bolas (roja, amarilla, verde, rosa) y un plato hondo y bajito, morado, vacío; a la derecha, lejos, una marca plana verde en el suelo. | jingle, "¿mmm?" |
| 02 | Deseo | 5 | 124 | Clic señala las bolas y luego la marca verde del otro lado: hay que llevarlas allí. Plof saluda como un soldado, ansioso por empezar. | "¡oh!", risita |
| 03 | Intento | 8 | 192 | Plof coge la roja, corre hasta la marca verde, la deja y vuelve corriendo. Coge la amarilla, corre, la deja, vuelve, ya más despacio, resoplando. | pasos rápidos, resoplidos |
| 04 | Fallo | 8 | 192 | Tercer viaje con la verde: a mitad de camino Plof va arrastrando los pies, con la lengua fuera; se le cae la verde, que rueda de vuelta al principio, y Plof se desploma como una tortita, jadeando. | pasos lentos, "plof", jadeo |
| 05 | Mejora | 5 | 124 | Clic intenta llevar la verde y la rosa a la vez, abrazadas contra el cuerpo: se le escurren, la rosa rueda por el suelo y la verde cae dentro del plato hondo y se queda quieta. Clic mira el plato. | rodar, "toc", "¡oh!" |
| 06 | Predicción | 5 + 3 | 124 + `@pausa=3` | Clic señala el plato hondo y mira a cámara. Plof, tumbado, levanta la cabeza y también mira a cámara. Quietos. | voz: "¿Cómo las llevamos todas de una vez?" + pausa |
| 07 | Solución | 8 | 192 | Clic mete la rosa en el plato (con la verde), lo coge con las dos manos, lo lleva hasta la marca verde y lo deja allí, junto a la roja y la amarilla. Plof se levanta y aplaude. Saltan de alegría. | pasos, "ping", voz: "¡Todas a la vez!", risas |
| 08 | Eco | 5 | 124 | Plof, agotado, intenta meterse en el plato hondo: es demasiado grande y se queda sentado encima, desbordando. Clic tira del plato para arrastrarlo y no puede. Se ríen. | "chof", esfuerzo, risas |

## Go / no-go

- [x] ~~el aprendizaje puede quitarse~~ → sin el plato no acaban
- [x] ~~más de un problema central~~ → uno: llevarlas todas
- [x] ~~la pregunta no se puede responder~~ → el plato se ve desde el principio y una bola ha caído dentro
- [x] ~~error de relleno~~ → de una en una agota; abrazadas se caen
- [x] ~~estímulo sin función~~ → el desplome de Plof es el coste de ir de una en una
- [x] ~~final sin resolver~~ → las cuatro en la marca

Luz verde: el agotamiento creciente de Plof es comedia que entiende un niño de 2 años.

## Producción

- **Focos (3, en el límite):** las bolas con su plato (van juntos), la marca verde y los personajes.
- **Arranque del beat 01:** Qwen sobre la referencia. Abrir el plano en horizontal todo lo posible: las bolas y el plato junto a los personajes, a la izquierda; la marca verde a la derecha, lejos.
- **Objetos estables:** **exactamente cuatro bolas** (roja, amarilla, verde, rosa), un plato y una marca.
- **Riesgos y plan B:**
  - (a) **El plato hondo es "meter dentro de"** (regla 1). Se pide un plato **bajito y ancho**, donde las bolas quedan a la vista por encima del borde. Si las pierde, plan B: una bandeja plana con reborde.
  - (b) Los viajes de Plof cruzan el cuadro varias veces: que no salga del cuadro. "Los viajes van de un lado al otro del suelo, siempre dentro del cuadro".
  - (c) Contar cuatro bolas en movimiento: enumerar dónde está cada una en cada tramo.
  - (d) Beat 08: que Plof "entre" en el plato. Pedir que se queda **encima**, desbordando, porque no cabe.

## Registro de generación

(se rellena clip a clip)
