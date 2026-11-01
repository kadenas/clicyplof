# PLAN DE NEGOCIO — Serie de plastilina para entretenimiento y aprendizaje infantil

**Nombre de la serie:** Plof (decidido el 14/09/2026)
**Personajes:** Clic (alto y delgado, el que observa y piensa) y Plof (bajito y redondo, el que se lanza y se cae)
**Nombre interno del proyecto:** PLASTI (carpeta, scripts y rótulo actual)
**Autor:** JMR Studio
**Fecha:** 14/09/2026

---

## Resumen ejecutivo

Clic y Plof (nombre interno del proyecto: PLASTI) es una serie corta de animación de plastilina (claymation, generada con IA local) protagonizada por dos muñecos azules, Clic y Plof, pensada para niños de **2 a 6 años**. Combina humor físico sencillo (tropezones, persecuciones, juegos) con un **micro-aprendizaje** de vocabulario básico, colores y números en español, mediante diálogos muy cortos y repetitivos.

- **Mercado inicial:** España, audiencia hispanohablante, en YouTube (canal + Shorts).
- **Monetización inicial:** publicidad de YouTube (Programa de Socios), ampliable más adelante si el canal crece.
- **Ventaja competitiva real:** el coste marginal de producción es casi cero. Ya tienes un pipeline local (ComfyUI + MiniMax H3, RTX 4060 Ti) que genera clips de 8 s y los monta en capítulos, sin depender de estudios de animación ni presupuestos de producción tradicionales. Eso es lo que hace viable este proyecto en solitario y a tiempo parcial — ningún competidor tradicional (Pocoyo, Bluey, Cocomelon) puede producir a este coste.
- **Recursos:** proyecto en solitario, tiempo parcial, sin presupuesto externo por ahora.
- **Riesgos más importantes a resolver ANTES de publicar:** dos, ambos de impacto alto: (a) la política de "contenido no auténtico" de YouTube, que apunta directamente a canales infantiles generados con IA (sección 8), y (b) el parecido con Pocoyo, porque hoy los dos muñecos son azules sobre fondo blanco (sección 9; la mención "estilo Pocoyo" del README ya se ha eliminado el 14/09/2026).
- **Siguiente paso concreto:** completar el pipeline de voz + subtítulos (ya lo tenías anotado como próximo paso técnico), producir 5-8 episodios piloto en formato Shorts (60-90 s) antes de abrir el canal públicamente, y validar el formato pedagógico con niños reales del entorno cercano.

---

## 1. El proyecto

Dos personajes de plastilina, generados y animados con modelos de IA de vídeo (MiniMax H3) en ComfyUI, sobre fondo blanco, en formato vertical 9:16. Ya existe un capítulo piloto montado (`capitulo_01.mp4`, 31,7 s) con intro, gags físicos y cierre.

La idea de negocio añade una capa pedagógica a lo que hoy es un experimento técnico: convertir los gags en pequeñas lecciones de idioma para niños pequeños (palabras, colores, números), usando diálogos deliberadamente simples.

## 2. Producto: la serie

### 2.1 Formato de episodio

Recomendación: episodios **cortos (60-90 segundos)**, no capítulos largos tipo el actual de 31,7 s ampliado. Motivos:
- Encajan directamente en **YouTube Shorts**, que tiene su propio criterio de monetización (ver sección 8) y es más fácil de viralizar para un canal nuevo sin audiencia previa.
- Reducen el riesgo de "deriva de color/fondo" que ya detectaste al encadenar clips largos.
- Permiten publicar con más frecuencia sin agotar el tiempo disponible (tiempo parcial).

### 2.2 Estructura pedagógica de cada episodio (recomendada)

Los programas infantiles de éxito (Pocoyo, Bluey, Peppa Pig) usan **rituales repetidos**: los niños pequeños aprenden por repetición y previsibilidad. Propuesta de estructura fija, reutilizable en cada episodio (y que además reduce el trabajo de producción, porque la intro/cierre se reutilizan):

1. **Saludo ritual** (misma frase siempre — "¡Hola!") — ya tienes la intro con rótulo hecha.
2. **Palabra o color del día**, repetido 3-4 veces con refuerzo visual (el objeto señalado, el color mostrado).
3. **Mini-gag físico** (el humor que ya sabes generar: tropiezos, persecuciones, juegos) que usa esa palabra/color en contexto.
4. **Cierre con conteo** (número del día, contado en voz alta) y despedida ritual.

