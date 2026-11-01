# FICHA DE EPISODIO — EP05 "El otro lado"

Fecha: 01/11/2026. Tanda 1 (ep04-07). Personajes fijados por imagen (`docs/PERSONAJES.md`, regla 8).

## Datos

- **Episodio:** 05
- **Título:** El otro lado
- **Dominio del currículo:** posición (por encima / por debajo; si no puedes por encima, busca el paso)
- **Motor de historia:** transportar
- **Resuelve:** Plof, que se cansa de lanzar la pelota y la hace rodar por el arco
- **Duración objetivo:** ≈ 61 s

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** | Llevar la pelota naranja hasta la estrella amarilla que hay al otro lado del muro. |
| **Obstáculo** | Un muro de plastilina que ocupa todo el ancho del cuadro. Clic ve por encima, Plof no. |
| **Concepto** | Si no puedes por encima, busca el paso: el arco de abajo. |
| **Error 01** | Plof lanza la pelota por encima: choca con el borde del muro y vuelve. |
| **Error 02** | Clic empuja el muro para moverlo: se abomba, tiembla y vuelve a su sitio. Al agacharse a empujar, mira por el arco y ve la estrella. |
| **Pregunta** | Plof, sentado y cansado, con la pelota delante. Clic señala el arco. Los dos miran a cámara: "¿Por dónde puede pasar?" Pausa de 3 s. |
| **Solución** | Plof empuja la pelota rodando por el suelo: pasa por el arco y se para encima de la estrella. "¡Por abajo!" |
| **Emoción** | Plof pasa del empeño agotado a la sorpresa de que era fácil; Clic, de la fuerza a mirar. |
| **Transfer** | En casa: hacer rodar una pelota por debajo de una silla o de una mesa. |
| **Callback** | Plof se hace bola y rueda hacia el arco para pasar él también: es demasiado grande, rebota blandito contra el muro y se ríe. |

## La pista (mecánica de la serie)

En este episodio **el que lía la cosa es Clic**, empujando el muro, y **es él quien ve la pista** al agacharse (el arco). Pero la ejecuta Plof, que está tan cansado de lanzar que la empuja rodando sin ganas. El niño ha visto el arco desde el primer fotograma.

## 8 beats

| # | Beat | Seg. | Fotogramas | Acción dominante | Audio / voz |
|---|---|---|---|---|---|
| 01 | Anomalía | 5 | 124 | Se sueltan de la pose de la intro, bailan y frenan en seco: delante de ellos hay un muro de plastilina marrón que cruza el cuadro, con un arco pequeño abierto abajo. Al otro lado, en el suelo, una estrella plana amarilla. A sus pies, una pelota naranja. | jingle, "¿mmm?" |
| 02 | Deseo | 5 | 124 | Clic se estira y mira por encima del muro, ve la estrella y la señala. Plof da saltitos pero no ve nada. Clic le enseña la pelota y señala la estrella: hay que llevarla allí. | "¡oh!", saltitos |
| 03 | Intento | 8 | 192 | Plof coge la pelota y la lanza por encima del muro: choca con el borde de arriba y vuelve rodando hacia él. Lo intenta otra vez más fuerte: igual. Clic se tapa la boca. | "boing", rodar |
| 04 | Fallo | 8 | 192 | Plof lanza con todas sus fuerzas girando sobre sí mismo: la pelota sube recta y le cae en la cabeza. Plof se aplasta como una tortita y vuelve a su forma, mareado. Se sienta en el suelo con la pelota delante. | giro, "plof", "ooh" mareado |
| 05 | Mejora | 5 | 124 | Clic empuja el muro con las dos manos: se abomba, tiembla y vuelve a su sitio. Al agacharse para empujar más fuerte, mira por el arco y ve la estrella al otro lado. Abre mucho los ojos. | empuje blando, "ping" pequeño |
| 06 | Predicción | 5 + 3 | 124 + `@pausa=3` | Clic señala el arco a Plof. Plof, sentado con la pelota delante, mira el arco y luego a cámara. Clic también mira a cámara. Quietos. | voz: "¿Por dónde puede pasar?" + pausa |
| 07 | Solución | 8 | 192 | Plof empuja la pelota rodando por el suelo, sin ganas: pasa por el arco y sigue rodando despacio hasta pararse encima de la estrella. Plof se levanta de un salto, Clic aplaude. Saltan de alegría. | rodar, "ping", voz: "¡Por abajo!", risas |
| 08 | Eco | 5 | 124 | Plof se hace bola y rueda hacia el arco para pasar él también: es demasiado grande, rebota blandito contra el muro y se queda sentado riéndose. Clic se ríe. | "boing" blando, risas |

## Go / no-go

- [x] ~~el aprendizaje puede quitarse~~ → sin el arco la pelota no llega
- [x] ~~más de un problema central~~ → uno: llevar la pelota a la estrella
- [x] ~~la pregunta no se puede responder~~ → el arco está a la vista desde el beat 01
- [x] ~~error de relleno~~ → por encima no se puede, empujar no sirve, y así se descubre el arco
- [x] ~~estímulo sin función~~ → la pelota en la cabeza es la consecuencia del lanzamiento
- [x] ~~final sin resolver~~ → la pelota está encima de la estrella

Luz verde: el de 2 años ve el arco y grita antes que Plof; el callback es comedia física sobre el tamaño.

## Producción

- **Focos (3):** el muro con su arco, la pelota y la estrella (van juntas: son el objetivo), los personajes.
- **Arranque del beat 01:** Qwen sobre la referencia. Muro marrón de lado a lado del cuadro, a media profundidad, **más bajo que la cabeza de Clic y más alto que Plof**, con un arco pequeño abierto abajo en el centro, de tamaño justo para la pelota. Estrella amarilla plana en el suelo detrás del muro, visible por el arco. Pelota naranja a sus pies. Personajes delante del muro. **Puede que Qwen tenga que abrir el plano** (más que en el ep02): revisar a los personajes con la referencia.
- **Objetos estables:** muro (no se mueve nunca de sitio; solo se abomba en el beat 05 y vuelve), arco siempre abierto, estrella siempre en su sitio, una sola pelota naranja.
- **Riesgos y plan B:**
  - (a) **Pasar por el arco = "pasar por dentro de"** (fallo del ep01). El arco está abierto desde el primer fotograma y la pelota es claramente más pequeña que él. Si se pierde la pelota al cruzar, plan B: que la pelota pase rodando **junto al extremo del muro** (muro que no llega al borde derecho).
  - (b) Que los personajes atraviesen el muro: "el muro es sólido; nadie lo cruza".
  - (c) Que la pelota se quede detrás del muro y no se vea sobre la estrella: el muro es bajo para que la estrella se vea por encima del muro desde la cámara.
  - (d) Beat 08: que Plof se cuele por el arco. Pedir explícitamente "es más grande que el arco y no cabe".

## Registro de generación

(se rellena clip a clip)
