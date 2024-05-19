from turtle import mainloop, goto, color, width, penup, pendown
from turtle import forward as linha, left as esquerda, right as direita
from collections import namedtuple


Step = namedtuple('Step', ['limiar', 'color'])
# https://colorswall.com/palette/175970
steps = [Step(301, '#e67c73'),
         Step(101, '#f7cb4d'),
         Step(34, '#41b375'),
         Step(12, '#7baaf7'),
         Step(6, '#ba67c8')]


COMPRIMENTO = 300

penup()
goto(-COMPRIMENTO // 2, COMPRIMENTO // 3)
pendown()


def curva_de_koch(comprimento, limiar=6):
    # https://pt.wikipedia.org/wiki/Curva_de_Koch
    if comprimento < limiar:
        linha(comprimento)                  # ______
    else:
        comprimento /= 3

        curva_de_koch(comprimento, limiar)  # __

        esquerda(60)
        curva_de_koch(comprimento, limiar)  # __/

        direita(120)
        curva_de_koch(comprimento, limiar)  # __/\

        esquerda(60)
        curva_de_koch(comprimento, limiar)  # __/\__


# Floco de neve (3 curvas de Koch formando um "triângulo equilátero")
w = len(steps) ** 2
for step in steps:
    width(w)
    w /= 2
    for _ in range(3):
        color(step.color)
        curva_de_koch(COMPRIMENTO, step.limiar)
        direita(120)

mainloop()  # Mantém a janela aberta
