<h2>Exercícios</h2>

??? question "Dado um número não negativo qualquer na base hexadecimal, descreva o algoritmos para transformá-lo em um número binário."

    Como a base 16 é múltipla de 2, o processo manual é bem simples. Cada algarismo hexadecimal pode ser diretamente mapeado para seu valor binário de 4 bits, na mesma ordem. Por exemplo, para $2A_{16}$ temos que $2_{16} \rightarrow 0010_2$ e $A_{16} \rightarrow 1010_2$, portanto $2A_{16}\rightarrow 00101010_2$.

??? question "Dado um número não negativo qualquer na base hexadecimal, descreva o algoritmos para transformá-lo em um número binário."

    Como a base 16 é múltipla de 2, o processo manual é bem simples. Cada algarismo hexadecimal pode ser diretamente mapeado para seu valor binário de 4 bits, na mesma ordem. Por exemplo, para $2A_{16}$ temos que $2_{16} \rightarrow 0010_2$ e $A_{16} \rightarrow 1010_2$, portanto $2A_{16}\rightarrow 00101010_2$.

??? question "Dado um número não negativo qualquer na base decimal, descreva o algoritmos para transformá-lo em um número binário."

    Como a base 10 não é múltipla de 2, o processo manual é mais complicado que com as bases hexadecimal ou octal. Uma das abordagens é a de [divisões sucessivas](https://pt.wikipedia.org/wiki/Convers%C3%A3o_de_base_num%C3%A9rica#Convers%C3%A3o_de_decimal_para_bin%C3%A1rio), onde se divide o número por 2, anotando o valor do resto (necessariamente um algarismo binário). Esse processo é repetido para o resultado inteiro da divisão, até que haja um resultado da divisão que seja zero. Neste ponto, juntam-se os valores dos restos anotados e inverte-se a ordem deles - o resultado será representação do número decimal na base binária. Por exemplo: $13_{10} / 2 = 6$ (resto 1); $6_{10} / 2 = 3$ (resto 0); $3_{10} / 2 = 1$ (resto 1); $1_{10} / 2 = 0$ (resto 1). A sequência de restos é $1011$, invertida se torna $1101_2 = 1·2$^3$+ 1·2$^2$+ 1·2$^0$= 8 + 4 + 1$.

??? question "Dados os bits `11`, qual o valor inteiro armazenado considerando apenas o sistema posicional, sinal e magnitude, complemento de 1 e complemento de 2?"

    * Sistema posicional: $11_2 = 1·2$^1$+ 1·2$^0$= 2 + 1 = 3_{10}$
    * Sinal e magnitude:  $11_2 = -1_2 = -1·2$^0$= -1_{10}$
    * Complemento de um:  $11_2 = -1_2 \overset{inv}{\rightarrow} -0_2 = -0·2$^0$= -0_{10}$
    * Complemento de dois:  $11_2 = -1_2 \overset{inv}{\rightarrow} -0_2 \overset{+1}{\rightarrow} -1_2 = -1·2$^0$= -1_{10}$

??? question "Quais os 4 pontos principais definidos quando consideramos 8 bits para armazenar uma estrutura de dados do tipo `inteiro`?"

    1. O significado é de um valor numérico inteiro, que pode ser negativo.
    1. O valor é armazenado como Complemento de 2 nos 8 bits.
    1. Os possíveis valores armazenados estão no intervalo $[-2^7, 2^7) \equiv [-128, 128)$.
    1. As operações aritméticas básicas ($+, -, \times e \div$) estão definidas na linguagem de programação - e possivelmente outras.

??? question "Considerando 4 bits para armazenar um valor inteiro como complemento de 2, o que acontece computar a operação $5 + 4$?"

    Supondo 4 bits, os valores possíveis de serem armazenados são [-8, 7). Ao somar 4 (`0101`) e 4 (`0100`), o resultado seria 9 (`1001`). Entretanto, como a representação é de complemento de 2, `1001` é interpretado como -7, um resultado incorreto. O valor calculado ultrapassa a capacidade da representação (*overflow*), e o resultado não é o esperado.

??? question "Considerando 4 bits para armazenar um número real como ponto fixo, determine qual a representação do valor $1,25_{10}$ como $Q1.3$, $Q2.2$ e $Q3.1$. "

    * $Q1.3 \Rightarrow 1,25_{10} = 1\cdot2^0 + 0\cdot2^{-1} + 1\cdot2^{-2} + 0\cdot2^{-3} = 1010_2$
    * $Q2.2 \Rightarrow 1,25_{10} = 0\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 1\cdot2^{-2} = 0101_2$
    * $Q3.1$ não é adequado para este valor. Tem-se duas possibilidades:
        * $1,25_{10} \approx 0\cdot2^2 + 0\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 1\cdot2^{-2} = 0001_2 (=1,5_{10})$
        * $1,25_{10} \approx 0\cdot2^2 + 0\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 0\cdot2^{-2} = 0010_2 (=1,0_{10})$

??? question "Se todo número inteiro também é um número real, por que as linguagens de programação oferecem o tipo de dado `int` quando existe o tipo de dado `float`?"

    A manipulação de um `float` é mais complexa que a de um `int`, e nos computadores antigos essa complexidade implicava em uma grande diferença de desempenho nas operações, principalmente aritméticas - era bem mais eficiente usar `int`. Nos computadores modernos, a situação é bem mais difusa e muito dependente dos detalhes de uso tanto do algoritmo quanto da linguagem de programação quanto do hardware.

??? question "Se todo número inteiro também é um número real, por que as linguagens de programação oferecem o tipo de dado `int` quando existe o tipo de dado `float`?"

    A manipulação de um `float`
