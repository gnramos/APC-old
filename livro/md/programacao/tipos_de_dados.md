# Estruturas de Dados

!!! quote "[David Jones](http://www0.cs.ucl.ac.uk/staff/D.Jones/)"

    Acerte as estruturas de dados primeiro, e o resto do programa se escreverá sozinho.

Todo processo no computador gerencia a execução de um programa armazenado, a implementação de um algoritmo computacional nãos sendo, portanto, possível dissociar um algoritmo de dados manipulados - o próprio programa é um conjunto de dados (as instruções). Além disso, praticamente todos os programas manipulas dados fornecidos e gerados no processamento, na forma de variáveis ou constantes, que são os objetos de dados básicos manipulados em um programa[@Kernighan1989].

O forma como organizamos estes dados tem impacto direto no desempenho do computador. Ao executar um algoritmo computacional, estamos exigindo esforço da máquina para realizar o trabalho de processamento. Este esforço depende da quantidade de instruções sendo executadas, e do custo de cada instruções (podemos ter instruções mais simples e baratas, e instruções mais complexas e caras). A organização dos dados tem impacto direto neste esforço, e buscamos deixá-los organizados de forma a tornar o processo menos custoso. Por exemplo, imagine que seu problema é interpretar números e somá-los, é muito mais fácil[^1] fazer isso se lhe forem apresentados os números estruturados como $49$ e $1$ (com resultado $50$) que se fossem como $XLIX$ e $I$ (também com resultado $L$).

A memória do computador é um conjunto ordenado de bits, ou seja, toda informação é armazenada como zeros e uns e há uma ordem posicional entre eles (existe um primeiro bit, que pode ser `0/1`, um segundo bit que também pode ser `0/1`, e assim sucessivamente até um último bit). Para facilitar, há uma [nomenclatura específica](http://pt.wikipedia.org/wiki/Byte) para lidar com a quantidade de bits sendo 1 byte (8 bits) a unidade mais comum para quantificá-lo. A composição de bits permite representar mais estados; 2 bits são 4 estados (<code>00/01/11/10</code>), 3 bits definem 8 estados, e assim sucessivamente - havendo $n$ bits podemos definir $2^n$ estados distintos. O significado da informação armazenada depende da forma de interpretar estes bits, um mesmo conjunto de bits tem significados diferentes se for interpretado como um número, um símbolo ou outra coisa. Por exemplo, um byte pode assumir um de 256 valores numéricos diferentes, mas também pode representar inúmeras informações diferentes se mudarmos a forma de interpretá-lo.

![Diferentes interpretações para 1 byte](/img/byte_interpretacao.png "Diferentes interpretações para 1 byte"){ width="75%" }

A representação do dado é necessariamente binária mas a interpretação dos bits é o que define a informação. Esta interpretação é determinada pelo *tipo de dado*, e cada tipo tem suas características específicas definidas pela linguagem de programação. Por exemplo, o conjunto de bits <code>01000001001000000000000000000000</code> pode ser interpretado como o valor numérico do tipo inteiro 1092616192, como o valor numérico do tipo real 10.0 ou como um tipo simbólico <code>A</code> ([ASCII](https://pt.wikipedia.org/wiki/ascii)). Estes três tipos de dados, entre outros, geralmente estão presentes em qualquer linguagem de programação.

!!! note

    Como um mesmo conjunto de bits pode ser interpretado de diferentes formas, é preciso saber que tipo de dado foi armazenado na memória para interpretá-lo corretamente.

Um *[id> tipo abstrato de dado]* (TAD) determina um tipo de dado e as operações definidas sobre ele, delimitando assim a quantidade de informação necessária para manipulação dos valores pelo computador e, consequentemente, facilitando a programação. Por exemplo, o conjunto de números naturais $\mathbb{N}$ e suas operações (como $+, -, /, *$) é um TAD.

!!! info "Estrutura de Dados"

    Forma concreta de se implementar um tipo abstrato de dados em uma linguagem de programação, de modo a organizar os dados na memória para facilitar o acesso e a manipulação destes.

Portanto, para cada linguagem de programação específica, o tipo do dado determina:

1. o significado do valor armazenado;
1. como o valor é armazenado nos bits;
1. quais os possíveis valores que podem ser armazenados; e
1. quais as operações podem ser realizadas com o valor.

!!! note

    As características de uma estrutura de dados específica são importantes pois determinam o que pode e também o que **não** pode ser feito com ela.

{! programacao/tipos_de_dados/numericos.md !}

{! programacao/tipos_de_dados/simbolicos.md !}

{! programacao/tipos_de_dados/booleanos.md !}

{! programacao/tipos_de_dados/exercicios.md !}

[^1]: Exceto se você for um antigo romano...
