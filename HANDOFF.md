# HANDOFF

## Última actualización
Fecha: 01/11/2026

## Estado actual

- **NUEVO (01/11/2026): personajes fijados con imagen.** Al ver el ep03 el usuario detectó que Clic y Plof no son los de la intro (el beat 01 se generó solo con texto y el modelo se los inventó). **El ep03 se queda así.** Desde el ep02, los personajes son los de la intro: referencia `assets/personajes_referencia.png` (rótulo de la intro sin letras, hecho con Qwen), ficha `docs/PERSONAJES.md`, bloque fijo `prompts/serie/BLOQUE_PERSONAJES.txt` y **regla 8**: el beat 01 nunca arranca de texto solo.

- **Serie renombrada a "Clic y Plof"** (antes "Plof"). Personajes: **Clic** (A, alto y delgado; observa, compara y piensa; antes "Tato") y **Plof** (B, bajito y redondo; se lanza, empuja y se cae). Los dos son del mismo azul y se distinguen solo por la silueta. Idea de serie: **"del plof al clic"**.
- **Público: 2-6 años.** Decidido el 16/09/2026 y ya unificado en todos los documentos, incluida la guía HTML.
- **Episodio 03 "El balón de arriba" MONTADO** (17/09/2026, 02:22): `output/ep03_el_balon_de_arriba.mp4`, **61,3 s**. Primer episodio con las duraciones nuevas, la descripción nueva de los personajes, la careta corta, el rótulo con Qwen y el cierre. 8 beats + rótulo + cierre **sin repetir ningún clip**. Ficha y registro completo en `docs/ep03_el_balon_de_arriba.md`. **Pendiente de que el usuario lo vea y oiga** (cinco frases de voz sin verificar de oído).
- **Piezas fijas de la serie ya hechas**: intro (8 s), **careta corta** (`output/v_careta_corta.mp4`, 2,2 s) y **cierre** (`output/v_cierre_final.mp4`, 3,3 s). Se reutilizan; no se regeneran.
- **Escaleta de la temporada 0 TERMINADA**: `docs/TEMPORADA_0.md`. **25 episodios** sobre la rejilla de la guía (4 motores × 6 dominios = 24 casillas, más el ep. 02 que repite casilla a propósito).
  - **Informe publicado para enseñar**: **https://clicyplof.surge.sh** (público; se abre desde cualquier dispositivo sin cuenta). Fuente en `web/index.html`; para republicar, ver `DESPLIEGUE.md`. El artefacto original de claude.ai (https://claude.ai/artifact/6S3nrhaehtpWFz612o3rfN) es privado y solo se abre con la sesión del propietario: ya no es el enlace que se comparte.
- **Intro de la serie TERMINADA**: `output/v_intro_cp2_00001_.mp4` (8 s, 768×1344). Revisada y aprobada. Se reutiliza siempre; no se regenera.
  - Rótulo (fotograma final): `output/v_rotulo_cp2_00001_.png`
  - Pegotes (fotograma inicial): `output/v_intro_inicio2_00001_.png`
  - Prompts en `prompts/serie/`, todo con semilla **20260916**.
- **Episodio 01 "Los colores" montado**: `output/plof_ep01_v2.mp4` (71,7 s). **Lleva la marca antigua** (rótulo "PLOF", intro vieja): hay que volver a montarlo antes de publicarlo.
- **Validado con un niño real (15/09/2026)**: un niño con TDAH lo vio entero sin despegar los ojos y quiso repetirlo. Es **una sola prueba**; faltan 2-3 niños más.
- ComfyUI debe estar arrancado en `http://127.0.0.1:8188`.

## Estructura fija de un episodio (decidida hoy)

