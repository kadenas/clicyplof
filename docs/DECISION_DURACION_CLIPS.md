# Decisión: motor narrativo fijo, punto dulce de calidad y duración de los clips

Fecha: 16/09/2026
Estado: **DECIDIDO el 16/09/2026**: se adopta la propuesta mixta (5 s los beats de situación, 8 s los tres de acción; Deseo a 5 s, con 3 s permitido si la ficha lo justifica). Historia = 52 s; con careta, rótulo y el cierre nuevo de 3 s, el Short ≈ 61 s. Aplicado en `TEMPORADA_0.md`, `PLANTILLA_FICHA_EPISODIO.md`, `README.md`, `FICHA_TECNICA.md` y la web. El episodio 01 se queda como está (8 × 8 s).

Este documento recoge el análisis de tres dudas planteadas el 16/09/2026, con las cifras medidas en la máquina de producción (RTX 4060 Ti 16 GB, 64 GB RAM, MiniMax H3 int8 con LoRA turbo de 8 pasos).

---

## 1. ¿Es un riesgo que todos los episodios recorran el mismo motor narrativo?

Nadie puede garantizar el éxito de una serie. Lo que sí se puede decir es si esta decisión concreta juega a favor o en contra con el público de 2-6 años.

### Lo que dice el precedente

Todo lo que ha funcionado en preescolar tiene estructura fija:

- **Blue's Clues**: cada episodio idéntico (tres pistas, silla de pensar, carta). Nickelodeon emitía *el mismo episodio* cinco días seguidos. Crawley, Anderson, Wilder, Williams y Santomero (1999, *Journal of Educational Psychology*, 91(4)) midieron que con cada repetición **subían la atención, la participación en voz alta y la comprensión**. Para un niño de 3 años la repetición no es aburrimiento: es dominio.
- **Pocoyó** (Zinkia, España): estudio blanco vacío, narrador, un problema por episodio. Es el precedente más parecido a Clic y Plof.
- **Dora, Peppa Pig, Teletubbies**: fórmula calcada episodio a episodio ("Again! Again!").
- **Ritmo**: Lillard y Peterson (2011, *Pediatrics*, 128(4)) midieron que 9 minutos de dibujos rápidos (*Bob Esponja*) deterioraban la función ejecutiva de niños de 4 años frente a dibujos lentos. El ritmo pausado y previsible es el adecuado para esta edad.

### El motivo interno

**La pausa de predicción del beat 06 solo funciona si el formato es fijo.** El niño se adelanta a la respuesta porque *sabe* que ahora toca la pregunta. Con un formato cambiante ese recurso desaparece.

### Conclusión

El motor fijo (anomalía → deseo → intento → fallo → mejora → predicción → solución → eco) es la norma del género, no el riesgo. Los riesgos reales están en otro sitio:

1. **La piel repetida, no el esqueleto.** El motor es invisible para el niño; lo que ve es el objeto, el color y el gag. En un feed de Shorts la decisión de pasar se toma en 1-2 s. Regla de producción: **el objeto del día está en pantalla desde el primer fotograma y es distinto en cada episodio.** Si los 25 abren igual (careta + dos azules en blanco), el espectador que ya conoce la serie la reconoce (bien) pero el nuevo no distingue un episodio de otro (mal).
2. **Los 8 s fijos por beat.** Las series citadas tienen *secuencia* fija, no *duración* fija. "Deseo" no necesita 8 s; "Fallo", que es la comedia física, puede necesitar más. Los 8 s son una comodidad de producción (la rejilla de 192 fotogramas), no una necesidad narrativa. Ver el apartado 3.
3. **Los 3 s congelados en un feed.** En televisión el niño espera. En Shorts, un fotograma quieto en silencio hacia el segundo 45 puede ser un acantilado de retención. No se cambia a ciegas: YouTube Studio da la curva de retención segundo a segundo y ahí se verá.

### Cómo comprobarlo antes de producir 25 episodios

1. Probar el ep. 01 con 3-4 niños más (ya está en el HANDOFF; hay una sola prueba hecha).
2. Publicar los 5 primeros y leer la curva de retención. Si hay caída en la pausa o en los cortes entre beats, se corrige antes del ep. 06.
3. Comparar el ep. 02 (misma piel que el 01: anillo y fichas) con el 03 (piel nueva). Eso mide si la repetición resta o no, con datos propios.

---

## 2. Punto dulce de calidad con la RTX 4060 Ti

### Tiempos medidos (LoRA turbo, 8 pasos)

| Resolución | Duración | Tiempo | Coste por segundo de vídeo | Memoria |
|---|---|---|---|---|
| 480×864 | 5 s | 4 min | 0,8 min/s | holgada |
| 480×864 | 8 s | 5,5 min | 0,7 min/s | holgada |
| 768×1344 | 5 s | 13 min | 2,6 min/s | bien |
| 768×1344 | 8 s | 23-25 min | 3,0 min/s | **1,8 GB de VRAM libres, <5 GB de RAM libres** |
| 864×1536 (siguiente 9:16 exacto) | 8 s | ≈ 35-45 min *si cabe* (extrapolado) | — | casi seguro desborda a RAM |

Lectura de las cifras:

