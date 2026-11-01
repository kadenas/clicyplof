# TEMPORADA 0 — escaleta de 24 episodios

Serie **"Clic y Plof"**. Fecha: 16/09/2026.

Mapa construido sobre la sección 08 de `TATO_PLOF_VANGUARDIA_EDUCATIVA_PLAN.html`:
**4 motores de historia × 6 dominios de aprendizaje = 24 premisas**. Una casilla, un episodio.

Antes de producir cualquiera de estos, rellenar su ficha con `PLANTILLA_FICHA_EPISODIO.md`
y pasar el go/no-go. Esta escaleta es el mapa, no el guion.

---

## Reglas de la serie que salen de esta escaleta

**El arranque es siempre el mismo.** Los dos están en la postura del final de la intro (Clic
apoyado en la cabeza de Plof), se sueltan a jugar, saltar o perseguirse, y frenan en seco
cuando ven el reto. Es el beat 01 (Anomalía) y es la firma de la serie: el niño de 2 años
reconoce el arranque y sabe que empieza. *(Cambiado el 01/11/2026: antes "entraban" desde
fuera del cuadro, pero así el modelo se inventa a los personajes. Ver `docs/PERSONAJES.md`.)*

**Quién resuelve, y por qué importa.** Si Clic resolviera siempre, Plof sería el tonto y Clic
el profesor, que es lo que la guía prohíbe. La mecánica de la serie es:

> **Plof se lanza y la lía. Al liarla, pasa algo que Clic ve. Esa es la pista.**

Los dos son imprescindibles: sin el desastre de Plof no hay pista, y sin la mirada de Clic
no hay solución. Y en un tercio de los episodios **gana Plof**: hay problemas que se resuelven
empujando más fuerte o saltando más alto, y ahí el que se equivoca es Clic por pensar de más.
El reparto está marcado en la columna "resuelve" y está equilibrado a propósito.

**El mundo.** Estudio blanco sin horizonte. Todo lo que aparece es **plastilina**: si hace falta
un árbol, es un árbol de plastilina, como el anillo verde del ep01. Nunca hay paisaje, ni
decorado, ni cielo. Máximo **3 focos semánticos** en pantalla (guía, sección de dramaturgia
vertical): los dos personajes cuentan como uno.

**Las tres capas de edad (2-6).** Cada episodio tiene que funcionar en las tres:
- **2-3 años:** la comedia física se entiende sin una sola palabra.
- **3-4 años:** el problema central es visual y concreto, y se ve cómo se resuelve.
- **5-6 años:** el beat 06 (predicción) les deja adelantarse en voz alta antes del final.

**Firmas sonoras (aprobadas el 01/11/2026).** Cuando Clic tiene una idea, levanta el dedo
índice y suena un **"clic"** seco, como dos piezas que encajan. Cuando Plof se cae o se aplasta,
suena un **"plof"** blando. Van en todos los episodios desde el ep00: los nombres de los
personajes son también sonidos que el niño reconoce y espera.

**Episodio de presentación (ep00, aprobado el 01/11/2026): "¡Hola, Clic y Plof!"** Se publica
antes del ep01. Presenta a los dos, Plof la lía dos veces con una pelota y una portería, y Clic
tiene la idea (apuntar y empujar suave). Ficha en `docs/ep00_hola_clic_y_plof.md`.

**Ningún color de objeto puede ser el azul de los muñecos.** Se confunde con sus cuerpos
(pasó con la ficha azul del ep01).

**Todo es plastilina y se comporta como plastilina.** No es un detalle estético, es la firma de
la serie: los personajes se aplastan al caer, rebotan, se estiran al saltar, y los objetos se
abollan cuando los aprietan y guardan las huellas de los dedos. El texto exacto que hay que
copiar en todos los prompts está en `prompts/serie/BLOQUE_PLASTILINA.txt`.

> **Cuidado:** la deformación tiene que ser **elástica**. La plastilina se aplasta y vuelve a su
> forma, su tamaño y su color exactos. Si se le pide deformación libre, el modelo la estira sin
> control y acaba perdiendo o duplicando objetos: fue el fallo del beat 05 del ep01, donde una
> ficha se estiró como un chicle y quedaron dos. El bloque fijo ya lleva esa cláusula.

