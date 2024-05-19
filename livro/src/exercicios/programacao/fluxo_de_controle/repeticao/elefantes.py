'''Solução do exercício "Elefantes".

Programação > Fluxo de Controle > Repetição

Lê a quantidade máxima N de elefantes e apresente a letra da música até que
N (≥1) elefantes incomodem muita gente. Por exemplo, para N = 4:
1 elefante incomoda muita gente...
2 elefantes incomodam, incomodam muito mais!
2 elefantes incomodam muita gente...
3 elefantes incomodam, incomodam, incomodam muito mais! 3 elefantes incomodam muita gente...
4 elefantes incomodam, incomodam, incomodam, incomodam muito mais!
'''

n = int(input('Digite a quantidade de elefantes: '))
print('1 elefante incomoda muita gente...')
print('2 elefantes incomodam, incomodam muito mais!')
for e in range(2, n):
    print(f'{e} elefantes incomodam muita gente...')
    incomodam = ', incomodam' * e
    print(f'{e + 1} elefantes incomodam{incomodam} muito mais!')
