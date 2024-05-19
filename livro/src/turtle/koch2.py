from tartaruga import *


def segmento_koch(comprimento, niveis=0, lados=3):
    r"""Desenha um segmento de reta baseado na Curva de Koch.

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
        frente(comprimento)
    elif niveis > 0:
        comprimento /= 3
        niveis -= 1
        angulo_externo = 360 / lados
        angulo_interno = 180 - angulo_externo

        # 1o segmento
        segmento_koch(comprimento, niveis, lados)
        direita(angulo_interno)

        # 2o "segmento" (polígono regular sem o "lado base")
        for _ in range(lados - 1):
            segmento_koch(comprimento, niveis, lados)
            esquerda(angulo_externo)

        # 3o segmento
        direita(180)
        segmento_koch(comprimento, niveis, lados)


def poligono_de_koch(lados, comprimento, niveis=0):
    angulo_externo = 360 / lados
    for _ in range(lados):
        segmento_koch(comprimento, niveis, lados)
        esquerda(angulo_externo)


# def main():
#     comprimento = limiar = 400
#     colors = ['#e67c73', '#f7cb4d', '#41b375', '#7baaf7', '#ba67c8']
#     w = len(colors) ** 2

#     penup()
#     goto(-comprimento // 2, -200)
#     pendown()

#     poligono(3, 200, 2)

#     # for i, c in enumerate(colors):
#     #     penup()
#     #     goto(-comprimento // 2, i * i * 20)
#     #     pendown()

#     #     curva(comprimento, i)

#     # for c in colors:
#     #     color(c)

#     #     width(w)
#     #     w /= 2

#     #     poligono(3, comprimento, limiar + 1)

#     #     limiar //= 3

#     exitonclick()
#     # mainloop()  # Mantém a janela aberta


def triangulo_sierpinski(comprimento, niveis=0):
    # https://pt.wikipedia.org/wiki/Tri%C3%A2ngulo_de_Sierpinski
    if niveis == 0:
        poligono(3, comprimento)
    elif niveis > 0:
        comprimento /= 2
        niveis -= 1

        x_offset, y_offset = comprimento / 2, comprimento / 2 * (3 ** 0.5)

        # bottom left
        triangulo_sierpinski(comprimento, niveis)
        # top
        teleporta(x_offset, y_offset)
        triangulo_sierpinski(comprimento, niveis)
        # bottom right
        teleporta(x_offset, -y_offset)
        triangulo_sierpinski(comprimento, niveis)
        # back to origin
        teleporta(-comprimento, 0)


def balao(comprimento, niveis=0):
    if niveis >= 0:
        esquerda(60)
        frente(comprimento)
        direita(120)
        poligono_preenchido(3, comprimento)
        teleporta(comprimento / 2, -comprimento / 2 * (3 ** 0.5))
        esquerda(60)
        tras(comprimento)

        if niveis > 0:
            balao(comprimento / 2, niveis-1)


def tapete_sierpinski(comprimento, niveis=0):
    # https://pt.wikipedia.org/wiki/Tapete_de_Sierpinski
    if niveis >= 0:
        comprimento /= 3

        teleporta(comprimento, comprimento)
        poligono_preenchido(4, comprimento)
        teleporta(-comprimento, -comprimento)

        if niveis > 0:
            niveis -= 1
            for y in range(3):
                for x in range(3):
                    if not (x == y == 1):
                        tapete_sierpinski(comprimento, niveis)
                    teleporta(comprimento)
                teleporta(-3 * comprimento, comprimento)
            teleporta(0, -3 * comprimento)


if __name__ == '__main__':
    # poligono(4, 100, True)
    # poligono(5, 100, 2)
    # poligono(4, 100, 2)
    # poligono(3, 100)
    # poligono_de_koch(3, 200, 2)
    # balao(200, 3)
    # triangulo_sierpinski(200, 4)
    # tapete_sierpinski(200, 2)
    # poligono_preenchido(3, 100, 'blue')
    mantem_janela_aberta()
#     # main()

