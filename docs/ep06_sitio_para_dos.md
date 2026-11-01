# FICHA DE EPISODIO — EP06 "Sitio para dos"

Fecha: 01/11/2026. Tanda 1 (ep04-07). Personajes fijados por imagen (`docs/PERSONAJES.md`, regla 8).

## Datos

- **Episodio:** 06
- **Título:** Sitio para dos
- **Dominio del currículo:** posición (centro, lado, mitad)
- **Motor de historia:** compartir
- **Resuelve:** los dos
- **Duración objetivo:** ≈ 61 s

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** | Sentarse los dos en la alfombra blandita. |
| **Obstáculo** | La alfombra es pequeña y los dos quieren el centro. |
| **Concepto** | Hay sitio para los dos si cada uno ocupa su mitad. |
| **Error 01** | Se empujan por el centro, barriga contra barriga, y acaban los dos fuera, cada uno por un lado. |
| **Error 02** | Clic se sienta en la alfombra él solo, de lado. Cabe, pero Plof se queda fuera, triste. Clic tampoco está contento. |
| **Pregunta** | Clic ve la raya amarilla que parte la alfombra en dos, la señala y mira a cámara: "¿Cabemos los dos?" Pausa de 3 s. |
| **Solución** | Clic se sienta en una mitad y Plof en la otra, hombro con hombro. Caben. "¡Mitad y mitad!" |
| **Emoción** | De la rabieta de empujar a la alegría de estar juntos; el error 02 muestra que ganar solo no sienta bien. |
| **Transfer** | En casa: compartir un cojín o un sofá "cada uno su mitad". |
| **Callback** | Plof estira el brazo hacia la mitad de Clic; Clic levanta una ceja; Plof lo recoge con una sonrisa de pillo. Se ríen. |

## La pista (mecánica de la serie)

Al caerse los dos en el beat 04, **la alfombra queda vacía y se ve bien la raya amarilla que la parte en dos**. La raya está desde el primer fotograma; el niño la ve antes que ellos.

## 8 beats

| # | Beat | Seg. | Fotogramas | Acción dominante | Audio / voz |
|---|---|---|---|---|---|
| 01 | Anomalía | 5 | 124 | Se sueltan de la pose de la intro, bailan y frenan en seco: en el suelo hay una alfombrita plana de plastilina naranja, partida en dos mitades por una raya amarilla. | jingle, "¡oh!" |
| 02 | Deseo | 5 | 124 | Los dos señalan el centro de la alfombra a la vez, se miran y vuelven a señalar el centro. Se frotan las manos los dos. | "¡mmm!" glotón, risitas |
| 03 | Intento | 8 | 192 | Corren a la alfombra y se sientan los dos en el centro a la vez: chocan barriga contra barriga y se empujan con la tripa, botando como gelatina. | "boing", gruñidos de esfuerzo |
| 04 | Fallo | 8 | 192 | Un último empujón y salen despedidos cada uno por un lado: caen sentados en el suelo, fuera de la alfombra, y se aplastan y recuperan. La alfombra queda vacía con su raya amarilla bien a la vista. Se miran enfurruñados. | "plof, plof", "hmpf" |
| 05 | Mejora | 5 | 124 | Clic se sienta él solo en la alfombra. Plof se queda fuera, cabizbajo. Clic mira a Plof y deja de sonreír. Luego mira la raya amarilla junto a él. | silencio, suspiro |
| 06 | Predicción | 5 + 3 | 124 + `@pausa=3` | Clic señala la raya amarilla de la alfombra y mira a cámara. Plof también mira a cámara. Quietos. | voz: "¿Cabemos los dos?" + pausa |
| 07 | Solución | 8 | 192 | Clic se corre a una mitad y da palmaditas en la otra. Plof se sienta en ella. Quedan sentados hombro con hombro, cada uno en su mitad. Se abrazan de lado, contentos. | palmaditas, "ping", voz: "¡Mitad y mitad!", risas |
| 08 | Eco | 5 | 124 | Plof estira el brazo hacia la mitad de Clic, Clic levanta una ceja, Plof recoge el brazo con sonrisa de pillo. Se ríen los dos. | risita pilla, risas |

## Go / no-go

- [x] ~~el aprendizaje puede quitarse~~ → sin repartir la alfombra no se sientan los dos
- [x] ~~más de un problema central~~ → uno: el sitio
- [x] ~~la pregunta no se puede responder~~ → la raya está ahí desde el principio
- [x] ~~error de relleno~~ → empujar echa a los dos; quedarse solo no hace feliz
- [x] ~~estímulo sin función~~ → la caída deja la alfombra vacía y la raya a la vista
- [x] ~~final sin resolver~~ → sentados los dos

Luz verde: emoción muy legible (enfurruñados → juntos), conflicto que todo niño conoce.

## Producción

- **Focos (2):** la alfombra con su raya y los personajes. Es el episodio más sencillo de generar de la tanda.
- **Arranque del beat 01:** Qwen sobre la referencia, añadiendo la alfombrita naranja plana en el suelo, delante de ellos, con una raya amarilla recta que la parte en dos mitades iguales. Ancha justo para dos sentados hombro con hombro.
- **Objetos estables:** la alfombra (no se arruga, no se dobla, no cambia de tamaño) y la raya amarilla (siempre visible y recta cuando no hay nadie encima).
- **Riesgos y plan B:**
  - (a) Que los personajes se fundan al chocar barrigas (beat 03): "dos figuras separadas que botan al chocar y nunca se pegan".
  - (b) Que la alfombra se arrugue o se levante con los empujones: "plana, pegada al suelo".
  - (c) Que los dos sentados no quepan y uno quede medio fuera en el beat 07: aceptable si se lee "uno en cada mitad".

## Registro de generación

(se rellena clip a clip)