Esto convierte cada episodio en una "unidad de aprendizaje" reconocible, y de paso te da una plantilla de producción fija (menos decisiones creativas por episodio = más velocidad).

## 3. Propuesta de valor

- **Para los niños:** entretenimiento físico y visual simple, con aprendizaje incidental de vocabulario, colores y números.
- **Para los padres:** contenido breve, en español, sin violencia, con valor educativo explícito — un argumento de venta frente a contenido puramente de entretenimiento (tipo Cocomelon, criticado por sobreestimulación).
- **Diferencial de producción:** estética claymation (world-building físico, no dibujo plano) generada con IA, algo poco explotado todavía en el nicho educativo infantil en español.

## 4. Mercado y audiencia

- **Audiencia primaria:** niños de 2-6 años en España.
- **Audiencia real que decide (comprador/gatekeeper):** padres y madres de niños en esa franja, que buscan contenido "con propósito" en YouTube.
- **Canal de distribución inicial:** YouTube (canal dedicado + Shorts). No se descarta Instagram/TikTok como canales secundarios de promoción, pero el foco de monetización es YouTube.

## 5. Competencia

| Referencia | Formato | Punto fuerte | Hueco que dejan |
|---|---|---|---|
| Pocoyo | Serie 3D, larga trayectoria | Producción y marca consolidadas | Sin foco explícito en vocabulario/números |
| Cocomelon | 3D, canciones | Algoritmo, repetición | Criticado por sobreestimulación, sin foco en español de España |
| Masha y el Oso | 3D | Humor físico | No es educativo, ruso/doblado |
| Bluey | 2D | Calidad narrativa | Público algo mayor (4-8), no enfocado a vocabulario básico |
| Canales de "aprende inglés/español para niños" | Animación simple o stock | Foco educativo puro | Poca producción, poco entretenimiento, aburridos |

**Hueco identificado:** claymation con humor físico + estructura pedagógica explícita de vocabulario/colores/números, en español de España, con episodios cortos tipo Shorts. Es un nicho concreto, no un océano azul gigante, pero es defendible para un creador solo.

## 6. Modelo de producción (la ventaja competitiva real)

Esto es lo que hace que el plan sea viable para una persona sola a tiempo parcial, y por tanto merece ser el eje del plan de negocio, no un detalle técnico:

- Generación local con ComfyUI + MiniMax H3 (RTX 4060 Ti 16 GB), sin coste por clip más allá de electricidad y tiempo de máquina.
- Pipeline ya probado: intro con rótulo, clips encadenados por `first_frame`, montaje con limpieza de fondo.
- Próximo hito técnico (ya identificado por ti): voz nativa de los personajes (MiniMax H3 admite diálogo en el prompt) + subtítulos incrustados (PyAV + Pillow).
- Esto significa que el coste marginal de un episodio nuevo es, en esencia, **tiempo de tu parte** (escribir el prompt/guion, generar, revisar, montar), no dinero. Es la base de que este proyecto pueda sostenerse en solitario y a tiempo parcial.

## 7. Modelo de negocio y monetización

### Fase 1 (la que has elegido para empezar): YouTube Ads
- Ingresos vía Programa de Socios de YouTube (ver requisitos en sección 8).
- Cero inversión en herramientas nuevas: usas lo que ya tienes.
- Métrica de éxito: suscriptores, horas de visualización / vistas de Shorts, retención.

### Fase 2 (no ahora, pero a tener en el radar si el canal funciona)
- Patrocinios de marcas de productos infantiles.
- App o web complementaria con ejercicios (vocabulario, colores, números) ligados a cada episodio — coherente con tu perfil, ya que trabajas con Vite/React/Capacitor en otros proyectos.
- Merchandising (muy a largo plazo, solo si hay marca y audiencia consolidadas).

No recomiendo diseñar Fase 2 en detalle todavía: sin audiencia, cualquier proyección de patrocinios o app es especulativa. Mejor validar Fase 1 primero.

## 8. Requisitos y reglas de YouTube que afectan directamente al plan

