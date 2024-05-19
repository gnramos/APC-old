# Números Inteiros em Python

Toda linguagem de programação fornece alguns tipos de dados primitivos (ou embutidos) A linguagem Python define o tipo de dado [`int`](https://docs.python.org/pt-br/3/library/stdtypes.html#numeric-types-int-float-complex) para armazenar números inteiros. As principais operações com inteiros são:

| Operação | Resultado                               | Exemplo      |
|----------|-----------------------------------------|--------------|
| x + y    | soma de x e y                           | 2 + 3 = 5    |
| x - y    | diferença de x e y                      | 3 - 2 = -1   |
| x * y    | produto de x e y                        | 2 * 3 = 6    |
| x / y    | quociente da divisão de x por y         | 2 / 3 = 1.5  |
| x // y   | quociente inteiro da divisão de x por y | 2 // 3 = 1   |
| x % y    | resto da divisão de x por y             | 3 % 2 = 1    |
| -x       | x negado                                | -2           |
| abs(x)   | valor absoluto de x                     | abs(-2) = 2  |
| int(x)   | x convertido em inteiro                 | int(1.5) = 1 |
| x ** y   | x elevado a y                           | 2 ** 3 = 8   |


Na memória, os números são armazenados como complemento de 2, mas Python usa uma abordagem que têm precisão "ilimitada" - um mecanismo que usa quantos bits forem necessários para armazenar corretamente o valor. Isso permite que se lide com números muito grandes mas, obviamente, o magnitude máxima ainda está limitada à quantidade da memória disponível.

``` python title="Inteiro em Python"

inteiro_32 = 42
inteiro_64 = - 2 ** 63
inteiro_super_longo = - 2 ** 1000
```

# Números Reais em Python

O tipo de dado [`float`](https://docs.python.org/pt-br/3/library/stdtypes.html#numeric-types-int-float-complex) para armazenar números reais em 64 bits. As principais operações com inteiros são:

| Operação | Resultado                               | Exemplo            |
|----------|-----------------------------------------|--------------------|
| x + y    | soma de x e y                           | 2.5 + 3.25 = 5.25  |
| x - y    | diferença de x e y                      | 3.5 - 2.75 = -0.75 |
| x * y    | produto de x e y                        | 2.5 * 3.0 = 7.5    |
| x / y    | quociente da divisão de x por y         | 2.0 / 3.0 = 1.5    |
| x // y   | quociente inteiro da divisão de x por y | 2.0 // 3.0 = 1     |
| x % y    | resto da divisão de x por y             | 7.5 % 3.0 = 1.5    |
| -x       | x negado                                | -2.5               |
| abs(x)   | valor absoluto de x                     | abs(-2.5) = 2.5    |
| float(x) | x convertido em ponto flutuante         | float(1) = 1.0     |
| x ** y   | x elevado a y                           | .64 ** .5 = 0.8    |