**Estructura fija de cada episodio.**

| Pieza | Duración | Cómo se hace |
|---|---|---|
| **Careta corta** | 2-3 s | Recorte del final de la intro (el título formándose y el salto), para los Shorts. La intro completa de 8 s **no abre los Shorts**: son 8 s de logo antes de la historia, y en un feed eso cuesta audiencia |
| **Rótulo del episodio** | 3 s | El título del episodio escrito en letras de plastilina **y dicho por la voz de la narradora**. El texto fijo se genera con Qwen (los modelos de vídeo escriben mal) y la voz se pide en el clip |
| **8 beats** | 52 s en total: 5 s los beats de situación, 8 s los tres de acción (ver tabla) | El motor narrativo de la guía, con la duración de cada beat fijada por lo que necesita |
| **Cierre** | 3 s | Siempre el mismo clip: Clic y Plof abrazados saludando a cámara, y un círculo que se cierra sobre ellos (`herramientas/cerrar_iris.py`). Se genera una vez y se reutiliza |

Duración de cada beat (decidida el 16/09/2026; análisis en `DECISION_DURACION_CLIPS.md`):

| # | Beat | Duración | Fotogramas |
|---|---|---|---|
| 01 | Anomalía | 5 s | 124 |
| 02 | Deseo | 5 s (3 s / 73 si la ficha lo justifica) | 124 |
| 03 | Intento | 8 s | 192 |
| 04 | Fallo | 8 s | 192 |
| 05 | Mejora | 5 s | 124 |
| 06 | Predicción | 5 s + 3 s de pausa congelada (`@pausa=3`) | 124 |
| 07 | Solución | 8 s | 192 |
| 08 | Eco | 5 s | 124 |

Total ≈ **61 s** (2-3 + 3 + 52 + 3), dentro del objetivo de 56-72 s de la guía.

**Dos montajes distintos del mismo material** (decidido el 16/09/2026), aprovechando que la guía
ya separa Shorts = descubrimiento y largo = profundidad:

- **Shorts (lo que se publica):** careta corta + rótulo + los 52 s de beats + cierre ≈ **61 s**.
- **Recopilaciones (el largo):** la intro completa de 8 s una sola vez al principio, y detrás los
  episodios seguidos.

El motor narrativo de la guía se llama "64 SECOND SYSTEM" (8 beats × 8 s). El 16/09/2026 se
decidió conservar **la secuencia** de los ocho beats, que es lo que hace que el niño reconozca el
formato y se adelante en la pausa de predicción, pero **no la duración fija de 8 s**: cada beat
dura lo que necesita (5 s los de situación, 8 s los tres de acción). Motivos, medidos en la
máquina de producción: los clips cortos fallan menos y cuestan menos cuando fallan, el ritmo
respira donde debe, y el episodio baja de 3,2 h a ≈ 2,3 h de GPU. Regla fija: **un clip por beat;
nunca partir un beat en dos clips** (cada corte degrada el fondo y el azul).

El episodio 01 se produjo antes de esta decisión con 8 × 8 s y se queda así; desde el 02 se
aplican las duraciones nuevas.

---

## El mapa: 4 motores × 6 dominios

| | **POSICIÓN** | **CANTIDAD** | **FORMA** | **CAUSA** | **EMOCIÓN** | **COOPERAR** |
|---|---|---|---|---|---|---|
| **ENCONTRAR** | 03 | 07 | 11 | 15 | 19 | 23 |
| **CONSTRUIR** | 04 | 08 | 12 | **01 ✅ · 02** | 20 | 24 |
| **TRANSPORTAR** | 05 | 10 | 13 | 16 | 21 | 17 |
| **COMPARTIR** | 06 | 09 | 14 | 18 | 22 | **25** |

*(La numeración es el orden de producción, no el orden de la rejilla. Las 24 casillas están todas cubiertas; el ep. 02 es una repetición deliberada de la casilla del 01, así que la temporada tiene **25 episodios**.)*

---

