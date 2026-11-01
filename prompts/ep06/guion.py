# Guion del ep06 "Sitio para dos" para herramientas/montar_prompts.py
# Ficha: docs/ep06_sitio_para_dos.md

OBJETOS = ("On the white floor in front of the figures lies one small flat ORANGE clay rug, rectangular with rounded corners, "
           "just wide enough for the two figures sitting side by side. A straight YELLOW clay stripe crosses the rug from front to back, "
           "dividing it into two equal halves. The rug always lies flat on the floor: it never folds, wrinkles, lifts or changes size. "
           "Nothing in the scene is blue except the two figures.")

INVENTARIO = "Exactly two blue figures and one orange rug with its yellow stripe."

BEATS = {
"beat01_anomalia": dict(
    escena="In the first frame A is leaning sideways with its hand resting on top of B's head, exactly as at the end of the show's intro.",
    timeline="""[0s-1s] A lifts its hand off B's head and both figures straighten up, smiling. The rug lies still on the floor.
[1s-3s] A and B bounce and dance happily on the spot behind the rug, bending their knees and swinging their arms, giggling, never stepping on the rug.
[3s-5s] A and B freeze mid-dance, look down at the soft orange rug, and their faces light up with delight. The rug lies flat and still, the yellow stripe clearly visible.""",
    audio="Audio: a soft playful xylophone tune while they dance, happy toddler giggles, a soft squishy stop when they freeze, then two delighted wordless \"ooh!\" toddler sounds. No spoken words.",
    inventario=INVENTARIO + " The rug stays in the same place, flat, from the first frame to the last."),

"beat02_deseo": dict(
    timeline="""[0s-2s] A and B both point at the middle of the rug at the same time.
[2s-3.5s] They look at each other, frown a little, and point at the middle of the rug again, harder.
[3.5s-5s] Both rub their hands together, eyeing the middle of the rug. The rug lies flat and still.""",
    audio="Audio: two eager wordless \"mmm!\" sounds, a little competitive \"hmm!\" from each. No music, no spoken words.",
    inventario=INVENTARIO + " The rug does not move."),

"beat03_intento": dict(
    timeline="""[0s-2s] A and B hurry onto the rug and both try to sit down right in the middle at the same time.
[2s-5s] They bump belly against belly and push each other with their tummies, bouncing and wobbling like jelly, neither giving way.
[5s-8s] They keep pushing, side against side, grunting, both squeezed in the middle of the rug. The rug stays flat on the floor.""",
    audio="Audio: soft squishy \"boing\" sounds each time their bellies bump, wordless toddler effort grunts, playful annoyed \"hmpf\" sounds. No music, no spoken words.",
    inventario=INVENTARIO + " The two figures are always two separate figures: they bump and bounce off each other and never stick together or merge."),

"beat04_fallo": dict(
    timeline="""[0s-2s] With one last big push, A and B bounce off each other and fly out to opposite sides.
[2s-4s] Each one lands sitting on the floor OUTSIDE the rug, one on the left and one on the right; both squash flat on landing and spring back.
[4s-6s] The rug lies empty and flat between them, the yellow stripe across its middle clearly visible.
[6s-8s] A and B sit on the floor, cross their arms and look at each other, grumpy.""",
    audio="Audio: a big squishy \"boing\", two soft \"plof\" sounds as they land, two grumpy wordless \"hmpf\" sounds. No music, no spoken words.",
    inventario=INVENTARIO + " At the end the rug is empty and flat, with nobody on it."),

"beat05_mejora": dict(
    timeline="""[0s-1.5s] A stands up and sits down alone on the rug.
[1.5s-3s] B stays outside the rug on the floor, looking down, sad.
[3s-5s] A looks at B and stops smiling. Then A looks down at the yellow stripe on the rug next to it, thinking.""",
    audio="Audio: near silence, a soft sad sigh from B, a thoughtful \"mmm\" from A. No music, no spoken words.",
    inventario=INVENTARIO + " The rug stays flat."),

"beat06_prediccion": dict(
    timeline="""[0s-2s] A points at the yellow stripe that divides the rug in two halves.
[2s-3.5s] A looks straight at the camera with a curious face. B stands next to the rug and also looks at the camera.
[3.5s-5s] Both stay completely still, holding the pose, as if waiting for an answer.""",
    audio="Audio: near silence with soft clay sounds, and at 1.5s a warm, gentle, friendly female narrator voice asks clearly in Spanish: \"¿Cabemos los dos?\". Only that sentence is spoken. No music, no giggles.",
    inventario=INVENTARIO + " The rug and its stripe stay exactly the same."),

"beat07_solucion": dict(
    timeline="""[0s-2s] A slides over onto one half of the rug and pats the other half with its hand, inviting B.
[2s-4s] B smiles and sits down on the other half.
[4s-6s] They sit side by side, shoulder to shoulder, each one on its own half of the rug, with the yellow stripe between them. They fit.
[6s-8s] They hug each other sideways, smiling happily.""",
    audio="Audio: soft pats, a small magical \"ping\" when they both fit, and at 5s a warm, gentle, friendly female narrator voice says clearly in Spanish: \"¡Mitad y mitad!\". Only those words are spoken. Then happy toddler giggles. No music.",
    inventario=INVENTARIO + " The two figures stay two separate figures sitting side by side; they never merge."),

"beat08_eco": dict(
    timeline="""[0s-2s] Sitting on its half, B slowly stretches one arm over into A's half of the rug.
[2s-3.5s] A raises one eyebrow and looks at B's arm.
[3.5s-5s] B pulls its arm back with a cheeky grin, and both burst out laughing.""",
    audio="Audio: a cheeky little giggle from B, a questioning \"hm?\" from A, then happy toddler laughter from both. No spoken words.",
    inventario=INVENTARIO + " Both stay sitting on the rug, each on its own half."),
}
