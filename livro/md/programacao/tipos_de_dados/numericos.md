<h2>Números</h2>

Um *número* é um objeto matemático usado para descrever uma quantidade, e uma *base numérica* é um conjunto de algarismos utilizados para representar um número. Quais são os símbolos e as regras de como utilizá-los são definidos pelos sistema de numeração usado. O valor de um número é único, mas sua representação pode variar conforme o sistema utilizado - é fácil ilustrar isso comparando o abordagem usamos normalmente, com [algarismos arábicos](https://pt.wikipedia.org/wiki/Algarismos_ar%C3%A1bicos) e a [notação posicional](https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_posicional), à abordagem que os [antigos romanos](https://pt.wikipedia.org/wiki/Numera%C3%A7%C3%A3o_romana) usavam. Para o valor quarenta e nove, temos as representações $49$ e $XLIX$, respectivamente.

Na notação posicional, o valor representado por um algarismo depende da posição em que ele se encontra no conjunto de símbolos que representa o número, sendo valores a esquerda mais influentes que os a direita. O valor deste número é determinado pela soma dos valores relativos de cada algarismo. Por exemplo: 123 = 100 + 20 + 3, o algarismo mais a esquerda (1) tem uma influência maior que os demais no valor, e é considerado o mais significativo. O algarismo seguinte (2) tem uma influência menor que o anterior, mas maior que o seguinte. Isso se sucede até o último algarismo, o mais a direita, que é chamado de menos significativo. Podemos reescrever a informação da seguinte forma:

$$123 = 100 + 20 + 3 = 1·10^2+ 2·10^1+ 3·10^0$$

Nesta representação, duas coisas se destacam. A primeira é que a influência de cada algarismo é determinada por uma potência de 10, que é a base numérica. A segunda, é que esta potência é uma sequência crescente da posição menos significativa para a mais significativa, iniciando-se por 0. De forma mais genérica, um algarismo $A$ tem uma influência proporcional a sua posição $i$ para uma base numérica $B$.

$$A·{B^i}$$

No valor 123, na [base decimal](https://pt.wikipedia.org/wiki/Sistema_de_numera%C3%A7%C3%A3o_decimal), entendemos seu valor pela soma de seus componentes. O algarismo 3 está na posição mais a direita, considerada como posição $i = 0$, portanto seu peso no valor resultante é de 3·10$^0$. A posição seguinte (a esquerda) é i = 1 com o algarismo 2, acrescentando 2·10$^1$ ao resultado. O último algarismo (mais a esquerda) é 1 e está na posição 2, acrescentando 1·10$^2$. De forma genérica, o valor de um número em uma base numérica $B$ qualquer, representado com $n$ algarismos $A_i : A \in [0, B), i \in [0, n)$, é calculado com a seguinte fórmula:

$$A_{n-1}A_{n-2}…{A_2}A_1A_0 = \sum\limits_{i=0}^{n - 1}{A_i·{B^i}}$$

Para representar a informação numérica na memória do computador, ela necessariamente deve ser representada como um conjunto de bits. Isto é relativamente simples, o bit tem dois estados, 0/1 que são os algarismos da *[base numérica binária](https://pt.wikipedia.org/wiki/Sistema_de_numera%C3%A7%C3%A3o_bin%C3%A1rio)*. Portanto, podemos usar esta base na notação posicional para basta representar um valor numérico qualquer como bits na memória. Como também usaremos algarismos arábicos, para diferenciar as bases numéricas acrescentamos um sufixo ao número.

$$1101_2 = 1·2^3+ 1·2^2+ 0·2^1+ 1·2^0 = 8 + 4 + 0 + 1 = 13_{10}$$

Por ser uma base de valor baixo, são poucos os algarismos e, portanto, as representações dos números se tornam extensas. Outras bases de valor mais elevado permitem compactar isso, e as mais úteis são as múltiplas de 2 já que a [conversão](https://pt.wikipedia.org/wiki/Convers%C3%A3o_de_base_num%C3%A9rica) delas para a binária é simplificada. A tabela abaixo mostra alguns valores nas bases mais comuns na computação: binária, [octal](https://pt.wikipedia.org/wiki/Sistema_octal), decimal e [hexadecimal](https://pt.wikipedia.org/wiki/Sistema_de_numera%C3%A7%C3%A3o_hexadecimal). Note que, como a notação posicional utiliza apenas um símbolo por posição, a base hexadecimal define os valores superiores a 9 (o maior algarismo arábico) para letras do alfabeto latino.

<center>

| binária | octal | decimal | hexadecimal |
|---------|-------|---------|-------------|
| 0       | 0     | 0       | 0           |
| 1       | 1     | 1       | 1           |
| 10      | 2     | 2       | 2           |
| 11      | 3     | 3       | 3           |
| 100     | 4     | 4       | 4           |
| 101     | 5     | 5       | 5           |
| 110     | 6     | 6       | 6           |
| 111     | 7     | 7       | 7           |
| 1000    | 10    | 8       | 8           |
| 1001    | 11    | 9       | 9           |
| 1010    | 12    | 10      | A           |
| 1011    | 13    | 11      | B           |
| 1100    | 14    | 12      | C           |
| 1101    | 15    | 13      | D           |
| 1110    | 16    | 14      | E           |
| 1111    | 17    | 15      | F           |
| 101010  | 52    | 42      | 2A          |
| 1111011 | 173   | 123     | 7B          |

</center>

{! programacao/tipos_de_dados/inteiros.md !}

{! programacao/tipos_de_dados/reais.md !}