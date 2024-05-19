'''Exemplo de aplicação do turtle para desenhar uma "flor".

Programação > Fluxo de Controle > Repetição

Desenha uma flor com "pétalas" de raio L.
'''

L = 70  # mas poderia ser qualquer valor (positivo).
petalas = 6


from tartaruga import *


for i in range(petalas):
    circulo(L)
    direita(360 // petalas)

mantem_janela_aberta()