## Los 25 episodios

| # | Motor × Dominio | Título | El reto | Concepto que desbloquea | Resuelve |
|---|---|---|---|---|---|
| **01** | Construir × Causa | **Los colores** ✅ | Un anillo verde vacío y solo fichas azul y amarilla | Azul + amarillo = verde | Los dos |
| **02** | Construir × Causa | **El morado** | Vuelve el anillo, ahora hay que llenar un hueco morado con fichas roja y azul | Rojo + azul = morado *(repetir para dominar)* | Plof, que ya se sabe el truco |
| **03** | Encontrar × Posición | **El balón de arriba** | Jugando al balón, se queda encajado en lo alto de un árbol de plastilina | Arriba / abajo. Para llegar más alto hay que subirse a algo | Clic (Plof salta y no llega) |
| **04** | Construir × Posición | **La torre que se cae** | Apilan piezas y la torre se derrumba siempre | Lo grande debajo, lo pequeño encima | Clic |
| **05** | Transportar × Posición | **El otro lado** | Hay que pasar una pelota al otro lado de un muro de plastilina que tiene un arco abierto abajo | Si no puedes por encima, busca el paso | Plof, que se cansa de lanzarla y la hace rodar por el arco |
| **06** | Compartir × Posición | **Sitio para dos** | Una alfombra pequeña y los dos quieren el centro | Hay sitio si cada uno ocupa su mitad | Los dos |
| **07** | Encontrar × Cantidad | **Falta una** | Juegan con tres bolas; una rueda fuera de cuadro | Contar hasta tres. "Faltan" tiene forma de hueco | Clic contando |
| **08** | Construir × Cantidad | **La banqueta coja** | Montan una banqueta y siempre cojea | Cuatro patas. Una menos y se cae | Plof, sentándose encima |
| **09** | Compartir × Cantidad | **Una para cada uno** | Cinco galletas de plastilina para dos | Repartir igual: dos y dos, y la que sobra por la mitad | Clic |
| **10** | Transportar × Cantidad | **Un solo viaje** | Llevan bolas de una en una y no acaban nunca | Muchos en uno: meterlas todas en un cuenco | Clic (Plof está agotado) |
| **11** | Encontrar × Forma | **La que no encaja** | Entre muchas piezas iguales hay una distinta escondida | Reconocer por la forma, no por el color | Clic |
| **12** | Construir × Forma | **El agujero cuadrado** | Un hueco cuadrado y solo piezas redondas | La plastilina cambia de forma: se aplasta una redonda hasta hacerla cuadrada | Plof, aplastándola |
| **13** | Transportar × Forma | **Lo que rueda** | Un bloque cuadrado pesadísimo que no avanza | Lo redondo rueda, lo cuadrado no | Plof, que de tanto empujar le redondea las esquinas sin querer |
| **14** | Compartir × Forma | **La mitad justa** | Una sola pieza grande y la parten mal: un trozo mucho mayor | Igual / desigual. Comparar antes de repartir | Los dos |
| **15** | Encontrar × Causa | **El rastro** | Una bola rueda fuera de cuadro y deja un surco marcado en el suelo blando | Las cosas dejan marcas, y las marcas dicen por dónde se fueron | Clic |
| **16** | Transportar × Causa | **Cuesta abajo** | Empujan algo pesado y no avanza | Una rampa: si lo sueltas en cuesta, baja solo | Plof, al tropezar y soltarlo |
| **17** | Transportar × Cooperar | **El palo largo** | Una pieza larguísima que uno solo no puede llevar | Uno de cada punta, y hay que ir al mismo paso | Los dos |
| **18** | Compartir × Causa | **No aprietes** | Comparten algo blando y Plof lo aprieta hasta dejarlo hecho un churro | Cómo tratas algo cambia lo que le pasa | Los dos, arreglándolo a cuatro manos |
| **19** | Encontrar × Emoción | **Plof se esconde** | Plof la lía, le da vergüenza y desaparece de cuadro | Cuando alguien se esconde no siempre juega: a veces está triste | Clic, buscándolo sin regañar |
| **20** | Construir × Emoción | **Lo que se rompió** | Plof rompe sin querer lo que Clic estaba construyendo | El enfado pasa; lo roto se puede rehacer, y entre dos sale mejor | Los dos |
| **21** | Transportar × Emoción | **Yo puedo solo** | Plof se empeña en cargar con todo, se agobia y se cae | Pedir ayuda no es perder | Plof, cuando por fin la pide |
| **22** | Compartir × Emoción | **Todavía no** | **Clic** no quiere prestar su pieza favorita: no se fía de las manos de Plof | Esperar sin arrebatar. El otro acaba dándotela | Plof, esperando sentado sin quitársela |
| **23** | Encontrar × Cooperar | **Cuatro ojos** | Se pierde algo diminuto y por separado no lo encuentran | Repartirse el terreno: tú ese lado, yo este | Los dos |
| **24** | Construir × Cooperar | **Hacen falta dos** | Un arco que se cae en cuanto uno suelta | Hay cosas que no se pueden hacer solo, por mucho que insistas | Los dos |
| **25** | Compartir × Cooperar | **Por turnos** | Un solo balancín de plastilina y los dos encima a la vez: no funciona | El turno. Cuentas hasta tres y cambias | Los dos |