| Pieza | Duración | Cómo se hace |
|---|---|---|
| Careta corta | 2-3 s | Recorte del final de la intro. **La intro completa de 8 s NO abre los Shorts** |
| Rótulo del episodio | 3 s | Título en letras de plastilina **y dicho por la narradora**. Imagen fija con Qwen, voz pedida en el clip |
| 8 beats | **52 s**: 5 s Anomalía, Deseo, Mejora, Predicción (+3 s de pausa) y Eco; 8 s Intento, Fallo y Solución | Secuencia de la guía intacta; **duración por beat decidida el 16/09/2026** (`docs/DECISION_DURACION_CLIPS.md`). Un clip por beat, nunca dos |
| Cierre | 3 s | **Siempre el mismo clip**: Clic y Plof abrazados saludando, y un círculo que se cierra sobre ellos. Prompt `prompts/serie/cierre.txt` + `herramientas/cerrar_iris.py`. **Generado el 16/09/2026**: `output/v_cierre_final.mp4` (3,3 s). Pendiente de que el usuario apruebe el audio |

**Total ≈ 61 s** para Shorts. El ep. 01 se produjo con 8 × 8 s y se queda así. Las recopilaciones llevan la intro completa de 8 s una sola vez al principio.

## Completado en esta sesión (01/11/2026)

- Diagnóstico de la diferencia de personajes entre intro y ep03 (fotogramas comparados): cabezas pequeñas, Clic como un palo, Plof como un bulto, azul más oscuro. Causa: beat 01 con `tropiezo_t2v.json`. Además, los prompts decían que Plof mide "la mitad" de Clic; en la intro mide **≈ 2/3**.
- **`assets/personajes_referencia.png`** generada con Qwen desde `output/v_rotulo_cp2_00001_.png` (`prompts/serie/personajes_referencia.txt`, semilla 20260916, 30 s, buena a la primera; diferencia media con el original en la zona de los muñecos: 2,3/255). Aprobada por el usuario.
- **`docs/PERSONAJES.md`** (ficha de personajes con medidas y color medido) y **`prompts/serie/BLOQUE_PERSONAJES.txt`**.
- **Regla 8** en `docs/ep01_los_colores.md`; plantilla de ficha, `FICHA_TECNICA.md` (flujo, paso 5) y ficha del ep03 (nota de aceptación) actualizadas.

## Completado en la sesión anterior (16-17/09/2026)

