# FICHA DE EPISODIO — EP01 "Los colores"

> **Aviso (16/09/2026):** los personajes se llaman ahora **Clic** (antes "Tato") y Plof, y la serie se titula **"Clic y Plof"**. Esta ficha ya usa los nombres nuevos, pero el vídeo ya montado (`output/plof_ep01_v2.mp4`) sigue llevando la marca antigua: su rótulo dice "PLOF" y la despedida del beat 08 dice "¡Hasta el próximo Plof!" (esta última sigue siendo válida). Para publicarlo hay que volver a montarlo con la intro nueva de la serie (`output/v_intro_cp2_00001_.mp4`). Los prompts de `prompts/ep01/` **no** se han renombrado a propósito: son el registro de lo que produjo estos clips.

Fecha: 14/09/2026. Versión 2 del piloto (la versión 1, horizontal y sin motor narrativo, está en `output/plof_ep01_los_colores.mp4`).

## Datos

- **Episodio:** 01
- **Título:** Los colores
- **Dominio del currículo:** causa / efecto (mezclar → color nuevo) con apoyo de forma (encajar)
- **Motor de historia:** construir (completar el anillo)
- **Duración objetivo:** ≈ 72 s (intro 5 s + título 3 s + 7 beats × 8 s + beat 06 de 5 s + pausa congelada 3 s)
- **Formato:** vertical 768×1344, MiniMax H3 en ComfyUI

## Ficha

| Campo | Respuesta |
|---|---|
| **Deseo** | Plof quiere llenar el anillo verde vacío que hay en el suelo. |
| **Obstáculo** | Solo hay dos fichas, una azul y una amarilla; ninguna es verde y el anillo las escupe. |
| **Concepto** | Azul + amarillo = verde. Sin saberlo, el anillo no se completa. |
| **Error 01** | Plof mete la azul a la fuerza (empuja, se sube, salta encima): sale disparada. |
| **Error 02** | Clic compara y prueba la amarilla con cuidado: tampoco encaja, pero ya ha mirado los colores. |
| **Pregunta** | Clic sostiene la azul y la amarilla juntas y mira a cámara: "¿Qué pasará si las juntamos?" Pausa real de 3 s. |
| **Solución** | Las aplastan juntas → ficha verde → encaja en el anillo. "¡Verde!" |
| **Emoción** | Plof pasa de la fuerza bruta a la sorpresa; Clic de observar a actuar. Lo resuelven juntos: ninguno es el profesor. |
| **Transfer** | En casa: mezclar plastilina (o pintura) azul y amarilla. Frase para la descripción del vídeo: "¿Qué pasa si mezcláis azul y amarillo?" |
| **Callback** | Aparecen una ficha roja y otra azul; Plof las coge con cara de pillo. "¿Y rojo con azul?" → gancho para el siguiente episodio (morado). |

## 8 beats

| # | Beat | Seg. | Acción dominante | Audio / voz |
|---|---|---|---|---|
| 01 | Anomalía | 8 | Clic y Plof entran jugando y frenan en seco: en el suelo, un anillo verde vacío y dos fichas (azul, amarilla). Miran el anillo, miran las fichas, ladean la cabeza. | pasos, "¿mmm?" curioso. Sin palabras |
| 02 | Deseo | 8 | Plof señala el hueco del anillo y las fichas, se frota las manos, coge la azul y la arrastra hasta el anillo. Clic observa. | esfuerzo, risitas |
| 03 | Intento | 8 | Plof deja caer la azul en el anillo: queda torcida, no entra. Empuja, se sube encima y salta para meterla a la fuerza. Clic se tapa los ojos. | golpes blandos, boings |
| 04 | Fallo | 8 | La azul sale disparada como un muelle; Plof cae, rueda hecho bola perfecta, se desenrolla mareado. El anillo sigue vacío. Clic se ríe. | "boing", "plof", risa de Clic |
| 05 | Mejora | 8 | Clic coge la amarilla, la compara con el borde verde del anillo y la apoya encima: es más ancha que el hueco y se queda tapándolo, torcida. La retira y la deja junto a la azul. Los dos se quedan mirando las dos fichas, pensando. | silencio curioso, un "mmm" |
| 06 | Predicción | 5 + 3 | Cada uno coge una ficha, Clic la azul y Plof la amarilla, se ponen de pie uno al lado del otro y miran a cámara sin juntarlas. **Último fotograma congelado 3 s.** | voz: "¿Qué pasará si las juntamos?" + pausa en silencio |
| 07 | Solución | 8 | Se giran el uno hacia el otro y empujan sus fichas hasta fundirlas → una sola ficha verde, que amasan entre los dos hasta el tamaño del hueco. La encajan en el anillo: entra a ras. Saltan de alegría. | "squish", "ping", voz: "¡Verde!", risas |
| 08 | Eco | 8 | Entran rodando una ficha roja y otra azul, que se paran lejos del anillo. Plof las coge él solo, una en cada mano, y mira a cámara con cara de pillo; Clic se tapa la cara riendo. El anillo sigue lleno. | boings, voz: "¿Y rojo con azul? ¡Hasta el próximo Plof!" |

