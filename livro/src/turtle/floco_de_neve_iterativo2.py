from turtle import mainloop, goto, color, width, penup, pendown
from turtle import forward as linha, left as esquerda, right as direita
from collections import namedtuple
from floco_de_neve import curva_de_koch


Step = namedtuple('Step', ['limiar', 'color'])
# https://colorswall.com/palette/175970
steps = [Step(301, '#e67c73'),
         Step(101, '#f7cb4d'),
         Step(34, '#41b375'),
         Step(12, '#7baaf7'),
         Step(6, '#ba67c8')]


def main():
    COMPRIMENTO = 300

    penup()
    goto(-COMPRIMENTO // 2, COMPRIMENTO // 3)
    pendown()
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


if __name__ == '__main__':
    main()
