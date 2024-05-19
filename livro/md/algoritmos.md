# Algoritmos

!!! quote "[Thomas H. Cormen](https://en.wikipedia.org/wiki/Thomas_H._Cormen)"

    *Antes de existirem computadores, já havia algoritmos. Mas agora que os computadores existem, há ainda mais algoritmos, e os algoritmos são a base da computação.*

---

*Este capítulo apresenta o conceito de algoritmo e algumas formas de representá-lo. Ao final do texto, espera-se que se tenha um entendimento claro do que envolve este conceito e capacidade de expressar soluções como algoritmos.*

---
Algoritmos são "métodos" ou instruções para realizar uma tarefa. Por exemplo, é relativamente simples seguir os passos de uma receita para obter um bolo, seguir uma rota para chegar ao destino desejado, ou calcular um valor matemático. Para tanto, basta que se consiga entender e realizar cada etapa descrita.

Um algoritmo descreve o processo para se obter um resultado, e espera-se que este resultado seja alcançado independentemente de quem esteja seguindo os passos. Pessoas diferentes seguindo uma mesma receita deveriam produzir o mesmo bolo, chegar ao mesmo local e obter o mesmo valor. Entretanto, seres humanos são muito inteligentes, e conseguem abstrair detalhes e inferir uma série de informações ausentes em sua comunicação. Considere o algoritmo abaixo, a maioria dos recém ingressos à universidade não teria dificuldade em resolvê-lo com sucesso.

``` linguagem_natural title="Média Aritmética"
Leia quatro números e calcule a média aritmética.
```

Apesar da aparente simplicidade, ele apresenta diversas possíveis interpretações. "Leia quatro números" significa ler todos de uma só vez ou um da cada vez? "Calcule a média aritmética" se refere a de todos os números fornecidos, a de parte deles ou a de outros números não especificados? É garantido que a pessoa a realizar a tarefa reconhece o termo "média aritmética"? O que fazer com o resultado calculado?

É possível, portanto, que alguém leia 2357, considere que este valor único é composto por "quatro números" (ignorando que representam apenas um valor), e calcule mentalmente a média aritmética deles como 4 (já que a parte fracionária é "uma conta mais difícil"). Se você esperava que lhe fosse dito o valor exato de 4.25, ficaria desapontado...

Esta variação (e outras possíveis) não parece ser a forma mais óbvia de se resolver o problema, mas nem por isso está errada considerando a forma como as instruções foram apresentadas no algoritmo. A ideia por trás do conceito de algoritmo é descrever um processo de modo que os mesmos resultados possam ser obtidos independentemente de que executa os passos. É fácil enxergar isso considerando uma receita de bolo sendo compartilhada: se for bem detalhada, mesmo uma pessoa que nunca cozinhou na vida consegue chegar ao resultado desejado. Portanto, buscamos essa descrição do processo que permite garantir o resultado e abstrair do contexto "quem" (ou "o que") realiza o esforço.

!!! note

    A principal característica de um algoritmo é sua corretude, ou seja, sua capacidade de realizar corretamente a tarefa conforme a especificação.

O computador é uma ferramenta fantástica que faz, muito rapidamente, exatamente o que pedimos - desde que esta solicitação seja feita de um modo que a máquina consiga interpretar de forma inequívoca. O objetivo se torna, portanto, definir um *algoritmo computacional*, ou seja, descrever as instruções do algoritmo de um modo específico e detalhado o suficiente para que o computador possa interpretá-las para realizar a tarefa em questão[@Cormen2013].

!!! info "Algoritmo Computacional"

    Uma sequência finita de instruções bem definidas para realizar uma tarefa com um computador.

Há discussões interessantes sobre a definição precisa do conceito de um algoritmo computacional, mas as todas convergem no pontos mais importantes[@Knuth1997]. A sequência de instruções deve ser finita porque o objetivo é realizar a tarefa, portanto a execução deve terminar. As instruções utilizadas devem ser bem especificadas e com apenas uma interpretação possível, de modo que o computador saiba exatamente o que fazer a cada passo. A realização da tarefa também pode lidar com entrada de dados e saída de dados, ou seja, o algoritmo pode receber informações externas necessárias para a realização da tarefa e fornecer informações resultantes deste processo. Por fim, os passos devem ser apresentados de tal forma que seja possível para o computador entender e executar cada um deles.

Existem diversas formas de representar de um algoritmo e não há consenso de qual é a melhor delas. Independentemente, o algoritmo deve ser representado da forma mais clara possível para facilitar seu entendimento por quem vai executá-lo. Apresentamos a seguir algumas possibilidades.

{! algoritmos/narrativa.md !}

{! algoritmos/fluxograma.md !}

{! algoritmos/pseudocodigo.md !}

{! algoritmos/codigo.md !}

<h2>Resumo</h2>

Um algoritmo é uma sequência de instruções bem definidas para realização uma tarefa. Algoritmos representados como linguagens de programação podem ser fornecidos a computadores para execução.


{! algoritmos/exercicios.md !}

