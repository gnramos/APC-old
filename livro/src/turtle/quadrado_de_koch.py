from turtle import mainloop, goto, penup, pendown
from turtle import forward as linha, left as esquerda, right as direita


def quadrado_de_koch(comprimento, limiar=8):
    if comprimento < limiar:
        linha(comprimento)             # ________
    else:
        comprimento /= 4

        quadrado_de_koch(comprimento)  # __

        esquerda(90)
        quadrado_de_koch(comprimento)  # __|

        direita(90)                    #    __
        quadrado_de_koch(comprimento)  # __|

        direita(90)                    #    __
        quadrado_de_koch(comprimento)  # __|  |

        esquerda(90)                   #    __
        quadrado_de_koch(comprimento)  # __|  |__


def main():
    COMPRIMENTO = 400

    penup()
    goto(-COMPRIMENTO // 4, COMPRIMENTO // 4)
    pendown()

    for _ in range(4):
        quadrado_de_koch(COMPRIMENTO)
        direita(90)

    mainloop()  # Mantém a janela aberta


if __name__ == '__main__':
    main()
