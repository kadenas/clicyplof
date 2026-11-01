# Guion del ep07 "Falta una" para herramientas/montar_prompts.py
# Ficha: docs/ep07_falta_una.md

OBJETOS = ("On the white floor in front of the figures there are exactly three small flat round LIGHT PINK clay marks lying in a row, "
           "like three little pink coins, evenly spaced. There are exactly three clay balls, each about the size of a fist of B and much smaller "
           "than B's belly: (1) one RED ball, (2) one YELLOW ball, (3) one GREEN ball. Each ball keeps its own colour and size. "
           "Nothing in the scene is blue except the two figures.")

INVENTARIO = ("Exactly two blue figures, exactly three pink marks and exactly three balls: one red, one yellow and one green. "
              "Never four balls, never two balls: there are always three.")

BEATS = {
"beat01_anomalia": dict(
    escena="In the first frame A is leaning sideways with its hand resting on top of B's head, exactly as at the end of the show's intro, and each ball sits on top of one pink mark: red on the first, yellow on the second, green on the third.",
    timeline="""[0s-1s] A lifts its hand off B's head and both figures straighten up, smiling. The three balls sit still on their marks.
[1s-2.5s] A and B bounce and dance happily on the spot, giggling. While dancing, B stamps its foot on the floor right next to the row.
[2.5s-4s] The three balls roll off their marks. The red and the yellow roll a little and stop near the marks. The GREEN ball keeps rolling slowly across the floor and stops in the bottom right corner of the frame, still inside the frame and fully visible.
[4s-5s] A and B freeze and look down at the three empty pink marks, surprised. The green ball stays still in the corner.""",
    audio="Audio: a soft playful xylophone tune while they dance, happy toddler giggles, a soft thump on the stamp, little rolling sounds, then a surprised wordless \"oops!\" toddler sound. No spoken words.",
    inventario=INVENTARIO + " The green ball stays inside the frame, in the bottom right corner, fully visible. The marks never move."),

"beat02_deseo": dict(
    timeline="""[0s-2s] B picks up the red ball and puts it on the first pink mark.
[2s-3.5s] B picks up the yellow ball and puts it on the second pink mark.
[3.5s-5s] B dusts off its hands proudly, with its back to the bottom right corner. The third pink mark is empty. The green ball stays still in the corner, fully visible.""",
    audio="Audio: two soft clay \"toc\" sounds, a proud little giggle from B. No music, no spoken words.",
    inventario=INVENTARIO + " The green ball does not move from the corner."),

"beat03_intento": dict(
    timeline="""[0s-2s] A points at the empty third pink mark.
[2s-4s] B scratches its head, then smiles cheekily and curls itself up into a round ball shape.
[4s-6.5s] B sits down on top of the empty third mark, curled up and very still, pretending to be the missing ball. B is much bigger than the balls.
[6.5s-8s] A covers its mouth with both hands, trying not to laugh. The green ball stays still in the corner, fully visible.""",
    audio="Audio: a questioning \"hm?\" from A, a cheeky giggle from B, a soft squishy sound as B sits, a muffled giggle from A. No music, no spoken words.",
    inventario=INVENTARIO + " The red ball stays on the first mark, the yellow on the second, the green in the corner."),

"beat04_fallo": dict(
    timeline="""[0s-2.5s] B, curled up like a ball on the third mark, starts to wobble from side to side.
[2.5s-5s] B rolls off the mark, tumbles head over heels across the floor and squashes flat, then springs back into its shape.
[5s-8s] B sits up, dizzy, its head wobbling. The third pink mark is empty again. A laughs. The green ball stays still in the corner.""",
    audio="Audio: a wobbly creak, a soft rolling tumble, a squishy \"plof\", a dizzy \"ooh\" from B, warm wordless toddler laughter from A. No music, no spoken words.",
    inventario=INVENTARIO + " B never bumps into the balls. The red and yellow balls stay on their marks; the green stays in the corner."),

"beat05_mejora": dict(
    timeline="""[0s-2s] A touches the three pink marks one by one with its finger: one, two, three.
[2s-3.5s] A touches the two balls on the marks one by one: one, two.
[3.5s-5s] A stops and stares at the empty third mark, puzzled.""",
    audio="Audio: soft little taps, and from 0.5s a warm, gentle, friendly female narrator voice counts slowly in Spanish: \"Una, dos, tres... una, dos...\". Only those words are spoken. No music.",
    inventario=INVENTARIO + " Nothing moves in this clip except A."),

"beat06_prediccion": dict(
    timeline="""[0s-2s] A stands next to the empty third mark and holds up two fingers.
[2s-3.5s] A looks straight at the camera with a questioning face. B stands next to A and also looks at the camera.
[3.5s-5s] Both stay completely still, holding the pose, as if waiting for an answer. The green ball stays still in the bottom right corner, fully visible.""",
    audio="Audio: near silence with soft clay sounds, and at 1.5s a warm, gentle, friendly female narrator voice asks clearly in Spanish: \"¿Dónde está la que falta?\". Only that sentence is spoken. No music, no giggles.",
    inventario=INVENTARIO),

"beat07_solucion": dict(
    timeline="""[0s-2s] A turns around and sees the green ball in the bottom right corner, and points at it happily.
[2s-4s] A walks to the corner and picks up the green ball.
[4s-6s] A walks back and puts the green ball on the empty third pink mark. Now there are three balls on three marks: red, yellow and green.
[6s-8s] A and B jump with joy, arms in the air.""",
    audio="Audio: an excited \"oh!\" from A, soft squishy footsteps, a soft \"toc\", a small magical \"ping\", and at 5s a warm, gentle, friendly female narrator voice says clearly in Spanish: \"¡Tres!\". Only that word is spoken. Then happy toddler cheers. No music.",
    inventario=INVENTARIO + " At the end each ball sits on its own mark: red on the first, yellow on the second, green on the third."),

"beat08_eco": dict(
    timeline="""[0s-2s] B curls up into a round ball shape and sits down at the end of the row, next to the three balls, like a fourth ball.
[2s-3.5s] A points at the balls one by one with its finger and then at B, and starts laughing.
[3.5s-5s] B uncurls and both laugh together.""",
    audio="Audio: a cheeky giggle from B, and at 2.5s a warm, gentle, friendly female narrator voice asks in Spanish with a smile: \"¿Cuatro?\". Only that word is spoken. Then happy toddler laughter. No music.",
    inventario=INVENTARIO + " The three balls stay on their marks and do not move."),
}