- Análisis completo del proyecto, verificando los vídeos con PyAV en vez de fiarse de la documentación.
- **Nombres nuevos comprobados**: libres `@clicyplof`, `@clicplof`, `@plofyclic`. Descartados "Pim" (choca con *Plim Plim*, serie preescolar argentina de Disney Junior) y "Tic" (se confunde con TikTok). Detalle en `PLAN_NEGOCIO.md` § 9.1.
- **Intro nueva completa**: personajes de cuerpo entero, gag de Clic apoyándose en la cabeza de Plof, baile, y letras que llegan como pegotes y se forman al llegar. Generada dos veces (la primera perdía objetos).
- **Método nuevo para el fotograma inicial**: Qwen Image Edit convierte las letras del rótulo en pegotes informes conservando a los personajes intactos. Sustituye a `desordenar_letras.py`.
- **Escaleta de la temporada 0** (`docs/TEMPORADA_0.md`) y su informe publicado.
- **`prompts/serie/BLOQUE_PLASTILINA.txt`**: el bloque de texto fijo que va en todos los prompts para que la plastilina se comporte como plastilina.
- **RealESRGAN_x2plus** instalado en ComfyUI y detectado.
- Documentación entera actualizada: `README.md` (reescrito), `FICHA_TECNICA.md`, `DESPLIEGUE.md`, `PLAN_NEGOCIO.md`, `docs/ep01_los_colores.md`, `docs/PLANTILLA_FICHA_EPISODIO.md`.
- **Biblia de temporada publicada en Surge**: el artefacto de claude.ai no se abría desde otros dispositivos por ser privado. Se guardó su HTML en `web/index.html` (estructura `<head>`/`<body>` correcta, `lang="es"`, favicon) y se subió a **https://clicyplof.surge.sh** (comprobado: HTTP 200). Documentado en `DESPLIEGUE.md` y `FICHA_TECNICA.md`.
- **Análisis de motor fijo, calidad y duración de clips** guardado en `docs/DECISION_DURACION_CLIPS.md` (con los tiempos medidos de la máquina). **Decisión tomada: duración mixta por beat** (5 s / 8 s), aplicada en `TEMPORADA_0.md`, la plantilla de ficha, `README.md`, `FICHA_TECNICA.md` y la web.
- **Cierre de la serie preparado**: `prompts/serie/cierre.txt` (arranca del fotograma final de la intro; abrazo de lado y saludo a cámara, 3 s) y `herramientas/cerrar_iris.py` (círculo que se cierra, con borde suavizado, cola de color liso y audio conservado). **Clip generado** (6 min 31 s de GPU, semilla 20260916): `output/v_cierre_00001_.mp4` (bruto, 73 fotogramas) → `output/v_cierre_final.mp4` (con círculo y 0,25 s de negro, 79 fotogramas = 3,3 s). Bueno a la primera; pendiente solo de oír el audio.
- **Episodio 03 "El balón de arriba" completo**: ficha (`docs/ep03_el_balon_de_arriba.md`), 8 prompts + rótulo (`prompts/ep03/`), 8 beats generados y aceptados sin repetir ninguno, rótulo con Qwen (a la segunda ronda: la primera escribió "BALÓ-N / ARRIBATA"), careta corta recortada de la intro, y montaje de 61,3 s. Decisión de guion: "lo que hay que subirse" es Plof hecho bola (sin cuarto objeto; paga el gag de la intro).
- **Método nuevo para rótulos con tilde**: además del prompt de texto, se probó dar a Qwen un lienzo con el título ya escrito (Pillow, fuente Comic Sans Bold) para que solo cambie el material. Funcionó en ortografía (vía B) pero con letras finas; ganó el prompt de texto endurecido con recuento de letras (vía A). Las dos vías quedan en `prompts/ep03/`.
- **Incidente de memoria documentado** (ver "Problemas conocidos").

## Próximos pasos

0. **Continuar el plan con el ep02 "El morado" aplicando el método nuevo de personajes** (`docs/PERSONAJES.md` § "Cómo se usa" y § "Pendiente de comprobar"): primer episodio con arranque desde la referencia. Vigilar que Qwen no retoque a los personajes al añadir el atrezo y resolver la postura inicial (la referencia los tiene abrazados).
1. **Ver y oír `output/ep03_el_balon_de_arriba.mp4`** y decidir: (a) las cinco frases de voz (careta "¡Clic y Plof!", rótulo "El balón de arriba", beat 06 "¿Cómo puede llegar Clic al balón?", beat 07 "¡Arriba!", cierre "¡Adiós!"); (b) si el beat 08 se repite con otra semilla (Clic y Plof se ven como un bulto un tercio de segundo al soltar el balón; 13 min); (c) si el final del cierre convence (círculo a negro, 0,75 s de silencio).
2. **PENDIENTE DE CONVERSACIÓN: la estrategia de venta.** El usuario la dejó abierta. Hay que decidir a qué llama vender antes de escribirla, porque el catálogo a producir cambia:
   - *Hacer caja con el canal* (audiencia + publicidad). Ojo: en contenido infantil la publicidad personalizada está prohibida y eso hunde el RPM.
   - *Colocar la serie* a una productora o plataforma (negocio de relaciones; que esté generada con IA es hoy un obstáculo real).
   - *Vender a los padres* el método y los materiales (mejor margen; la guía ya lo apunta con la capa de canal para adultos).
