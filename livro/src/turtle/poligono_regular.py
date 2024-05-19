from turtle import mainloop, forward as linha, left as esquerda


comprimento = 100
num_lados = 8

angulo_externo = 360 / num_lados

for _ in range(num_lados):
    linha(comprimento)
    esquerda(angulo_externo)

mainloop()  # Mantém a janela aberta
