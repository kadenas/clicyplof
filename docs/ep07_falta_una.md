# FICHA DE EPISODIO — EP07 "Falta una"

Fecha: 01/11/2026. Tanda 1 (ep04-07). Personajes fijados por imagen (`docs/PERSONAJES.md`, regla 8).

## Datos

- **Episodio:** 07
- **Título:** Falta una
- **Dominio del currículo:** cantidad (contar hasta tres; "falta" tiene forma de hueco)
- **Motor de historia:** encontrar
- **Resuelve:** Clic, contando
- **Duración objetivo:** ≈ 61 s

## Cambio sobre la escaleta

La escaleta dice que una bola "rueda fuera de cuadro". **Se cambia: rueda hasta la esquina del cuadro y se queda allí, a la vista.** Motivos: (1) "nada entra ni sale del cuadro" es una de las protecciones que mejor funcionan con el modelo; si sale, al volver puede entrar otra distinta o ninguna; (2) es mejor para los de 2-3 años: **ven la bola desde el principio y pueden gritar "¡ahí!"** mientras los personajes no la ven. Es el mismo juego que "está detrás de ti".

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** | Volver a poner cada bola en su marca: tres bolas, tres marcas. |
| **Obstáculo** | Al bailar, Plof las desordena y una (la verde) se va rodando a la esquina; ellos no la ven. |
| **Concepto** | Contar hasta tres. Si hay tres marcas y dos bolas, falta una: la marca vacía es el hueco de la que falta. |
| **Error 01** | Plof coloca la roja y la amarilla y lo da por terminado. Clic señala la marca vacía. Plof se sienta él encima, hecho bola, haciéndose pasar por la tercera bola. |
| **Error 02** | Plof se tambalea y rueda fuera de la marca. Clic cuenta las marcas (una, dos, tres) y las bolas (una, dos…). |
| **Pregunta** | Clic, con dos dedos levantados, junto a la marca vacía, mira a cámara: "¿Dónde está la que falta?" Pausa de 3 s. (Los niños señalan la esquina.) |
| **Solución** | Clic se gira, ve la verde en la esquina, va, la coge y la pone en la marca vacía. "¡Tres!" |
| **Emoción** | Plof pasa del "ya está" chapucero a la risa de su propio truco; Clic, de la duda a la satisfacción de contar bien. |
| **Transfer** | En casa: contar los zapatos de la entrada, los platos de la mesa. ¿Falta alguno? |
| **Callback** | Plof se hace bola y se sienta al lado de las tres bolas, como una cuarta. Clic le cuenta con el dedo y se ríe: "¿Cuatro?" |

## La pista (mecánica de la serie)

Plof la lía dos veces (desordena las bolas y luego se hace pasar por una). Su truco de hacerse bola **deja la marca vacía a la vista**, y eso es lo que hace contar a Clic.

## 8 beats

| # | Beat | Seg. | Fotogramas | Acción dominante | Audio / voz |
|---|---|---|---|---|---|
| 01 | Anomalía | 5 | 124 | Se sueltan de la pose de la intro y bailan. En el suelo hay tres marcas planas rosas en fila, con una bola encima de cada una: roja, amarilla y verde. Plof, bailando, da un pisotón junto a la fila: las tres bolas ruedan fuera de sus marcas; la verde sigue rodando y se para en la esquina inferior derecha, a la vista. Los dos frenan en seco y miran las marcas vacías. | jingle, rodar, "¡uy!" |
| 02 | Deseo | 5 | 124 | Plof coge la roja y la pone en la primera marca; coge la amarilla y la pone en la segunda. Se sacude las manos orgulloso, de espaldas a la esquina. La tercera marca queda vacía. | "toc, toc", risita |
| 03 | Intento | 8 | 192 | Clic señala la marca vacía. Plof se rasca la cabeza, sonríe con picardía, se hace bola y se sienta encima de la tercera marca, quietecito, haciéndose pasar por la bola que falta. Clic se tapa la boca para no reírse. | "¡hmm!", risa contenida |
| 04 | Fallo | 8 | 192 | Plof, hecho bola, se tambalea, rueda fuera de la marca, da una voltereta y se queda sentado, mareado. La tercera marca vuelve a estar vacía. La verde sigue quieta en la esquina. | rodar, "plof", "ooh" |
| 05 | Mejora | 5 | 124 | Clic toca las marcas una a una con el dedo, y luego las bolas una a una. Se queda mirando la marca vacía. | voz: "Una, dos, tres… una, dos…" |
| 06 | Predicción | 5 + 3 | 124 + `@pausa=3` | Clic, junto a la marca vacía, levanta dos dedos y mira a cámara con cara de pregunta. Plof mira a cámara también. Quietos. La verde, en la esquina, a la vista. | voz: "¿Dónde está la que falta?" + pausa |
| 07 | Solución | 8 | 192 | Clic se gira, ve la bola verde en la esquina, va hasta ella, la coge y vuelve a ponerla en la marca vacía. Tres bolas en tres marcas. Saltan de alegría. | pasos, "ping", voz: "¡Tres!", risas |
| 08 | Eco | 5 | 124 | Plof se hace bola y se sienta al lado de las tres bolas, como una cuarta. Clic lo señala con el dedo y se ríe. | voz: "¿Cuatro?", risas |

## Go / no-go

- [x] ~~el aprendizaje puede quitarse~~ → sin contar no saben que falta una
- [x] ~~más de un problema central~~ → uno: completar las tres
- [x] ~~la pregunta no se puede responder~~ → la verde se ve en la esquina todo el tiempo
- [x] ~~error de relleno~~ → el truco de Plof hace evidente el hueco
- [x] ~~estímulo sin función~~ → la voltereta deja la marca vacía otra vez
- [x] ~~final sin resolver~~ → tres en tres

Luz verde: "¡ahí!" es la participación más fácil que existe para un niño de 2 años.

## Producción

- **Focos (3):** las marcas con sus bolas (fila), la bola verde en la esquina (es parte del mismo grupo) y los personajes.
- **Arranque del beat 01:** Qwen sobre la referencia, añadiendo en el suelo, delante de ellos, una fila de tres marcas planas rosas con una bola encima de cada una (roja, amarilla, verde), separadas. La esquina inferior derecha del suelo queda **libre** para que la verde ruede hasta allí.
- **Objetos estables:** **exactamente tres bolas y tres marcas en todos los fotogramas** (enumerar una a una en cada prompt, como los nueve pegotes de la intro); la verde, cuando está en la esquina, no se mueve hasta el beat 07.
- **Riesgos y plan B:**
  - (a) **Contar es lo que peor se le da al modelo** (TEMPORADA_0). Pocas piezas, enumeradas, de colores distintos. Si se duplica una bola, otra semilla.
  - (b) Que la verde se salga del cuadro al rodar en el beat 01: "rueda despacio y se para en la esquina, dentro del cuadro, a la vista".
  - (c) Que Plof hecho bola se confunda con una bola más: es azul y del tamaño de su barriga, mucho más grande que las bolas, y ninguna bola es azul.
  - (d) Las marcas rosas: que no se confundan con la alfombra del ep06 ni con nada rojo. Rosa claro.

## Registro de generación

(se rellena clip a clip)