## Go / no-go

Rechazar si:
- [x] ~~el aprendizaje puede quitarse sin afectar a la historia~~ → sin azul + amarillo = verde no se llena el anillo
- [x] ~~más de un problema central~~ → uno: llenar el anillo
- [x] ~~la pregunta no se puede responder con lo visto~~ → el niño ha visto que ni azul ni amarilla valen y el borde es verde
- [x] ~~el error existe solo para rellenar~~ → error 01 (fuerza) y error 02 (probar la otra) llevan al concepto
- [x] ~~estímulo sin función~~ → la bola de Plof es la consecuencia del fallo
- [x] ~~el final no resuelve~~ → el anillo queda lleno

Luz verde: deseo claro, anticipación posible en el beat 06, el concepto cambia la acción, emoción legible (fuerza → sorpresa), replay (la segunda vez el niño dice "verde" antes), transferencia (mezclar en casa).

## Producción

- Focos: anillo verde + 2 fichas + 2 personajes (dentro del máximo de 3 focos semánticos: anillo, fichas, personajes).
- Objetos estables entre clips: anillo verde (plano, en el suelo) y fichas. El encadenado por `first_frame` los conserva.
## Aprendido al generar (aplicar a los siguientes episodios)

El modelo pierde objetos cuando algo **entra o sale de dentro de otra cosa**, y los inventa cuando algo **aparece de la nada**. Los dos únicos clips que hubo que repetir fallaron por esto:

- **Beat 05 (repetido):** se le pidió que la ficha amarilla entrase en el anillo y saliera rebotando. Resultado: la ficha se estiró como un chicle y quedaron dos amarillas. Solución: que **nunca llegue a entrar** (se queda apoyada encima, es más ancha que el hueco) y que **la retire un personaje**, no la física.
- **Beat 08 (repetido):** la ficha roja cayó justo delante del anillo y, al recogerla, desapareció el disco verde que lo llenaba. Solución: que los objetos nuevos **lleguen rodando y se paren lejos**, y una cláusula explícita de que el anillo y su contenido no se tocan ni cambian en todo el clip.

Reglas para los prompts, entonces:

1. Nada entra ni sale de dentro de nada. Si algo tiene que quitarse, lo quita un personaje con las manos.
2. Los objetos nuevos llegan rodando desde fuera de cuadro, no brotan del suelo.
3. Los objetos nuevos se paran lejos de lo que no queremos que se estropee.
4. Cerrar siempre con el inventario: cuántos objetos hay de cada color y qué no debe cambiar de aquí al último fotograma.
5. Cuando dos personajes se parecen, decir cuál es cuál **por su posición en el cuadro** ("B es el de la derecha").
6. Si el modelo reparte la acción entre los dos por su cuenta, mirar si no habrá mejorado la escena antes de repetirla: en el beat 06 lo hizo y quedó mejor que el guion.
7. **Todo objeto necesita tarea en todos los tramos del guion**, aunque la tarea sea "se queda quieto en su sitio, a la vista y a su tamaño". Aprendido al generar la intro de la serie (16/09/2026): cuatro pegotes de plastilina se quedaron sin instrucciones durante dos segundos del *timeline* y el modelo rellenó ese hueco **borrándolos**. Con la tarea explícita dejaron de desaparecer, aunque todavía encogen un poco.
8. **Los personajes se fijan con una imagen, no con texto.** El beat 01 de cada episodio nunca arranca de texto solo: arranca de `assets/personajes_referencia.png` con el atrezo añadido por Qwen. En todos los prompts va el bloque `prompts/serie/BLOQUE_PERSONAJES.txt`. Aprendido al ver el ep03 (01/11/2026): su beat 01 se hizo solo con texto, el modelo se inventó unos personajes distintos a los de la intro y los siete beats siguientes los heredaron. Detalle en `docs/PERSONAJES.md`.

- Riesgos: (a) el modelo no respeta la pausa → se resuelve congelando el fotograma en el montaje; (b) la voz (frases más largas que en la v1) → si no se entiende, plan B: grabar/TTS y sustituir el audio en el montaje; (c) el "encajar" en el anillo → si no se ve claro, repetir con otra semilla.
