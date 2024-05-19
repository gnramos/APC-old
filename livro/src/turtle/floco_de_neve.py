from turtle import mainloop, goto, penup, pendown, forward as linha, left as gira


COMPRIMENTO = 300

penup()
goto(-COMPRIMENTO // 2, COMPRIMENTO // 3)
pendown()


def curva_de_koch(comprimento):
    # https://pt.wikipedia.org/wiki/Curva_de_Koch
    if comprimento < 6:
        linha(comprimento)          # ______
    else:
        comprimento /= 3

        curva_de_koch(comprimento)  # __

        gira(60)
        curva_de_koch(comprimento)  # __/

        gira(-120)
        curva_de_koch(comprimento)  # __/\

        gira(60)
        curva_de_koch(comprimento)  # __/\__


# Floco de neve (3 curvas de Koch formando um "triângulo equilátero")
for _ in range(3):
    curva_de_koch(COMPRIMENTO)
    gira(-120)

mainloop()  # Mantém a janela aberta
