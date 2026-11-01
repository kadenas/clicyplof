# Guion del ep04 "La torre que se cae" para herramientas/montar_prompts.py
# Ficha: docs/ep04_la_torre_que_se_cae.md

OBJETOS = ("In the scene there are exactly three separate clay cubes with soft rounded edges, matte, with fingerprints: "
           "(1) one BIG RED cube, about as tall as B's belly; (2) one MEDIUM YELLOW cube, clearly smaller than the red one; "
           "(3) one SMALL GREEN cube, clearly smaller than the yellow one. Each cube always keeps its own size and colour. "
           "When stacked, the cubes rest on each other but never stick together, never merge and never squash into one. "
           "None of the cubes is blue.")

INVENTARIO_CUBOS = "Exactly two blue figures and exactly three cubes: one big red, one medium yellow and one small green."

BEATS = {
"beat01_anomalia": dict(
    escena="In the first frame A is leaning sideways with its hand resting on top of B's head, exactly as at the end of the show's intro, and the three cubes lie apart from each other on the floor in front of them.",
    timeline="""[0s-1s] A lifts its hand off B's head and both figures straighten up, smiling. The three cubes lie still on the floor.
[1s-3s] A and B bounce and dance happily on the spot behind the cubes, bending their knees and swinging their arms, giggling, feet staying on the floor, never touching the cubes. The three cubes lie still on the floor, fully visible.
[3s-5s] A and B freeze mid-dance and look down at the three cubes: the big red one, the medium yellow one and the small green one. They look at each other with curious, surprised faces. The three cubes lie still, fully visible.""",
    audio="Audio: a soft playful xylophone tune while they dance, happy toddler giggles, a soft squishy stop when they freeze, then two curious wordless \"hmm?\" toddler sounds. No spoken words.",
    inventario=INVENTARIO_CUBOS + " Every cube stays in the same place, at the same size and colour, from the first frame to the last."),

"beat02_deseo": dict(
    timeline="""[0s-2s] B looks up at A from its feet to the top of its head, stands on tiptoe and holds one stubby arm up high, measuring how tall A is. A watches, amused.
[2s-3.5s] B points at the three cubes on the floor and then points high up into the air, as high as A's head: it wants to build a tower that tall.
[3.5s-5s] B rubs its hands together excitedly, grinning. A smiles with its hand on its chin. The three cubes lie still on the floor, fully visible.""",
    audio="Audio: eager wordless toddler giggles from B, a curious little \"oh!\" from A. No music, no spoken words.",
    inventario=INVENTARIO_CUBOS + " The cubes do not move in this clip."),

"beat03_intento": dict(
    timeline="""[0s-2s] B quickly picks up the SMALL GREEN cube and puts it down on the floor in the middle of the frame.
[2s-4s] B puts the MEDIUM YELLOW cube on top of the small green cube.
[4s-6s] B lifts the BIG RED cube with both arms, straining, and puts it on the very top. Now the tower is upside down: small green at the bottom, yellow in the middle, big red on top. The tower wobbles dangerously.
[6s-8s] B holds the wobbling tower with both stubby arms stretched out. A covers its eyes with both hands, peeking through its fingers.""",
    audio="Audio: soft squishy clay thuds as each cube is placed, a wordless toddler effort grunt when B lifts the red cube, a creaky wobble sound, a worried little \"uh-oh\" from A. No music, no spoken words.",
    inventario=INVENTARIO_CUBOS + " The three cubes stay separate pieces that never merge, never split and never change size."),

"beat04_fallo": dict(
    timeline="""[0s-2s] The upside-down tower tips over towards B. The cubes fall softly onto the floor one after another.
[2s-4s] The big red cube lands on top of B and squashes B flat like a pancake; B springs back into its round shape, dizzy, and the red cube slides off onto the floor next to it.
[4s-6s] The big red cube sits still and steady on the floor, flat and planted. The small green cube keeps rolling a little further across the floor and wobbles before stopping. The yellow cube lies still.
[6s-8s] A looks at the big red cube standing firm, then at the small green cube still wobbling, and tilts its head, thinking. B sits on the floor rubbing its head.""",
    audio="Audio: soft clay thuds as the cubes fall, a big squishy \"plof\" when the red cube lands on B, a little rolling sound for the green cube, a dizzy \"ooh\" from B, a curious \"hmm\" from A. No music, no spoken words.",
    inventario=INVENTARIO_CUBOS + " At the end all three cubes lie apart on the floor, fully visible and whole. No cube splits, disappears, duplicates or leaves the frame."),

"beat05_mejora": dict(
    timeline="""[0s-1.5s] B puts the BIG RED cube on the floor in the middle of the frame.
[1.5s-3s] B puts the SMALL GREEN cube on top of the red one, and then the MEDIUM YELLOW cube on top of the small green one.
[3s-4s] The yellow cube on top tilts and slides off, landing whole on the floor beside the tower, where it rolls a little and stops. The red and the green stay stacked.
[4s-5s] B crosses its arms, grumpy. A scratches its chin, looking at the cubes.""",
    audio="Audio: soft clay thuds, a soft sliding sound and a little \"plop\" when the yellow cube falls, a grumpy \"hmpf\" from B, a thoughtful \"mmm\" from A. No music, no spoken words.",
    inventario=INVENTARIO_CUBOS + " The yellow cube stays whole when it slides off. The cubes never merge."),

"beat06_prediccion": dict(
    timeline="""[0s-2.5s] A takes the cubes and lines them up on the floor in a row, side by side, from the biggest to the smallest: big red, medium yellow, small green.
[2.5s-4s] A points at the row of cubes and looks straight at the camera with a curious face. B stands next to A and also looks at the camera.
[4s-5s] Both stay completely still, holding the pose, as if waiting for an answer.""",
    audio="Audio: near silence with soft clay sounds, and at 1.5s a warm, gentle, friendly female narrator voice asks clearly in Spanish: \"¿Cuál va abajo?\". Only that sentence is spoken. No music, no giggles.",
    inventario=INVENTARIO_CUBOS + " At the end they lie in a row on the floor, from big to small, not stacked."),

"beat07_solucion": dict(
    timeline="""[0s-2s] A puts the BIG RED cube on the floor in the middle of the frame.
[2s-3.5s] A puts the MEDIUM YELLOW cube on top of the red one.
[3.5s-5s] A puts the SMALL GREEN cube on the very top. The tower is now big red at the bottom, medium yellow in the middle and small green on top, standing perfectly straight and completely still.
[5s-6.5s] B stands next to the tower and measures it with its arm: it is almost as tall as A's chin. A and B look at each other amazed.
[6.5s-8s] A and B jump with joy, arms in the air, next to the tower, which stays perfectly still and straight.""",
    audio="Audio: three soft clay \"toc\" sounds as each cube is placed, a small magical \"ping\" when the tower is finished, and at 5s a warm, gentle, friendly female narrator voice says clearly in Spanish: \"¡El grande, abajo!\". Only those words are spoken. Then happy toddler cheers and giggles. No music.",
    inventario=INVENTARIO_CUBOS + " At the end they are stacked in one straight tower: red at the bottom, yellow in the middle, green on top. The tower does not fall."),

"beat08_eco": dict(
    timeline="""[0s-1.5s] B gives the tower a little pat with its hand.
[1.5s-3.5s] The tower wobbles gently from side to side, once, twice... and settles, standing perfectly straight again. A and B hold their breath, eyes wide.
[3.5s-5s] A and B let out a big sigh of relief, their bodies squashing softly, and burst out laughing.""",
    audio="Audio: a soft pat, a creaky wobble, a tense \"uuuh\" from both, a big relieved sigh and happy toddler laughter. No spoken words.",
    inventario=INVENTARIO_CUBOS + " The three cubes stay stacked in the same tower (red, yellow, green from bottom to top) and never fall."),
}
