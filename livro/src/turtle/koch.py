from turtle import mainloop, goto, penup, pendown, width, color, exitonclick
from turtle import forward as linha, left as esquerda, right as direita


def curva_de_koch(comprimento, niveis):
    """Desenha uma Curva de Koch.

    https://pt.wikipedia.org/wiki/Curva_de_Koch
    """
    if niveis == 0:
        linha(comprimento)          # ______
    else:
        comprimento /= 3
        niveis -= 1

        curva_de_koch(comprimento, niveis)  # __

        esquerda(60)
        curva_de_koch(comprimento, niveis)  # __/

        direita(-120)
        curva_de_koch(comprimento, niveis)  # __/\

        esquerda(60)
        curva_de_koch(comprimento, niveis)  # __/\__


def curva(comprimento, niveis=0, lados=3):
    """Desenha um segmento de reta baseado na Curva de Koch.

    A Curva de Koch é baseada em um conceito mais simples de triângulo
    equilátero. Ela divide um segmento de reta em 3 partes de mesmo comprimento
    e usa o segundo segmento como a base de um triângulo equilátero. A linha de
    "base" do não é desenhada. Por exemplo, para um segmento de reta de
    comprimento "6" temos a seguinte representação:

                            ______ -> __/\__

    A implementação é recursiva, portanto cada parte do segmento é, por sua vez,
    desenhada como uma Curva de Koch, até que se atinja um limiar de precisão
    arbitrário. Neste momento, é desenhada um segmento com todo o comprimento.

    Esta função generaliza a ideia para qualquer polígono regular. A
    implementação é similar, são separados os 3 segmentos de mesmo tamanho e o
    do meio serve de base para o polígono. Por exemplo, para um polígono de 4
    lados temos:
                                         __
                            ______ -> __| |__

    Args:
      - comprimento: valor do comprimento total do segmento de reta.
      - niveis: a quantidade de níveis de recursão desejada.
      - lados: número de lados do polígono.

    https://pt.wikipedia.org/wiki/Curva_de_Koch
    """

    if lados < 3:
        raise ValueError('A quantidade mínima de lados é 3.')

    if niveis == 0:
        linha(comprimento)
    else:
        comprimento /= 3
        niveis -= 1
        angulo_externo = 360 / lados
        angulo_interno = 180 - angulo_externo

        # 1o segmento
        curva(comprimento, niveis, lados)
        esquerda(angulo_interno)

        # 2o "segmento" (polígono regular sem o "lado base")
        for _ in range(lados - 1):
            curva(comprimento, niveis, lados)
            direita(angulo_externo)

        # 3o segmento
        esquerda(180)
        curva(comprimento, niveis, lados)


def poligono(lados, comprimento, niveis=0, desenha=lambda x, y, z: linha(x)):
    angulo_externo = 360 / lados
    for _ in range(lados):
        desenha(comprimento, niveis, lados)
        direita(angulo_externo)


def main():
    comprimento = limiar = 400
    colors = ['#e67c73', '#f7cb4d', '#41b375', '#7baaf7', '#ba67c8']
    w = len(colors) ** 2

    penup()
    goto(-comprimento // 2, -200)
    pendown()

    poligono(3, 200, 2)

    # for i, c in enumerate(colors):
    #     penup()
    #     goto(-comprimento // 2, i * i * 20)
    #     pendown()

    #     curva(comprimento, i)

    # for c in colors:
    #     color(c)

    #     width(w)
    #     w /= 2

    #     poligono(3, comprimento, limiar + 1)

    #     limiar //= 3

    exitonclick()
    # mainloop()  # Mantém a janela aberta


def triangulo_sierpinski(comprimento, niveis):
    def triangulo(c):
        esquerda(60)
        linha(c)
        direita(120)
        linha(c)
        direita(120)
        linha(c)
        esquerda(180)

    if niveis == 0:
        triangulo(comprimento)
    else:
        comprimento /= 2
        niveis -= 1

        # bottom left
        triangulo_sierpinski(comprimento, niveis)
        # top
        penup()
        esquerda(60)
        linha(comprimento)
        direita(60)
        pendown()
        triangulo_sierpinski(comprimento, niveis)
        # bottom right
        penup()
        direita(60)
        linha(comprimento)
        esquerda(60)
        pendown()
        triangulo_sierpinski(comprimento, niveis)
        # back to origin
        penup()
        esquerda(180)
        linha(comprimento)
        esquerda(180)
        pendown()


def tapete_sierpinski(comprimento, niveis):
    pass




    # esquerda(60)
    # linha(comprimento)
    # triangulo(comprimento)
    # linha(comprimento)
    # direita(60)
    # triangulo(comprimento)

    # triangulo_sierpinski(comprimento, limiar)
    # direita(120)
    # triangulo_sierpinski(comprimento, limiar)
    # direita(120)
    # triangulo_sierpinski(comprimento, limiar)
    # esquerda(180)


if __name__ == '__main__':
    poligono(4, 100, 2)
    # triangulo_sierpinski(200, 4)
    mainloop()
    # main()