3. **Mejora propuesta, no implementada: limpiar el reflejo azulado del suelo en `herramientas/fondo.py`.** En todos los beats del ep03 el suelo quedaba con un tinte azul tenue donde pisa Plof; se limpió a mano en cada fotograma de arranque con la regla "píxel claro (R y G > 150) con B > R + 8 → blanco". Si se mete en `fondo.py`, se aplica sola en los enlaces y en el montaje. Cambio de 3 líneas; pedir aprobación.
4. **Volver a montar el episodio 01** con careta corta, rótulo nuevo (hay que hacerlo: el actual dice "PLOF") y cierre. No cuesta GPU salvo el rótulo (Qwen, 30 s + clip de 3 s).
5. **Episodio 02 "El morado"**: ficha con la plantilla (duraciones ya rellenas), reglas de `docs/ep01_los_colores.md` § "Aprendido al generar" y bloque de plastilina. Publicar el 02 detrás del 01 (el 01 termina prometiendo "¿y rojo con azul?"); el 03 puede ir después.
6. **Terminar de instalar `faster-whisper`** (ver "Problemas conocidos"). Serviría para verificar las voces sin oírlas una a una.
7. **Reservar `@clicyplof`** en YouTube y **comprobar "CLIC Y PLOF" en TMview** a mano (clases 41, 9, 16, 28).
8. **Prueba de calidad sin el LoRA turbo** en un clip de 3 s (~20 min).
9. **Mejoras de calidad ya diagnosticadas**: (a) guardar el fotograma de enlace como PNG sin comprimir desde el workflow; (b) recortar a 756×1344 (9:16 exacto) y reescalar a 1080×1920 en el montaje.
10. **Poner el proyecto en git.** Lo irremplazable son ~200 KB de texto; `output/` y `.venv-voz/` al `.gitignore`.
11. Decidir si se renombra `docs/TATO_PLOF_VANGUARDIA_EDUCATIVA_PLAN.html`, que conserva los nombres antiguos dentro y en el nombre del archivo (lo referencian otros cuatro documentos).

## Decisiones tomadas

- **(01/11/2026) Los personajes canónicos son los de la intro**, fijados con la imagen `assets/personajes_referencia.png`; si texto e imagen no coinciden, manda la imagen. El ep03 se acepta con los personajes desviados. Ningún beat 01 vuelve a arrancar de texto solo (regla 8).

- **Nombre "Clic y Plof"**, con los dos personajes en el título. *Clic* es el momento de entender y el sonido de dos piezas encajando; *Plof* es el error blando y la caída.
- **Edad 2-6**, servida por capas: la comedia física para los de 2-3, el problema visual para los de 3-4, la pausa de predicción para los de 5-6.
- **Quién resuelve, equilibrado a propósito: Clic 8, Plof 8, los dos 9.** La mecánica es *Plof se lanza y la lía; al liarla pasa algo que Clic ve, y esa es la pista*. En los ocho de Plof la respuesta correcta es la fuerza. En el dominio de emoción, dos veces se descompone Plof y dos veces Clic: si los cuatro fueran de Plof, quedaría como el niño problemático y Clic como el adulto sereno.
- **Todo es plastilina y se comporta como tal**, con deformación **elástica**: se aplasta y vuelve a la misma forma, tamaño y color. Si se pide deformación libre, el modelo estira sin control y pierde o duplica objetos (fallo del beat 05 del ep01). Bloque fijo en `prompts/serie/BLOQUE_PLASTILINA.txt`.
- **El atrezo de plastilina entra** (árbol, muro, rampa, banqueta, cuenco, alfombra), siempre de plastilina y sin paisaje ni decorado.
- **Careta corta en Shorts, intro completa en recopilaciones.**
- **Duración por beat, no 8 s fijos** (16/09/2026): 5 s los beats de situación, 8 s los tres de acción. Se conserva la *secuencia* de los ocho beats (es lo que hace que el niño reconozca el formato y se adelante en la pausa), no su duración. Motivo: los clips cortos fallan menos y cuestan menos al fallar; el episodio baja de 3,2 h a ≈ 2,3 h de GPU. **Nunca partir un beat en dos clips.** Ver `docs/DECISION_DURACION_CLIPS.md`.
- **La descripción de los personajes en los prompts de episodio es la de la intro y el cierre** (Clic alto y delgado "como una salchicha estirada", Plof bola "casi tan ancho como alto", cuerpo entero), no la del ep01 ("A ligeramente más alto"). Así los beats casan con careta y cierre.
- **Reflejo azulado del suelo**: se limpia en cada fotograma de arranque (a mano en el ep03; propuesto para `fondo.py`).
- **Cierre fijo de 3 s en todos los episodios**: los dos abrazados saludando y un círculo que se cierra (iris). El círculo se hace en el montaje con `cerrar_iris.py`, no se le pide al modelo: así sale idéntico siempre.
- **Regla de prompt nueva (la 7ª)**: **todo objeto necesita tarea en todos los tramos del guion**, aunque sea "se queda quieto, a la vista y a su tamaño". En la primera intro, cuatro pegotes se quedaron dos segundos sin instrucciones y el modelo los borró.
- Letras del rótulo pegadas a la pared, no de pie en el suelo. **Ninguna letra azul.**
- **Los prompts de `prompts/ep01/` NO se renombran**: son el registro de lo que produjo los clips existentes.
- **Instalaciones y generaciones no se solapan**: durante una generación quedan <5 GB libres de 64 GB de RAM y el sistema mata procesos.
- **No se instalan nodos de terceros en ComfyUI**: la instalación es 100 % núcleo (928 nodos). Descartadas la interpolación de fotogramas (quitaría el aire de stop-motion) y los packs de vídeo (duplican lo que ya hace `herramientas/`).