- **Programa de Socios de YouTube (monetización):** tiene **dos niveles** y conviene no confundirlos:
  - *Nivel bajo* (500 suscriptores, 3 vídeos públicos en los últimos 90 días y 3.000 horas de visualización en 12 meses **o** 3 millones de vistas de Shorts en 90 días): solo desbloquea membresías, Super Thanks, Super Chat y tienda. **No sirve para este proyecto:** esas funciones están desactivadas en contenido "hecho para niños".
  - *Nivel de ingresos por publicidad* (el que necesita la Fase 1): **1.000 suscriptores** y **4.000 horas válidas de visualización pública en 12 meses o 10 millones de vistas válidas de Shorts en 90 días**.
  - Consecuencia: 10 millones de vistas de Shorts en 90 días es una barrera altísima para un canal nuevo, y además el ingreso por mil vistas de Shorts es una fracción del de los vídeos largos. En cambio, el contenido infantil es de los que más horas de visualización acumula (los niños ven en bucle, en tele o tablet). El camino realista para monetizar un canal infantil es **horas de visualización de vídeos largos**, con los Shorts como herramienta de descubrimiento, no como producto principal. Esto pesa en la decisión de formato de la sección 2.1 (pendiente: vertical, horizontal o ambos).
  - Cifras según las condiciones conocidas a septiembre de 2026; comprobarlas en la página oficial del Programa de Socios antes de solicitar la monetización, porque cambian.
- **Política de "contenido no auténtico" (antes "contenido repetitivo") — el riesgo principal para este canal:** desde julio de 2025 YouTube desmonetiza canales cuyo contenido considera producido en masa o repetitivo, y los canales infantiles generados con IA son justo el tipo de contenido al que apunta esa política. La plantilla fija de episodio (sección 2.2) más la generación por IA pueden hacer que el canal parezca "contenido en serie" si no hay aportación humana visible en cada episodio. Mitigación: guion propio y distinto en cada episodio (no cambiar solo la palabra del día), voz y narración con intención (no texto leído por máquina sin más), gags diferentes y no publicar en masa. Conviene guardar guiones y decisiones de cada episodio por si YouTube pide justificación en una revisión.
- **Contenido "hecho para niños" ("Made for Kids"):** YouTube obliga a marcar el canal/vídeos como contenido infantil si va dirigido a niños. Esto **desactiva** ciertas funciones (comentarios, notificaciones personalizadas, algunos tipos de anuncios) y cambia el tipo de publicidad disponible (más limitada, sin personalización basada en datos del usuario). Hay que contarlo con esto en las proyecciones de ingresos: el RPM (ingreso por mil impresiones) de contenido infantil suele ser más bajo que el de canales generalistas.
- **Divulgación de contenido sintético/generado por IA:** YouTube exige declarar cuándo un vídeo contiene contenido "alterado o sintético" que pueda parecer realista (personas, voces, escenas realistas). Los muñecos de plastilina generados por IA probablemente no encajan en el supuesto más estricto (no son personas reales ni voces clonadas de alguien real), pero conviene revisar la política vigente antes de escalar el canal, porque las reglas de IA en YouTube cambian con frecuencia.

## 9. Riesgo legal: similitud con Pocoyo — IMPORTANTE

Pocoyo es una marca registrada y un personaje con derechos de autor y de marca propiedad de Zinkia Entertainment. Si el diseño de los personajes se parece demasiado a Pocoyo (silueta, proporciones, color, forma de la cabeza, gorro/ropa), existe riesgo real de:

- Reclamación por infracción de derechos de autor o de marca si el canal gana visibilidad.
- Retirada de contenido (Content ID / DMCA) en YouTube.
- Bloqueo total de la posibilidad de licenciar o monetizar la serie más adelante (un comprador o plataforma no tocará un producto con ese riesgo).

**Situación real (revisada el 14/09/2026):**
- La frase "estilo Pocoyo" solo aparecía en el `README.md` y se ha eliminado. No debe usarse nunca en títulos, descripciones ni etiquetas del canal: sería la prueba más fácil de "inspiración directa" en una reclamación.
- Los prompts (`prompts/tropiezo.txt`) no mencionan a Pocoyo y describen figuras genéricas: bolas de plastilina azul, cabeza redonda, ojos de punto, sin gorro ni ropa. Lo que define visualmente a Pocoyo (gorro y ropa azules, cuerpo liso de 3D, fondo blanco) coincide solo en el color y el fondo blanco, que no son protegibles por sí solos. El riesgo real está en que **ambos muñecos sean azules sobre blanco con la misma silueta infantil**.

**Decisiones de diseño (14/09/2026):**
1. **Los dos protagonistas siguen siendo azules** (decisión del autor: "la serie de los muñecos azules"). Los demás colores se reservan para personajes futuros (por ejemplo, los mayores tirando a rojo). El rótulo de la intro llevará letras de colores.
   - Queda pendiente comprobar en la prueba con niños reales (sección 10, Fase 1) si distinguen a Clic de Plof solo por la altura y la forma. Si no, la palanca barata es usar **dos tonos de azul** (Clic oscuro, Plof claro) sin cambiar la identidad de la serie.
