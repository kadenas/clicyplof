# FICHA DE EPISODIO — EP04 "La torre que se cae"

Fecha: 01/11/2026. Tanda 1 (ep04-07). Personajes fijados por imagen (`docs/PERSONAJES.md`, regla 8).

## Datos

- **Episodio:** 04
- **Título:** La torre que se cae
- **Dominio del currículo:** posición (lo grande debajo, lo pequeño encima)
- **Motor de historia:** construir
- **Resuelve:** Clic
- **Duración objetivo:** ≈ 61 s (careta 2,2 s + rótulo 3 s + 52 s de beats + cierre 3,3 s)

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** | Plof quiere hacer una torre tan alta como Clic. |
| **Obstáculo** | Con las piezas al revés, la torre se tambalea y se cae. |
| **Concepto** | Lo grande va debajo y lo pequeño encima. |
| **Error 01** | Plof apila deprisa: el cubo pequeño abajo y el grande arriba. La torre se cae. |
| **Error 02** | Plof lo intenta otra vez con el grande abajo, pero luego el pequeño en medio y el mediano arriba: se tuerce y el de arriba resbala. Mejor, pero no queda. |
| **Pregunta** | Clic pone los tres cubos en fila en el suelo, del más grande al más pequeño, señala la fila y mira a cámara: "¿Cuál va abajo?" Pausa de 3 s. |
| **Solución** | Clic apila grande, mediano y pequeño. La torre se queda quieta. "¡El grande, abajo!" |
| **Emoción** | Plof pasa de la frustración a la sorpresa; Clic, de mirar a ordenar. |
| **Transfer** | Apilar en casa tres cosas de distinto tamaño (cajas, vasos, cojines). |
| **Callback** | Plof da una palmadita a la torre: se balancea… y se queda. Los dos sueltan el aire aliviados. |

## La pista (mecánica de la serie)

Cuando la torre se cae en el beat 04, **el cubo grande aterriza y se queda quieto, plantado, mientras el pequeño sigue rodando**. Clic lo ve. Es lo que le da la idea.

## 8 beats

| # | Beat | Seg. | Fotogramas | Acción dominante | Audio / voz |
|---|---|---|---|---|---|
| 01 | Anomalía | 5 | 124 | Se sueltan de la pose de la intro, bailan y frenan en seco: en el suelo hay tres cubos de plastilina, uno grande rojo, uno mediano amarillo y uno pequeño verde. | jingle, "¿mmm?" |
| 02 | Deseo | 5 | 124 | Plof mira a Clic de abajo arriba, se pone de puntillas para medirle con la mano, señala los cubos y luego hacia arriba: quiere una torre así de alta. Se frota las manos. | risitas, "¡oh!" |
| 03 | Intento | 8 | 192 | Plof apila deprisa: el verde pequeño abajo, encima el amarillo y arriba del todo el rojo grande. La torre se tambalea. Plof la sujeta con los brazos estirados. Clic se tapa los ojos. | golpes blandos, crujidos de plastilina |
| 04 | Fallo | 8 | 192 | La torre se cae hacia Plof. El cubo rojo le aplasta como una tortita y él vuelve a su forma. Los cubos se quedan en el suelo: **el rojo plantado y quieto, el verde rodando un poco más**. Clic mira el rojo y luego el verde. | "plof", "boing", rodar |
| 05 | Mejora | 5 | 124 | Plof vuelve a apilar con el rojo abajo, pero pone el verde en medio y el amarillo arriba. El amarillo se ladea y resbala al suelo, sin romperse. Plof se cruza de brazos. Clic se rasca la barbilla. | resbalón blando, "mmm" |
| 06 | Predicción | 5 + 3 | 124 + `@pausa=3` | Clic pone los tres cubos en fila en el suelo, de grande a pequeño, los señala y mira a cámara. Plof también mira a cámara. Quietos. | voz: "¿Cuál va abajo?" + pausa |
| 07 | Solución | 8 | 192 | Clic apila el rojo, luego el amarillo encima y luego el verde arriba. La torre se queda recta y quieta. Plof la mide: le llega casi a la barbilla de Clic. Saltan de alegría. | "toc, toc, toc", "ping", voz: "¡El grande, abajo!", risas |
| 08 | Eco | 5 | 124 | Plof le da una palmadita a la torre: se balancea, se balancea… y se queda. Los dos sueltan el aire aliviados y se ríen. | palmada, "uuuh", suspiro, risas |

## Go / no-go

- [x] ~~el aprendizaje puede quitarse~~ → sin "grande abajo" la torre no se sostiene
- [x] ~~más de un problema central~~ → uno: que la torre aguante
- [x] ~~la pregunta no se puede responder~~ → el niño ha visto al rojo quedarse plantado y al verde rodar
- [x] ~~error de relleno~~ → el error 01 tiene todo al revés; el error 02 solo acierta con el de abajo
- [x] ~~estímulo sin función~~ → el aplastón de Plof es la consecuencia del fallo
- [x] ~~final sin resolver~~ → la torre se sostiene

Luz verde: deseo claro (alta como Clic), anticipación (ordenar de mayor a menor), emoción legible, transferencia inmediata.

## Producción

- **Focos (3):** los tres cubos (uno solo, porque son el mismo "objeto torre"), los personajes. Nada más en escena.
- **Arranque del beat 01:** Qwen sobre `assets/personajes_referencia.png` añadiendo los tres cubos en el suelo, separados entre sí → `assets/ep04_arranque_beat01.png`.
- **Objetos estables entre clips:** exactamente tres cubos: grande rojo, mediano amarillo y pequeño verde. El tamaño de cada uno no cambia nunca.
- **Riesgos y plan B:**
  - (a) **Es un episodio de riesgo alto** (TEMPORADA_0: "estructuras que se caen"). Por eso solo hay tres piezas, y se enumeran una a una en todos los prompts.
  - (b) Que los cubos se fundan al apilarlos: deformación elástica y "tres cubos separados, que se tocan pero nunca se pegan".
  - (c) Que al caer se pierda o se duplique un cubo (beat 04): la caída es "hacia Plof", corta, sin rebotes; cerrar con el inventario.
  - (d) Que el amarillo se rompa al resbalar (beat 05): "resbala entero, rueda un poco y se para".
  - (e) Que la torre buena se tambalee de verdad en el beat 07: pedir "completamente quieta".

## Registro de generación

(se rellena clip a clip)
