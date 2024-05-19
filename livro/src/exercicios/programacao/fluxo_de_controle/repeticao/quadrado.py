'''Solução do exercício "Quadrado".

Programação > Fluxo de Controle > Repetição

Desenha um quadrado de lado L.
'''

L = 100  # qualquer valor (positivo).

from tartaruga import *


for _ in range(4):
    frente(L)
    direita(90)

mantem_janela_aberta()