**Reparto de quién resuelve (recontado el 16/09/2026): Clic 8, Plof 8, los dos 9.**

**Y el reparto del problema emocional también está equilibrado**, que es la otra mitad del asunto: en el 19 y el 21 el que se descompone es Plof (vergüenza, cabezonería); en el 20 y el 22 es Clic (enfado, no querer prestar). Si los cuatro fueran de Plof, Clic acabaría siendo el adulto sereno que nunca falla y Plof el niño problemático.

---

## Orden de producción y por qué

El orden **no** es el de la rejilla. Está pensado por dos criterios: pagar las promesas que
deja cada final, y empezar por lo que es fácil de generar.

1. **El 02 va primero** porque el ep01 termina prometiendo "¿Y rojo con azul?". Esa promesa se
   paga en el episodio siguiente o se pierde.
2. **Del 03 al 14, lo generable.** Pocos objetos, físicas simples, nada que tenga que entrar o
   salir de dentro de nada. Son las reglas de `ep01_los_colores.md` § "Aprendido al generar".
3. **Los de emoción (19-22) al final.** Son los mejores de la temporada y los más difíciles: la
   emoción hay que leerla en una cara de plastilina sin diálogo. Conviene llegar a ellos con
   veinte episodios de oficio encima.

**Riesgos de generación ya identificados para esta escaleta:**

- **Ep. 03, 04, 24 (apilar, torres, arcos):** las estructuras que se caen implican muchas piezas
  moviéndose a la vez. Alto riesgo de que el modelo pierda o invente piezas. Limitar a 3 piezas.
- **Ep. 07, 09:** contar exige que el número de objetos sea exacto en todos los fotogramas. Es
  justo lo que peor se le da al modelo. Enumerar las piezas una a una en el prompt (funcionó
  con los nueve pegotes de la intro) y no pasar de 5.
- **Ep. 15 (el rastro):** algo que sale de cuadro y deja huellas. Las huellas hay que describirlas
  como objetos presentes desde el primer fotograma, no como algo que aparece.
- **Ep. 05 (por debajo del muro):** "pasar por dentro de" es exactamente el caso que hizo fallar
  el beat 05 del ep01. Reformular: el muro tiene un arco abierto desde el primer fotograma.

---

## Lo que queda por decidir

- ~~Si cada episodio lleva rótulo propio~~ **DECIDIDO (16/09/2026): sí.** Intro de la serie
  siempre igual, y detrás un rótulo de 3 s con el título del episodio escrito y dicho por la voz.
- ~~Si el atrezo de plastilina entra~~ **DECIDIDO (16/09/2026): sí.** Árbol, muro, rampa,
  banqueta, cuenco y alfombra son válidos mientras sean de plastilina y se comporten como tal.
- ~~Si la intro de los episodios se acorta~~ **DECIDIDO (16/09/2026): sí.** Careta corta en los Shorts, intro completa en las recopilaciones.