## Problemas conocidos

- **TRAMPA DE RESOLUCIÓN (01/11/2026): `workflow/clip_i2v.json` genera a 480×864 si no se pasa `--tamano 768x1344`.** La primera pasada del ep02 salió entera a 480×864 por esto. Pasarlo SIEMPRE en los clips de la serie. Señal de alarma: un clip de 5 s que tarda 3-4 min en vez de ~13.
- **Deriva del azul al encadenar: corregida con `ultimo_fotograma.py --corregir-azul`** (01/11/2026), que lleva el azul de los muñecos del fotograma de enlace al de la referencia (RGB 25,128,202). Usar siempre junto a `--limpiar-fondo`.

- **`faster-whisper` NO se llegó a instalar.** El entorno `.venv-voz/` está creado y su `pip` funciona (instaló `six` en segundos como prueba), pero `pip install faster-whisper` lleva más de 10 minutos sin completarse ni dar error. Comando exacto:
  `cd D:\CLAUDE\PLASTI && PYTHONUNBUFFERED=1 .venv-voz\Scripts\python.exe -m pip install faster-whisper`
  Si vuelve a colgarse, probar `--only-binary :all:` o fijar versiones de `ctranslate2`. **Lanzar la salida sin tubería y con `PYTHONUNBUFFERED=1`**: sin eso Python acumula la salida en bloques y parece colgado cuando no lo está (perdí tres intentos por esto).