- **La resolución escala peor que lineal**: 2,5× píxeles cuestan 3,3-4,4× tiempo, porque la atención del modelo crece con el cuadrado de los tokens.
- **768×1344 a 8 s es el techo práctico de la tarjeta.** Con 1,8 GB de VRAM libres, el siguiente escalón desborda a RAM y el tiempo se dispara.
- Resoluciones 9:16 exactas con lados múltiplos de 32: 576×1024, 864×1536, 1152×2048. Ninguna es mejor opción que 768×1344 recortado.

### Recomendación

- **Resolución: 768×1344 se queda.** El salto a 864×1536 cuesta ×1,5 como mínimo, probablemente no cabe, y el reescalador lo cubre: plastilina sobre fondo blanco (superficies planas, bordes suaves, sin textura fina) es el caso ideal para RealESRGAN. El 9:16 se corrige gratis: **recortar a 756×1344 en el montaje** (6 px de fondo blanco por lado; 756/1344 = 0,5625 exacto) y reescalar a 1080×1920.
- **Pasos: el turbo de 8 se queda.** Sin LoRA son 30-50 pasos: ×4-6, entre 1,5 y 2,5 h por clip. Para unos 200 clips es inviable. La prueba de 3 s sin turbo (~20 min, apuntada en el HANDOFF) sirve para *saber* qué se pierde, no para producir así.
- **Antes que cualquier subida de resolución, las tres mejoras ya diagnosticadas que cuestan 0 GPU:**
  1. Fotograma de enlace en PNG desde el workflow, en vez de extraerlo del mp4 comprimido. La intro, que arranca de PNG, se ve mejor que los beats encadenados: la prueba está hecha.
  2. Recorte a 9:16 exacto en el montaje.
  3. Afinar `FUERZA = 0.85` en `herramientas/fondo.py` (puede aplanar la textura).

### Presupuesto resultante

Episodio de 8 beats a 8 s ≈ 3,2 h, más un 25 % de repeticiones (en el ep. 01 se repitieron 2 de 8 clips) ≈ **4 h de GPU por episodio, ≈ 100 h para 25 episodios**. Doce o trece noches de máquina.

---

## 3. ¿Clips de 5 s en vez de 8 s?

### El coste no es exponencial

De 5 a 8 s son ×1,55 fotogramas (124 → 192) y ×1,85 tiempo (13 → 24 min). Por segundo de vídeo terminado, el clip de 8 s cuesta 3,0 min/s y el de 5 s cuesta 2,6 min/s: **un 15 % más caro el de 8 s**, no el doble ni el triple. Exponencial sería que 8 s costara ×4.

### Dónde gana el clip de 5 s

- **En lo que se tira.** Un clip fallido de 8 s son 24 min a la basura; uno de 5 s, 13.
- **En la tasa de fallo.** Los fallos del ep. 01 fueron de conservación de objetos (fichas que se duplican, cosas que desaparecen), que empeora cuanto más largo es el clip. El clip corto falla menos y cuesta menos cuando falla.
- **En margen de memoria.**

### Dónde pierde

- **Cada corte cuesta calidad**: deriva del fondo, azul que se oscurece, 8 fotogramas que se saltan (`@saltar=8`). Rellenar 64 s con clips de 5 s son 13 clips y 12 cortes en vez de 7.
- **La narradora llega 1-2 s tarde**, que en un clip de 5 s es una fracción grande.

### Propuesta: un clip por beat, y cada beat con la duración que necesita

La rejilla del modelo (5 + 17k fotogramas a 24 fps) da más opciones de las usadas hasta ahora:

| Fotogramas | Duración |
|---|---|
| 73 | 3 s |
| 107 | 4,5 s |
| 124 | 5 s |
| 141 | 6 s |
| 158 | 6,5 s |
| 192 | 8 s |

Reparto propuesto:

| Beat | Ahora | Propuesta |
|---|---|---|
| 01 Anomalía | 8 s | 5 s |
| 02 Deseo | 8 s | 3-5 s |
| 03 Intento | 8 s | 8 s |
| 04 Fallo | 8 s | 8 s (la comedia física, no se recorta) |
| 05 Mejora | 8 s | 5 s |
| 06 Predicción | 5 + 3 s | 5 + 3 s |
| 07 Solución | 8 s | 8 s |
| 08 Eco | 8 s | 5 s |

Resultado: historia ≈ 50 s en vez de 64, Short ≈ 56 s con careta y rótulo. Mismos 7 cortes, **≈ 2,2 h de GPU por episodio en vez de 3,2**, menos fallos y un ritmo que respira donde debe.

Regla fija: **nunca partir un beat en 5 + 3.** Ahí se pierde más en el corte de lo que se gana.

---

## Decisión

La propuesta del apartado 3 **cambia el "64 SECOND SYSTEM"** que el HANDOFF marcaba como intocable. **Aprobada el 16/09/2026.** Lo que implicaba, y su estado:

1. ✅ Actualizados `docs/TEMPORADA_0.md`, `docs/PLANTILLA_FICHA_EPISODIO.md`, `README.md`, `FICHA_TECNICA.md` y `web/index.html` con las duraciones por beat.
2. ⬜ Fijar las duraciones del ep. 02 en su ficha antes de generar nada (ya vienen rellenas en la plantilla).
3. ⬜ Aplicar las tres mejoras gratuitas del apartado 2 en el mismo cambio de montaje.
