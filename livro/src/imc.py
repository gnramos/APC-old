def calcula_imc(m, h):
    return m / (h * h)


def avalia_imc(m, h):
    imc = calcula_imc(m, h)
    if imc < 18.5:
        print('Situação de magreza!')
    elif imc < 25:
        print('Situação normal.')
    elif imc < 30:
        print('Situação de sobrepeso.')
    elif imc < 40:
        print('Situação de obesidade!')
    else:
        print('Situação de obesidade grave!!')
