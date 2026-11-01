"""
revisar_clip.py — tira de 10 fotogramas de un clip + azul medio de los muñecos al principio y al final.
Uso: D:/ComfyUI/.venv/Scripts/python.exe herramientas/revisar_clip.py output/clip.mp4 tira.png
Si el azul se aleja mucho de la referencia (~25,128,202) o la tira enseña personajes cambiados, el clip es dudoso.
"""
# Revisión rápida de un clip: tira de 10 fotogramas + azul medio de los muñecos al principio y al final
import av, sys
import numpy as np
from PIL import Image
ruta, salida = sys.argv[1], sys.argv[2]
with av.open(ruta) as c:
    fot = [f.to_image() for f in c.decode(video=0)]
n = 10; idx = [round(i * (len(fot) - 1) / (n - 1)) for i in range(n)]
w = 192; h = round(w * fot[0].height / fot[0].width)
lienzo = Image.new('RGB', (5 * w, 2 * h), 'white')
for k, i in enumerate(idx):
    lienzo.paste(fot[i].resize((w, h)), ((k % 5) * w, (k // 5) * h))
lienzo.save(salida)
def azul(im):
    x = np.asarray(im).astype(int); r, g, b = x[..., 0], x[..., 1], x[..., 2]
    m = (b > 150) & (b - r > 100) & (g > 90)   # azul vivo de los muñecos (excluye el marino)
    return x[m].mean(0).round().tolist(), int(m.sum())
print(len(fot), 'fotogramas | azul inicio', azul(fot[0]), '| azul final', azul(fot[-1]), '| referencia ~[25,128,202]')