2. Mantener la textura de plastilina real (huellas, imperfecciones): es el mayor diferenciador frente al 3D limpio de Pocoyo.
3. Nunca añadir gorro ni ropa azules.
4. Nombres decididos (16/09/2026): **Clic** y **Plof**; la serie se titula **"Clic y Plof"**. Usarlos siempre en títulos, descripciones y etiquetas del canal.

### 9.1 Comprobación del nombre (14/09/2026 y 16/09/2026)

**Comprobación de "Plof" (14/09/2026):**

- **YouTube:** `@plof` está cogido (canal de coches, sin relación). Libres en esa fecha: `@PlofSerie`, `@TatoyPlof`, `@PlofTV`. Reservar uno al crear el canal.
- **Marca:** en búsquedas web no aparece ninguna marca "PLOF" en entretenimiento infantil. TMview no admite consultas automáticas; **pendiente comprobar a mano** en https://www.tmdn.org/tmview buscando "PLOF" en las clases 41 (entretenimiento), 9 (apps y contenido digital), 16 (libros) y 28 (juguetes), antes de generar rótulos definitivos.
- Único parecido encontrado: "Plif, Plaf, Plof", libro infantil traducido (Editorial Molino, 1994), descatalogado. Irrelevante.
- "Pino" (primer nombre descartado para el personaje A) chocaba con un personaje infantil sueco del mismo nombre. Se pasó a "Tato", y el 16/09/2026 a **"Clic"** (ver más abajo).

**Comprobación de "Clic y Plof" (16/09/2026):**

Se pasó a un título con los dos nombres (modelo *Tom y Jerry*, *Rick y Morty*). Nombres evaluados y resultado:

| Opción | Handles | Veredicto |
|---|---|---|
| **Clic y Plof** | `@clicyplof`, `@clicplof`, `@plofyclic`, `@clicyploftv` **libres** | **ELEGIDA**. Sin colisiones. *Clic* = el momento de entender y el sonido de dos piezas encajando; *Plof* = el error blando y la caída. La serie va "del plof al clic" |
| Pim y Plof | `@pimyplof` libre, `@pimplof` **cogido** | **Descartada**: choca con *Plim Plim*, serie preescolar argentina emitida en Disney Junior para toda Latinoamérica. Mismo idioma, misma edad, mismo nicho |
| Tic y Plof | `@ticyplof`, `@ticplof` libres | **Descartada**: se confunde con TikTok en las búsquedas, y existe *Tik Tak* (serie preescolar belga) |
| Tin y Bombo | `@tinbombo`, `@tinybombo` libres | Descartada: obligaba a cambiar los dos nombres y a perder "Plof", que ya funciona |

- Control de la comprobación: `@plof` da canal real (cogido) y `@TatoyPlof` da 404 (libre), coincidiendo con lo medido el 14/09. El método distingue bien.
- Precedentes en plastilina, sin conflicto para el español: *Plonsters* (1987, personajes Plif, Plops y Plummy) y el Kabouter Plop belga (Studio 100).
- **PENDIENTE: comprobar "CLIC Y PLOF" a mano en TMview** (clases 41, 9, 16 y 28). Que el handle esté libre no dice nada sobre la marca.
- **PENDIENTE: reservar `@clicyplof`** en YouTube. Es gratis e inmediato y es la única forma real de quedárselo.

## 10. Hoja de ruta

**Fase 0 — Completada:** pipeline técnico funcionando, capítulo 1 piloto montado.

**Fase 1 — Preparación (próximas semanas, tiempo parcial):**
1. Diferenciación respecto a Pocoyo: nombres y colores decididos (sección 9); queda comprobar la marca "PLOF" en TMview (sección 9.1) y decidir el formato de vídeo.
2. Completar pipeline de voz (diálogo simple en español vía MiniMax H3) + subtítulos incrustados.
3. Definir la plantilla fija de episodio (saludo / palabra o color del día / gag / conteo y despedida — sección 2.2).
4. Producir 5-8 episodios piloto cortos (60-90 s) sin publicar todavía.
5. Probarlos con niños reales del entorno cercano (sobrinos, hijos de amigos, etc.) para validar si entienden y repiten las palabras/colores — esto es más valioso que cualquier proyección teórica.

