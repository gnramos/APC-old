### Números Inteiros

Já vimos a representação dos [números naturais](https://pt.wikipedia.org/wiki/N%C3%BAmero_natural) em binário. Entretanto, muitas problemas lidam com os [números inteiros](https://pt.wikipedia.org/wiki/N%C3%BAmero_inteiro), que podem ter valores negativos. Felizmente, um número só pode ser negativo ou não, ou seja, a informação do sinal é facilmente representada em um bit. A convenção é que o bit mais a esquerda armazena a informação se o número é negativo (ligado/1) ou se é positivo (desligado/0), e os demais bits armazenam a informação do valor do número. Há formas distintas de se interpretar este último conjunto de bits, como listadas a seguir.

[Sinal e Magnitude](https://pt.wikipedia.org/wiki/Representa%C3%A7%C3%A3o_de_n%C3%BAmeros_com_sinal#M.C3.A9todo_sinal-e-magnitude), onde o bit mais significativo indica o sinal e os demais bits determinam o valor diretamente pela notação posicional (como um número natural). Esta abordagem é intuitivamente simples para entendermos.

<center>

| bits    | sinal | notação posicional | decimal |
|---------|-------|--------------------|---------|
| **0**00 | +00   | $+(0·2^1+ 0·2^0)$  | +0      |
| **0**01 | +01   | $+(0·2^1+ 1·2^0)$  | +1      |
| **0**10 | +10   | $+(1·2^1+ 0·2^0)$  | +2      |
| **0**11 | +11   | $+(1·2^1+ 1·2^0)$  | +3      |
| **1**00 | -00   | $-(0·2^1+ 0·2^0)$  | -0      |
| **1**01 | -01   | $-(0·2^1+ 1·2^0)$  | -1      |
| **1**10 | -10   | $-(1·2^1+ 0·2^0)$  | -2      |
| **1**11 | -11   | $-(1·2^1+ 1·2^0)$  | -3      |

</center>

[Complemento de um](https://pt.wikipedia.org/wiki/Representa%C3%A7%C3%A3o_de_n%C3%BAmeros_com_sinal#Complemento_para_um) também considera o bit mais a esquerda como indicador de sinal e os demais para o valor, conforme o sinal. Se *positivo*, os bits restantes indicam o valor pela notação posicional (como na abordagem de sinal e magnitude); se *negativo*, é preciso inverter todos os bits antes de considerar a notação posicional. Esta variação é um pouco mais complexa para entendermos, mas tem vantagens quanto à anterior para algumas operações. Uma delas é que precisa-se de menos esforço para para inverter o sinal de um valor, uma operação muito frequente em problemas computacionais. Usando complemento de um, basta inverter todos os bits.

<center>

| bits    | sinal | inverte? |     | notação posicional | decimal |
|---------|-------|----------|-----|--------------------|---------|
| **0**00 | +00   | não      | +00 | $+(0·2^1+ 0·2^0)$  | +0      |
| **0**01 | +01   | não      | +01 | $+(0·2^1+ 1·2^0)$  | +1      |
| **0**10 | +10   | não      | +10 | $+(1·2^1+ 0·2^0)$  | +2      |
| **0**11 | +11   | não      | +11 | $+(1·2^1+ 1·2^0)$  | +3      |
| **1**00 | -00   | sim      | -11 | $-(1·2^1+ 1·2^0)$  | -3      |
| **1**01 | -01   | sim      | -10 | $-(1·2^1+ 0·2^0)$  | -2      |
| **1**10 | -10   | sim      | -01 | $-(0·2^1+ 1·2^0)$  | -1      |
| **1**11 | -11   | sim      | -00 | $-(0·2^1+ 0·2^0)$  | -0      |

</center>

Por fim, a forma mais utilizada é [complemento de dois](https://pt.wikipedia.org/wiki/Complemento_para_dois). Nela, também o bit mais a esquerda define o sinal e os demais determinam o valor conforme o sinal. Se *positivo*, os bits restantes indicam o valor pela notação posicional; se *negativo*, é preciso inverter todos os bits e incrementar em 1 o resultado antes de considerar a notação posicional. Embora mais complicada para nós, esta abordagem tem vantagens sobre as demais, como quantidade de valores distintos que se pode armazenar e facilidade na computação de operações aritméticas.

<center>

| bits    | sinal | inverte? |     |  +1 |      | notação posicional       | decimal |
|---------|-------|----------|-----|-----|------|--------------------------|---------|
| **0**00 | +00   | não      | +00 | não | +00  | $+(0·2^1+ 0·2^0)$        | +0      |
| **0**01 | +01   | não      | +01 | não | +01  | $+(0·2^1+ 1·2^0)$        | +1      |
| **0**10 | +10   | não      | +10 | não | +10  | $+(1·2^1+ 0·2^0)$        | +2      |
| **0**11 | +11   | não      | +11 | não | +11  | $+(1·2^1+ 1·2^0)$        | +3      |
| **1**00 | -00   | sim      | -11 | sim | -100 | $-(1·2^2+ 0·2^1+ 0·2^0)$ | -4      |
| **1**01 | -01   | sim      | -10 | sim | -011 | $-(0·2^2+ 1·2^1+ 1·2^0)$ | -3      |
| **1**10 | -10   | sim      | -01 | sim | -010 | $-(0·2^2+ 1·2^1+ 0·2^0)$ | -2      |
| **1**11 | -11   | sim      | -00 | sim | -001 | $-(0·2^2+ 0·2^1+ 1·2^0)$ | -1      |

</center>

Geralmente, valores inteiros são armazenados em um tipo de dado `inteiro` de 32 ou 64 bits. Considerando o primeiro caso, a estrutura de dados para complemento de dois determina:

1. O significado é de um valor numérico inteiro, que pode ser negativo.
1. O valor é armazenado como Complemento de 2 nos 32 bits.
1. Os possíveis valores armazenados estão no intervalo $[-2^{31}, 2^{31})$.
1. As operações aritméticas básicas ($+, -, \times\ e\ \div$) estão definidas na linguagem de programação - e possivelmente outras.
