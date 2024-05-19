from turtle import mainloop, goto, color, width, penup, pendown
from turtle import forward as linha, left as esquerda, right as direita
from collections import namedtuple
from quadrado_de_koch import quadrado_de_koch


Step = namedtuple('Step', ['limiar', 'color'])
# https://colorswall.com/palette/175970
steps = [Step(320, '#e67c73'),
         Step(80, '#f7cb4d'),
         Step(20, '#41b375'),
         # Step(12, '#7baaf7'),
         # Step(6, '#ba67c8'),
         ]


COMPRIMENTO = 320

# penup()
# goto(-COMPRIMENTO // 4, COMPRIMENTO // 4)
# pendown()

w = len(steps) ** 2
for step in steps:
    width(w)
    w /= 2
    for _ in range(4):
        color(step.color)
        quadrado_de_koch(COMPRIMENTO, step.limiar)
        direita(90)

mainloop()  # Mantém a janela aberta