**Fase 2 — Lanzamiento:**
6. Crear el canal de YouTube, marcarlo correctamente como contenido infantil.
7. Publicar los episodios piloto ya validados, con calendario sostenible (mejor 1-2 por semana de forma constante que muchos al principio y luego parar).
8. Medir retención y repetición de vocabulario en comentarios/feedback de padres.

**Fase 3 — Crecimiento:**
9. Ajustar formato según qué episodios funcionan mejor (palabra/color/número, tipo de gag).
10. Evaluar si se cumplen los requisitos del Programa de Socios y solicitar monetización.

**Fase 4 — Diversificación (solo si Fase 3 funciona):**
11. Explorar patrocinios, app complementaria u otros formatos (sección 7, Fase 2 del modelo de negocio).

## 11. Recursos y costes

| Recurso | Situación actual | Coste |
|---|---|---|
| Hardware (RTX 4060 Ti, 64 GB RAM) | Ya disponible | 0 € adicional |
| Software (ComfyUI, modelos) | Ya instalado y probado | 0 € adicional |
| Tiempo de producción | Tú, a tiempo parcial | Coste de oportunidad (tu tiempo) |
| Electricidad (generación GPU) | Marginal | Bajo, no significativo |
| Edición/voces/subtítulos | Pendiente de completar pipeline | 0 € (herramientas ya elegidas: MiniMax H3, PyAV+Pillow) |
| Publicidad/promoción externa | No contemplada en Fase 1 | 0 € (crecimiento orgánico vía Shorts) |

El coste real de este proyecto en su fase inicial es prácticamente cero en dinero; el recurso escaso es **tu tiempo**, y el mayor riesgo de ejecución no es técnico ni financiero, sino **mantener una cadencia de publicación constante** siendo un proyecto en solitario a tiempo parcial.

## 12. Métricas de éxito (KPIs)

- **Fase piloto (antes de publicar):** ¿los niños de prueba repiten la palabra/color/número del episodio después de verlo?
- **Fase lanzamiento:** suscriptores, vistas de Shorts, retención media por vídeo.
- **Fase monetización:** cumplimiento de umbrales del Programa de Socios (sección 8), RPM real una vez monetizado.
- **Señal de producto-mercado:** comentarios de padres mencionando que el niño repite palabras o cuenta números aprendidos del vídeo (validación cualitativa, muy valiosa en contenido infantil).

## 13. Riesgos y mitigación

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Desmonetización por "contenido no auténtico" (IA + plantilla repetitiva) | Alto | Guion, voz y gags distintos en cada episodio; aportación humana visible; no publicar en masa (sección 8) |
| Similitud con Pocoyo (marca/derechos) | Alto | "Estilo Pocoyo" eliminado del README; colores distintos por personaje y sin gorro/ropa antes de publicar (sección 9) |
| Cambios en políticas de IA/YouTube | Medio | Revisar política de "contenido alterado o sintético" y los umbrales del Programa de Socios antes de escalar |
| Deriva de color/fondo al encadenar clips (ya detectada) | Medio (calidad visual) | Ya mitigado parcialmente con `--limpiar-fondo`; vigilar en episodios más largos |
| Abandono por falta de tiempo (proyecto en solitario) | Alto | Plantilla fija de episodio (sección 2.2) para minimizar tiempo de producción por unidad |
| RPM bajo por ser contenido infantil | Medio (ingresos) | No basar el plan en ingresos altos en Fase 1; ver monetización como validación, no como objetivo económico inmediato |
| Saturación del nicho infantil en YouTube | Medio | Diferenciación por el ángulo educativo explícito (vocabulario/colores/números) + estética claymation poco explotada |

## 14. Próximos pasos inmediatos

1. **Cerrar la marca y el formato:** comprobar "PLOF" a mano en TMview (sección 9.1) y decidir el formato de vídeo (vertical, horizontal o ambos; la sección 8 explica por qué pesa). Nombres y colores ya decididos (sección 9).
2. Completar el pipeline de voz + subtítulos (ya lo tenías como siguiente paso técnico en `HANDOFF.md`).
3. Escribir 5-8 guiones piloto siguiendo la plantilla de la sección 2.2 (uno por palabra/color/número a enseñar).
4. Producir esos pilotos y probarlos con niños reales antes de abrir el canal.
5. Solo entonces, crear el canal de YouTube y lanzar con calendario sostenible.
