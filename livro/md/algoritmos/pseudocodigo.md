## Pseudocódigo

Outra abordagem bem interessante, pois visa diminuir o esforço de traduzir um algoritmo computacional em instruções que um computador possa usar. Utiliza termos simples e estruturas de uma linguagem de programação, mas com sintaxe e regras menos restritivas. Por exemplo, o algoritmo abaixo em pseudocódigo.

``` title="Média Aritmética"
Início
    Leia [nota_1]
    Leia [nota_2]
    Leia [nota_3]
    Leia [nota_4]
    média  = (nota_1 + nota_2 + nota_3 + nota_4) ÷ 4
    Escreva o valor da [média]
Fim
```

Note que o algoritmo da média em pseudocódigo começa e termina com duas palavras, `Início` e `Fim`. Estas, como as palavras `Leia` e `Escreva`, pertencem ao que chamamos de *vocabulário controlado*. O uso deste um conjunto mais restrito de palavras possibilita maior precisão e eficácia na comunicação das instruções.

Outro diferencial é a consideração de nomear as informações, de modo a poder recuperá-las em passos subsequentes. Por exemplo, a segunda instrução obtém um valor (comunicação de um dado) e lhe atribui um nome (`nota_1`); que é recuperado no momento de calcular a soma dos números, na sexta instrução.

Por fim, note também que as linhas com as instruções de cada passo do algoritmo estão deslocadas para a direita em relação às palavras destacadas, ressaltando o conjunto de instruções dentro do bloco definido por elas. Este deslocamento é denominado *endentação*, e facilita a visualização da estrutura do algoritmo.

Este detalhamento das instruções implica que o algoritmo com [média em pseudocódigo](#alg-media4-pseudo) ficou mais extenso e menos "natural" que o mesmo processo descrito no da [média detalhada](#alg-media4-natural-detalhado), mas é bem melhor definido e continua sendo de fácil entendimento. Além disso, se aproxima mais da forma de representar um algoritmo como uma linguagem de programação.
