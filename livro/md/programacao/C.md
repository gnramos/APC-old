# Números Inteiros em C

Toda linguagem de programação fornece alguns tipos de dados primitivos (ou embutidos) A linguagem C define o tipo de dado `int` para armazenar números inteiros. As principais operações com inteiros são:

| Operação | Resultado                               | Exemplo    |
|----------|-----------------------------------------|------------|
| x + y    | soma de x e y                           | 2 + 3 = 5  |
| x - y    | diferença de x e y                      | 3 - 2 = -1 |
| x * y    | produto de x e y                        | 2 * 3 = 6  |
| x / y    | quociente inteiro da divisão de x por y | 2 / 3 = 1  |
| x % y    | resto da divisão de x por y             | 3 % 2 = 1  |
| -x       | x negado                                | -2         |


Na memória, os números são armazenados como complemento de 2 em 32 bits, portanto os valores são limitados ao intervalo $[-2^{31}, 2^{31}) = [-2147483648, 2147483648)$. Adicionalmente, C fornece dois modificadores, `unsigned`, que determina que valor armazenado é sempre positivo e usa o bit de sinal para a magnitude (o valor está em $[0, 2^{32}) = [0, 4294967296)$); e `long` que duplica a quantidade de bits para armazenagem (valor em $[-2^{63}, 2^{63})).

``` C title="Inteiro em C"

int inteiro_32 = -42;
unsigned int inteiro_32_sem_sinal = 42;
long int inteiro_64 = 9000000000; /* 9 bilhões */
```
