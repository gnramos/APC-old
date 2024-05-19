### Números Reais

Os [números reais](https://pt.wikipedia.org/wiki/N%C3%BAmero_real) também podem ser representados como binários pelo sistema posicional, basta estender a lógica da notação posicional. Por exemplo, considere o seguinte número decimal:

$$13,125 = 1\cdot{10^1} + 3\cdot{10^0} + 1\cdot{10^{-1}} + 2\cdot{10^{-2}} + 5\cdot{10^{-3}}$$

Este valor pode ser representado com a mesma lógica em 7 bits:

$$1\cdot2^3 + 1\cdot2^2 + 0\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 0\cdot2^{-2} + 1\cdot2^{-3} = 1101,001_2$$

Neste caso usamos 4 bits para o valor inteiro e 3 para o valor fracionário.

<h4>Ponto Fixo</h4>

A representação com [ponto fixo](https://en.wikipedia.org/wiki/Fixed-point_arithmetic) define que, dada uma quantidade $Q$ de bits para representar o número, há uma quantidade fixa $m$ de bits que armazenam a parte inteira e outra quantidade $f$ que armazena a parte fracionária do número (tais que $Q = m + f$). Por exemplo, supondo $Qm.f = Q5.3$, o número 13,125 seria representado pelos bits `01101001` cujo valor é interpretado como `01101,001`. Supondo $Q4.4$, este mesmo valor é representado por `11010010`.

O ponto fixo é uma convenção interessante, mas pouco flexível. Como toda estrutura de dados, a quantidade de bits limita os valores que podem ser armazenado, portanto uma configuração $Qm.f$ que pode ser adequada para uma aplicação específica pode ser inadequada para outra. Por exemplo, considerando que $Q=8$, uma representação $Q0.7$ é mais interessante para lidar com o tamanho de componentes eletrônicos que a $Q5.3$. Desta forma, fica inviável determinar um padrão para ponto fixo que seja suficiente para a maioria das aplicações.

<h4>Ponto Flutuante</h4>

Como alternativa mas flexível, temos a representação em [ponto flutuante](https://pt.wikipedia.org/wiki/Ponto_flutuante) que se baseia na ideia da [notação científica](https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_cient%C3%ADfica) onde qualquer número pode ser representado no mesmo formato em duas componentes, separando valor numérico de sua grandeza. Dada uma *mantissa* ($m$) composta por algarismos que determinam o valor do número e um *expoente* ($e$) que determina sua grandeza, um número qualquer na base $B$ pode ser representado da seguinte forma:

$$m\cdot{B}^{e}$$

Por exemplo:

$$0,13125\cdot10^2 = 13,125_{10} \Longleftrightarrow 1101,001_2 = 0,1101001\cdot2^4$$

Esta representação oferece maior flexibilidade e alcance de valores. O padrão usado nos computadores modernos é o [IEEE 754](https://pt.wikipedia.org/wiki/Instituto_de_Engenheiros_Eletricistas_e_Eletr%C3%B4nicos#IEEE_754), que define o valor armazenado considerando um conjunto de bits de tamanho fixo em três partes: um bit para determinar o sinal, seguido de $e$ bits para o valor do expoente, seguido de $m$ bits para a mantissa. Esta abordagem permite que se use quaisquer quantidades de bits mas usualmente temos a precisão simples (32 bits em blocos de 1/8/23) e dupla (64 bits, em blocos de 1/11/52). O valor armazenado pode ser obtido pelo valor numérico simples de cada bloco desta forma:

$$(-1)^{s}\cdot1,m\cdot2^{e-offset}$$

O *offset* depende da quantidade de bits de *e*, sendo calculado como $2^{e-1}-1$. Para as precisões simples e dupla, temos os valores 127 e 1023, respectivamente. Por exemplo, para precisão simples temos que:

| sinal | expoente | mantissa                | fórmula                         | valor         |
|-------|----------|-------------------------|---------------------------------|---------------|
|   1   | 01111110 | 10000000000000000000000 | $(-1)^{1}\cdot1,1\cdot2^{-1}$   | $-0,75_{10}$  |
|   0   | 10000010 | 10100100000000000000000 | $(-1)^{0}\cdot1,101001\cdot2^3$ | $13,125_{10}$ |


O uso de ponto flutuante oferece diversas vantagens, principalmente a representação de valores absolutos muito grandes ou pequenos[@Tenenbaum1995], mas há limitações. O conjunto de números reais é infinitamente grande, e não pode ser completamente representado com a quantidade finita de bits disponível na memória, portanto é muito comum que valores em ponto flutuante sejam arredondados ao serem armazenados na quantidade fixa de bits disponível[@Goldberg1991].

Por exemplo, considere a expressão $1 / 3 = 0,33333\dots$. O valor resultante é uma dízima periódica, podemos mostrar matematicamente que $0,\overline{3} + 0,\overline{3} + 0,\overline{3} = 1$. Entretanto, $0,\overline{3}$ é uma expressão matemática com mais informação que "apenas" algarismos, ela determina um valor que não pode ser exatamente representado por uma quantidade fixa de algarismos (ou bits na memória). O que se pode fazer é usar toda a capacidade disponível para armazenar o valor mais próximo possível. Considere que só podemos usar 3 algarismos, então a expressão $0,\overline{3} + 0,\overline{3} + 0,\overline{3}$ se torna $0,33 + 0,33 + 0,33 = 0,99 \neq 1$.

Esta [imprecisão](http://pt.stackoverflow.com/a/11328) tem implicações interessantes pois, para um programa de computador, a expressão $0,1 + 0,1 + 0,1$ não resulta no valor $0,3$! O valor decimal $0,1$ é representado em binário como $0,1\overline{0011}$ até o limite de bits reservados, que é insuficiente para o valor exato. Abaixo, podemos ver as diferenças escolhendo precisões arbitrárias para mostrar um mesmo valor armazenado de $0,1$, bem como o efeito da propagação desta diferença ao longo de diversas operações:

=== "Valor"

    ```python title="Precisão" exec="on"
    --8<-- "float_precisao_valor.py"
    ```

=== "Somatório"

    ```python title="Precisão" exec="on"
    --8<-- "float_precisao_somatorio.py"
    ```

Os efeitos da imprecisão tendem a não ser considerados na maioria das aplicações (que não lidem com isso como as de engenharia/finanças/computação científica). Entretanto, deve-se ter atenção especial pois, apesar da diferença para o valor exato ser "pequena", ela existe e pode causar dificuldades se seu programa liga com algo simples como verificar se $0,1 + 0,2 = 0,3$ (algo bem provável de ocorrer em muitas aplicações). É papel do programador entender a situação e lidar com ela.

Algumas abordagens para com isso são trabalhar com inteiros e evitar comparar diretamente variáveis do tpo `float`. Se necessário, podemos realizar a comparação considerando uma tolerância razoável para a diferença entre os valores: ao invés de $a < b$, usamos $|a - b| < \epsilon$. Também é preciso atentar para acúmulo de imprecisões ao longo de múltiplas computações, pois [podem ser realmente significativos](https://www-users.cse.umn.edu/~arnold/disasters/disasters.html).
