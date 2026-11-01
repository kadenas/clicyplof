# FICHA DE EPISODIO — EP08 "La banqueta coja"

Fecha: 01/11/2026. Tanda 2 (ep08-11). Personajes fijados por imagen (`docs/PERSONAJES.md`, regla 8).

## Datos

- **Episodio:** 08
- **Título:** La banqueta coja
- **Dominio del currículo:** cantidad (cuatro patas; una menos y se cae)
- **Motor de historia:** construir (arreglar la banqueta)
- **Resuelve:** Plof, sentándose encima
- **Duración objetivo:** ≈ 61 s

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** | Plof, cansado de bailar, quiere sentarse en la banqueta. |
| **Obstáculo** | La banqueta tiene solo tres patas, en tres esquinas: la cuarta esquina está vacía y se vence hacia ese lado. |
| **Concepto** | Una banqueta necesita cuatro patas. Con tres, se cae por el lado de la que falta. |
| **Error 01** | Plof se sienta de golpe: la banqueta se ladea hacia la esquina vacía y le tira al suelo. Lo intenta otra vez: igual. |
| **Error 02** | Clic se sienta con mucho cuidado, haciendo equilibrio hacia el lado bueno: aguanta mientras no se mueve, pero en cuanto se mueve, se tambalea. Mejor, pero no sirve. |
| **Pregunta** | Plof, desde el suelo, ve la pata suelta y la esquina vacía. Coge la pata, la levanta y mira a cámara: "¿Cuántas patas necesita?" Pausa de 3 s. |
| **Solución** | Plof pone la pata en la esquina vacía y se sienta encima con todo su peso: la pata se queda pegada. La banqueta ya no se mueve. La narradora cuenta: "Una, dos, tres… ¡cuatro!" |
| **Emoción** | Plof pasa del enfado (le tira dos veces) al orgullo de arreglarla; Clic, de la maña a la sorpresa. |
| **Transfer** | En casa: contar las patas de las sillas, de la mesa, del perro. |
| **Callback** | Plof bota sentado en la banqueta, cada vez más fuerte: la banqueta aguanta. Clic se ríe. |

## La pista (mecánica de la serie)

Cuando Plof se cae en el beat 04, **la banqueta queda volcada con las patas al aire y se ve la esquina vacía**, y la pata suelta está tirada en el suelo al lado de Plof. Plof es el que la lía y, esta vez, el que ve la pista desde el suelo.

## 8 beats

| # | Beat | Seg. | Fotogramas | Acción dominante | Audio / voz |
|---|---|---|---|---|---|
| 01 | Anomalía | 5 | 124 | Se sueltan de la pose de la intro, bailan y frenan en seco, sofocados: en el suelo hay una banqueta de plastilina (asiento cuadrado verde y tres patas naranjas en tres esquinas; la cuarta esquina, sin pata) y una pata naranja suelta, tirada a un lado. | jingle, resoplidos |
| 02 | Deseo | 5 | 124 | Plof se abanica con la mano, cansado, ve la banqueta y le da palmaditas al asiento con cara de "¡mía!". | resoplido, "¡ah!" |
| 03 | Intento | 8 | 192 | Plof se sienta de golpe: la banqueta se ladea hacia la esquina vacía y Plof resbala al suelo. Se levanta, la endereza, se sienta otra vez: igual. Clic se tapa la boca. | "crec", "plof" |
| 04 | Fallo | 8 | 192 | Plof salta para sentarse con fuerza: la banqueta vuelca del todo y queda patas arriba. Plof cae de culo, se aplasta y se recupera. Desde el suelo, ve la esquina sin pata y la pata suelta a su lado. | "plof", "boing", "¿eh?" |
| 05 | Mejora | 5 | 124 | Clic endereza la banqueta y se sienta con mucho cuidado, inclinado hacia el lado bueno, con los brazos abiertos para hacer equilibrio. Aguanta… hasta que se mueve un poco y se tambalea. Se levanta de un salto. | "uuuh", tambaleo |
| 06 | Predicción | 5 + 3 | 124 + `@pausa=3` | Plof coge la pata suelta, la levanta y mira a cámara. Clic, junto a la banqueta, también mira a cámara. Quietos. | voz: "¿Cuántas patas necesita?" + pausa |
| 07 | Solución | 8 | 192 | Plof pone la pata debajo de la esquina vacía, se sienta encima de la banqueta con todo su peso y la pata se queda pegada. La banqueta queda recta y quieta. Clic toca las patas una a una. Saltan de alegría. | "chof", "ping", voz: "Una, dos, tres… ¡cuatro!", risas |
| 08 | Eco | 5 | 124 | Plof bota sentado en la banqueta, cada vez más fuerte: la banqueta aguanta sin moverse. Clic se ríe. | "boing, boing", risas |

## Go / no-go

- [x] ~~el aprendizaje puede quitarse~~ → sin la cuarta pata no se puede sentar
- [x] ~~más de un problema central~~ → uno: que la banqueta aguante
- [x] ~~la pregunta no se puede responder~~ → la esquina vacía y la pata suelta se ven desde el beat 01
- [x] ~~error de relleno~~ → la fuerza (Plof) y el equilibrio (Clic) fallan por lo mismo: falta una pata
- [x] ~~estímulo sin función~~ → la banqueta volcada enseña la esquina vacía
- [x] ~~final sin resolver~~ → banqueta firme

Luz verde: comedia física muy clara para los de 2 años; contar hasta cuatro para los mayores.

## Producción

- **Focos (2):** la banqueta con su pata suelta, y los personajes.
- **Arranque del beat 01:** Qwen sobre la referencia, añadiendo la banqueta (más baja que Plof, asiento cuadrado verde, tres patas naranjas en tres esquinas y la esquina delantera derecha sin pata) y una pata naranja suelta tumbada en el suelo, aparte.
- **Objetos estables:** exactamente un asiento verde y cuatro patas naranjas (tres puestas + una suelta hasta el beat 07; cuatro puestas desde el 07).
- **Riesgos y plan B:**
  - (a) **Que el modelo le ponga cuatro patas a la banqueta desde el principio** (lo "normal" para él). En el arranque, revisar que la esquina vacía se ve bien; en los prompts, repetir "tres patas, una esquina sin pata" en cada tramo.
  - (b) Que la banqueta se rompa al volcar: deformación elástica, "vuelca entera".
  - (c) Que la pata suelta desaparezca en los beats 02-05, donde no hace nada: tarea explícita en cada tramo (regla 7).
  - (d) Beat 07: que la pata no "se pegue". Basta con que quede debajo de la esquina y la banqueta deje de moverse.

## Registro de generación

(se rellena clip a clip)