- **Los juegos y otros programas pesados matan la generación de 8 s.** El 17/09 el beat 07 tardó ≈ 70 min en vez de 25 porque había un juego abierto (Timberborn, 7,3 GB) más Steam, Epic y un capturador: el sistema mandó el modelo de ComfyUI al archivo de paginación (36 GB reservados, 0,7 GB residentes) y el proceso de espera de `generar_video.py` fue matado a los 20 min. ComfyUI terminó igualmente y el vídeo se recogió con `--esperar <id>`. Regla: **durante un beat de 8 s, nada más abierto**. Si el proceso de espera muere, el trabajo sigue en ComfyUI: `curl http://127.0.0.1:8188/history/<id>` dice si ha acabado y `--esperar <id>` lo descarga.
- **Calidad de imagen.** Por orden de coste: (1) se publica a 768×1344 cuando Shorts trabaja a 1080×1920, y además 768×1344 **no es 9:16 exacto** (0,571 frente a 0,5625); (2) pérdida por generación en cadena, porque el fotograma de enlace sale de un mp4 comprimido — se confirma al ver que la intro, que arranca de un PNG limpio, se ve mejor que los beats encadenados; (3) el LoRA turbo de 8 pasos; (4) `FUERZA = 0.85` en `fondo.py` puede aplanar la textura.
- **Qwen reparte mal los colores** con cuatro letras seguidas: pinta dos contiguas del mismo color pase lo que pase (dos intentos, dos colores distintos, mismo fallo). En el rótulo bueno la P y la L son las dos rojas. La vía no es el prompt sino tirar semillas y elegir.
- **La intro buena todavía encoge los pegotes** entre el segundo 3,6 y el 4,3 antes de convertirlos en letras. Defecto menor, aceptado.
- Tiempos a 768×1344: 5 s ≈ 13 min, 8 s ≈ 21-25 min. Un episodio ≈ 3 h de GPU.
- La voz de MiniMax llega 1-2 s tarde respecto al momento pedido: se compensa pidiéndola antes.
- El azul de los muñecos se oscurece al encadenar clips; no corregido.
- Los clips que arrancan de imagen compuesta saltan en los 8 primeros fotogramas: `@saltar=8`.
- El proyecto no está en git.

## Archivos modificados en esta sesión (01/11/2026)

- **Nuevos:** `assets/personajes_referencia.png`, `output/personajes_referencia_00001_.png`, `docs/PERSONAJES.md`, `prompts/serie/BLOQUE_PERSONAJES.txt`, `prompts/serie/personajes_referencia.txt`
- **Modificados:** `docs/ep01_los_colores.md` (regla 8), `docs/PLANTILLA_FICHA_EPISODIO.md`, `docs/ep03_el_balon_de_arriba.md` (nota), `FICHA_TECNICA.md` (paso 5 del flujo), `HANDOFF.md`

## Archivos modificados en la sesión anterior (16-17/09/2026)

- **Nuevos (17/09):** `docs/ep03_el_balon_de_arriba.md`, `prompts/ep03/` (8 beats, `rotulo.txt`, `rotulo_desde_lienzo.txt`, `rotulo_clip.txt`), `assets/ep03_arranque_beat02..08.png`, `assets/ep03_rotulo_lienzo*.png`, `output/ep03_*` (8 beats, rótulo png y clip, 4 pruebas de rótulo), `output/v_careta_corta.mp4`, **`output/ep03_el_balon_de_arriba.mp4`**
- **Nuevos:** `docs/TEMPORADA_0.md`, `prompts/serie/` (`rotulo.txt`, `intro_inicio.txt`, `intro.txt`, `BLOQUE_PLASTILINA.txt`), `.venv-voz/`, **`web/`** (`index.html`, `CNAME`: la biblia publicada en Surge), `docs/DECISION_DURACION_CLIPS.md`, `prompts/serie/cierre.txt`, `herramientas/cerrar_iris.py`
- **Reescritos:** `README.md`, `HANDOFF.md`
- **Modificados:** `FICHA_TECNICA.md`, `DESPLIEGUE.md`, `PLAN_NEGOCIO.md`, `docs/ep01_los_colores.md`, `docs/PLANTILLA_FICHA_EPISODIO.md`, `docs/TATO_PLOF_VANGUARDIA_EDUCATIVA_PLAN.html` (solo la edad)
- **Salidas nuevas:** **`output/v_cierre_00001_.mp4` y `output/v_cierre_final.mp4` (cierre de la serie)**, `output/v_rotulo_cp2_00001_.png` (rótulo bueno), `v_intro_inicio2_00001_.png` (primer fotograma bueno), **`v_intro_cp2_00001_.mp4` (intro buena)**, más los descartes `v_rotulo_cp`, `v_rotulo_cp3`, `v_intro_inicio`, `v_intro_cp` y las tiras `revision_intro_cp.png`, `revision_intro_cp2.png`
- **Fuera del proyecto:** `D:\Comfy-Desktop\ComfyUI-Shared\models\upscale_models\RealESRGAN_x2plus.pth`
