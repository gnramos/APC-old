'''Versão em português das principais funções do módulo turtle.

https://docs.python.org/pt-br/3/library/turtle.html
'''


# https://medium.com/reflex%C3%A3o-computacional/m%C3%B3dulo-turtle-d8949db55008
# https://panda.ime.usp.br/pensepy/static/pensepy/index.html
# https://www.youtube.com/watch?v=bG_CCUOKruU&list=PLZtiWWeAdZkC5IMbxmzPYu05auGDGp0Km

import turtle

# 'addshape', 'begin_poly', 'bgcolor', 'bgpic', bye', 'clear',
# 'clearscreen', 'clearstamp', 'clearstamps', 'clone', 'color', 'colormode',
# 'config_dict', 'deepcopy', 'degrees', 'delay', 'distance', 'done', 'dot',
# 'end_poly', 'exitonclick', 'fd', 'fillcolor', 'filling',
# 'forward', 'get_poly', 'get_shapepoly', 'getcanvas', 'getmethparlist',
# 'getpen', 'getscreen', 'getshapes', 'getturtle', 'heading',
# 'hideturtle', 'ht', 'inspect', 'isdown', 'isfile', 'isvisible',
# 'join', 'listen', 'math', 'mode', 'numinput',
# 'onclick', 'ondrag', 'onkey', 'onkeypress', 'onkeyrelease', 'onrelease',
# 'onscreenclick', 'ontimer', 'pen', 'pencolor', 'radians',
# 'read_docstrings', 'readconfig', 'register_shape', 'reset', 'resetscreen',
# 'resizemode', 'screensize', 'seth', 'setheading', 'setpos',
# 'setposition', 'settiltangle', 'setundobuffer', 'setup', 'setworldcoordinates',
# 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor',
# 'showturtle', 'simpledialog', 'speed', 'split', 'st', 'stamp', 'sys',
# 'textinput', 'tilt', 'tiltangle', 'time', 'title', 'towards', 'tracer',
# 'turtles', 'turtlesize', 'types', 'undo', 'undobufferentries', 'update',
# 'window_height', 'window_width', 'write', 'write_docstringdict', 'xcor', 'ycor']

traduz = {
    'direita': 'turtle.right',
    'esquerda': 'turtle.left',
    'frente': 'turtle.forward',
    'tras': 'turtle.backward',

    'origem': 'turtle.home',
    'posicao': 'turtle.position',
    'vai_para': 'turtle.goto',

    'abaixa_caneta': 'turtle.pendown',
    'cor': 'turtle.color',
    'largura': 'turtle.pensize',
    'levanta_caneta': 'turtle.penup',

    'inicia_preenchimento': 'turtle.begin_fill',
    'termina__preenchimento': 'turtle.end_fill',

    'circulo': 'turtle.circle',

    'mantem_janela_aberta': 'turtle.mainloop',
    }

for pt, en in traduz.items():
    exec(f'{pt} = {en}')


def poligono(lados, comprimento):
    """Desenha um polígono regular.

    Args:
      - lados: o número de lados do polígono.
      - comprimento: o tamanho de cada lado.
    """
    if lados < 3:
        raise ValueError(f'Não é possível desenhar um polígono com {lados} lados.')
    if comprimento < 1:
        raise ValueError('Não é possível desenhar um polígono com lados menor que 1.')

    angulo_externo = 360 / lados
    for _ in range(lados):
        frente(comprimento)
        esquerda(angulo_externo)


def poligono_preenchido(lados, comprimento, str_cor=None):
    """Desenha um polígono regular com preenchimento.

    Args:
      - lados: o número de lados do polígono.
      - comprimento: o tamanho de cada lado.
    """
    try:
        cor_atual, preenchimento_atual = cor()
        if str_cor:
            cor(str_cor)
        inicia_preenchimento()
        poligono(lados, comprimento)
    finally:
        termina__preenchimento()
        if str_cor:
            cor(cor_atual, preenchimento_atual)


def teleporta(offset_x, offset_y=0):
    """Desloca a caneta sem desenhar.

    Args:
      - offset_x: a distância do deslocamento no eixo X.
      - offset_y: a distância do deslocamento no eixo Y.
    """
    levanta_caneta()
    x, y = posicao()
    vai_para(x + offset_x, y + offset_y)
    abaixa_caneta()
