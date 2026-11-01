# Guion del ep05 "El otro lado" para herramientas/montar_prompts.py
# Ficha: docs/ep05_el_otro_lado.md

OBJETOS = ("Behind the figures, in the middle distance, there is a BROWN clay wall that crosses the whole width of the frame from edge to edge. "
           "The wall is lower than A's head and taller than B. At the bottom of the wall, in the middle, there is a small round ARCH, an open "
           "hole through which the white floor behind can be seen; the arch is bigger than the ball but much smaller than B. "
           "On the floor behind the wall lies a flat YELLOW clay star, visible above the wall and through the arch. "
           "On the floor in front of the wall, near the figures, there is one ORANGE clay ball, about the size of B's head. "
           "The wall is solid and never moves from its place: nobody can walk through it. Nothing in the scene is blue except the two figures.")

INVENTARIO = "Exactly two blue figures, one brown wall with one open arch, one yellow star behind the wall and one orange ball."

BEATS = {
"beat01_anomalia": dict(
    escena="In the first frame A is leaning sideways with its hand resting on top of B's head, exactly as at the end of the show's intro.",
    timeline="""[0s-1s] A lifts its hand off B's head and both figures straighten up, smiling. The wall, the star and the ball stay still.
[1s-3s] A and B bounce and dance happily on the spot in front of the wall, bending their knees and swinging their arms, giggling. The wall, the star and the ball stay still, fully visible.
[3s-5s] A and B freeze mid-dance and look at the wall in front of them, then at each other, with puzzled faces. The orange ball lies still at their feet. The wall, the arch and the star stay exactly in place.""",
    audio="Audio: a soft playful xylophone tune while they dance, happy toddler giggles, a soft squishy stop when they freeze, then two curious wordless \"hmm?\" toddler sounds. No spoken words.",
    inventario=INVENTARIO + " Every object stays in the same place from the first frame to the last."),

"beat02_deseo": dict(
    timeline="""[0s-2s] A stretches up and looks over the top of the wall, sees the yellow star behind it and points at it excitedly.
[2s-3.5s] B jumps up and down next to the wall but is too short to see over it.
[3.5s-5s] A picks up the orange ball, shows it to B and points at the star behind the wall: the ball has to go there. B nods eagerly.""",
    audio="Audio: an excited \"oh!\" from A, soft squishy boings as B jumps, an eager giggle from B. No music, no spoken words.",
    inventario=INVENTARIO + " The wall, the arch and the star never move."),

"beat03_intento": dict(
    timeline="""[0s-1s] A hands the orange ball to B.
[1s-4s] B throws the ball up towards the top of the wall: it hits the top edge of the wall, bounces back and rolls along the floor to B's feet.
[4s-7s] B throws again, harder: the ball hits the top edge again, bounces back and rolls to B's feet again.
[7s-8s] A covers its mouth with both hands. B stamps its foot.""",
    audio="Audio: a wordless toddler effort grunt on each throw, a soft \"boing\" each time the ball hits the wall, rolling sounds, a little \"oh no\" sound from A. No music, no spoken words.",
    inventario=INVENTARIO + " The ball never goes over the wall in this clip, it always bounces back. One single ball, always visible."),

"beat04_fallo": dict(
    timeline="""[0s-2.5s] B grabs the ball, spins round and round on the spot with all its strength, and throws the ball straight up into the air.
[2.5s-4s] The ball goes straight up and comes straight back down onto B's head: B squashes flat like a pancake, then springs back into its round shape.
[4s-6s] B wobbles, dizzy, and sits down on the floor. The ball rolls a little and stops on the floor right in front of B.
[6s-8s] B sits tired and dizzy with the ball in front of it. A bends over laughing.""",
    audio="Audio: a whooshing spin, a soft \"boing\" and a big squishy \"plof\" when the ball lands on B's head, a dizzy \"ooh\" from B, warm wordless toddler laughter from A. No music, no spoken words.",
    inventario=INVENTARIO + " The ball stays inside the frame and never goes over the wall. The wall never moves."),

"beat05_mejora": dict(
    timeline="""[0s-2s] A goes to the wall and pushes it with both hands: the clay wall bulges and wobbles softly, then springs back exactly to its place and shape.
[2s-3.5s] A crouches down low to push harder, and its face ends up right in front of the arch at the bottom of the wall.
[3.5s-5s] A looks through the arch, sees the yellow star on the other side, and opens its eyes wide with surprise.""",
    audio="Audio: a soft squishy push and wobble, a wordless effort grunt from A, then a small magical \"ping\" when A looks through the arch. No music, no spoken words.",
    inventario=INVENTARIO + " The wall stays in exactly the same place and shape after the push. The arch stays open. Nobody goes through the arch."),

"beat06_prediccion": dict(
    timeline="""[0s-2s] A points at the arch at the bottom of the wall and looks at B.
[2s-3.5s] B, sitting on the floor with the orange ball in front of it, looks at the arch, then looks straight at the camera with a curious face.
[3.5s-5s] A also looks at the camera. Both stay completely still, holding the pose, as if waiting for an answer.""",
    audio="Audio: near silence with soft clay sounds, and at 1.5s a warm, gentle, friendly female narrator voice asks clearly in Spanish: \"¿Por dónde puede pasar?\". Only that sentence is spoken. No music, no giggles.",
    inventario=INVENTARIO + " The ball stays on the floor in front of B and does not move in this clip."),

"beat07_solucion": dict(
    timeline="""[0s-2s] B, still sitting and tired, gives the orange ball a lazy little push along the floor towards the arch.
[2s-4.5s] The ball rolls slowly along the floor, straight through the open arch at the bottom of the wall, and keeps rolling on the other side.
[4.5s-6s] The ball slows down and stops right on top of the yellow star, fully visible.
[6s-8s] B jumps up with joy, A claps, and they both jump up and down, arms in the air.""",
    audio="Audio: a soft rolling sound, a small magical \"ping\" when the ball stops on the star, and at 5s a warm, gentle, friendly female narrator voice says clearly in Spanish: \"¡Por abajo!\". Only those words are spoken. Then happy toddler cheers and giggles. No music.",
    inventario=INVENTARIO + " There is only one orange ball: it passes through the arch whole, without changing size, and ends resting on top of the star behind the wall, fully visible."),

"beat08_eco": dict(
    objetos=("Behind the figures there is a BROWN clay wall crossing the whole frame, with a small open ARCH at the bottom in the middle; "
             "behind the wall, the orange ball rests on top of a flat yellow star. The arch is much smaller than B. Nothing in the scene is blue except the two figures."),
    timeline="""[0s-2s] B curls up into a ball and rolls along the floor towards the arch, wanting to go through too.
[2s-3.5s] B is much bigger than the arch: it bumps softly against the wall next to the arch, squashes, and bounces back, uncurling.
[3.5s-5s] B sits on the floor laughing. A laughs too. The ball stays on the star behind the wall.""",
    audio="Audio: a soft rolling sound, a squishy \"boing\" when B bumps the wall, happy toddler laughter from both. No spoken words.",
    inventario=INVENTARIO + " B does not fit through the arch and stays on this side of the wall. The wall never moves. The ball stays on the star."),
}
