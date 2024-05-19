## Ciência da Computação

A tecnologia permeia todas as atividades humanas nos dias de hoje, principalmente alavancada pela disponibilidade e acessibilidade a ferramentas computacionais. Neste contexto, a *Ciência da Computação* torna-se uma área cada vez mais relevante.

!!! quote "[Dennis Ritchie](http://en.wikiquote.org/wiki/Dennis_Ritchie)"

    Ciência da Computação é diferente das disciplinas tradicionais. Filosoficamente, difere das ciências físicas porque não busca descobrir, explicar, ou explorar o mundo natural, mas estudar as propriedades de máquinas criadas por humanos. Nisso é análoga a Matemática, e de fato a parte de "ciência" da Ciência da Computação tem o espírito matemático em sua maior parte. Mas um aspecto inevitável da Ciência da Computação é a criação de programas de computadores: objetos que, apesar de intangíveis, estão sujeitos ao comércio.

A Ciência da Computação não é "ciência" por definição (matemática? engenharia? arte? esporte?), nem sobre computadores (como ferramenta). A área pode ser considerada como uma tentativa de formalizar certos processos, definindo uma forma precisa de se falar sobre *como* realizar algo, em contraste a *o que* é algo.

*[Ciência](http://pt.wikipedia.org/wiki/Ci\%C3\%AAncia) (do Latim *scientia*, "conhecimento") é uma forma sistemática de produzir conhecimento (via [método científico](http://pt.wikipedia.org/wiki/M%C3%A9todo_cient%C3%ADfico)), ou o nome dado a estrutura organizada do conhecimento obtido. O método científico é um conjunto de regras básicas de como proceder para produzir conhecimento, criando algo novo ou corrigindo/incrementando conhecimentos pré-existentes[@Newton1729]. Esta metodologia pode - e deve - ser aplicada a experimentos computacionais, mas a Ciência da Computação não tem este foco.

O [computador](http://pt.wikipedia.org/wiki/Computador) também não é o objetivo da Ciência da Computação. A ideia é que, uma vez formalizados os processos para realização de uma tarefa, alguém (ou algo) possa executá-los corretamente. O computador interpreta e executa rapidamente instruções muito simples, sendo uma das máquinas mais versáteis para realizar os processos.

!!! quote "[Edsger H. Dijkstra](http://pt.wikipedia.org/wiki/Edsger_Dijkstra)"

    Ciência da Computação está tão relacionada aos computadores quanto a Astronomia aos telescópios, Biologia aos microscópios, ou Química aos tubos de ensaio. A Ciência não estuda ferramentas. Ela estuda como nós as utilizamos, e o que descobrimos com elas.}%

O computador executa diversas tarefas por meio de seus processos, e para tanto lida com dois [tipos de conhecimento](http://pt.wikipedia.org/wiki/Conhecimento#Tipos_de_conhecimento). O primeiro deles é o *conhecimento declarativo* que é uma descrição de fato(s). Por exemplo, "a raiz quadrada de $n$ é o número $r$ tal que $r^2 = n$". Embora interessante, esta informação serve apenas para verificar se $r$ é ou não raiz de $n$, não resolve um problema relativamente comum de, dado o número $n$, descobrir *qual é $r$* tal que satisfaça a definição.

A [Ciência da Computação](http://pt.wikipedia.org/wiki/Ci\%C3\%AAncia_da_computa\%C3\%A7\%C3\%A3o) está interessada no segundo tipo, o *conhecimento procedural* que especifica processos, indicando como [melhor] realizar algo. Por exemplo, para aproximar o valor $r$, pode-se começar com $r = 0$ e incrementar seu valor até que $r^2 \geq n$. Esta estratégia de [busca exaustiva](http://pt.wikipedia.org/wiki/For%C3%A7a_bruta) pode ser apresentada de forma um pouco mais estruturada:

1. Defina $r = 0$ e $n \in \mathbb{N}$.
1. Adicione 1 a $r$.
1. Se $r^2 \geq n$, então pare ($r \approx \sqrt{n}$). Senão, vá para o passo 2.

Uma vez estabelecido o processo de calcular a raiz, este pode ser passado ao computador para que execute as etapas. A versatilidade desta máquina permite que ela possa executar diversos tipos de processos com fins diferentes (ou não), desde que adequadamente definidos.

A Ciência da Computação tenta formalizar este conhecimento procedural, e juntar seus blocos em sistemas grandes e complexos que podem ser [re]utilizados nas mais diversas áreas. Por exemplo, supondo as diversas [Leis da Física](http://pt.wikipedia.org/wiki/Leis_de_Newton), pode-se elaborar diversos procedimentos para definir posições e forças, e juntar estes resultados para [entretenimento](https://gabrielecirulli.github.io/2048/), [progresso](http://pt.wikipedia.org/wiki/Ve%C3%ADculo_aut%C3%B4nomo), ou [praticamente] qualquer outra [coisa que se possa imaginar](http://pt.wikipedia.org/wiki/Rosetta).

Esta "mágica" ocorre via *[processos computacionais](http://pt.wikipedia.org/wiki/Thread_%28ci%C3%AAncia_da_computa%C3%A7%C3%A3o%29)*, que são entidades abstratas que existem nos computadores. A medida que evolui, o processo manipula *dados* (outras entidades abstratas), e esta evolução é dirigida por regras definidas em um *programa* (composto por expressões simbólicas em uma *linguagens de programação*)[@Abelson1996].

Programação é a atividade de escrever os passos do processo de modo que o computador possa entendê-los e executá-los. Programação é uma forma de [arte](http://www.paulgraham.com/knuth.html), mas também é uma [habilidade que pode ser desenvolvida](http://pihisall.wordpress.com/2007/03/15/aprenda-a-programar-em-dez-anos/). E [você deveria aprender a programar](http://www.youtube.com/watch?v=xfBWk4nw440), afinal:

!!!quote "[Donald Knuth](http://pt.wikipedia.org/wiki/Donald_Knuth])"

    É preciso ver um algoritmo para crer nele.

No contexto acadêmico, a Ciência da Computação segue as diretrizes curriculares do [Ministério da Educação](http://portal.mec.gov.br/)[@MEC2005], e os esforços para incentivar a pesquisa e o ensino são guiados pela [Sociedade Brasileira de Computação](http://www.sbc.org.br).  O Projeto Pedagógico do Curso de Bacharelado em Ciência da Computação[@ppcBCC2015] diz que o egresso deve possuir conhecimentos para encontrar soluções computacionais para várias áreas de conhecimento e estar preparado para a investigação, desenvolvimento, análise, modelagem, projeto, e implementação de sistemas computacionais, bem como para desenvolver pesquisa científica e tecnológica. Portanto, o profissional deveria ser capaz de resolver qualquer problema lógico em qualquer área, desde que a solução possa ser implementada em um computador.%

Segundo o Currículo de Referência da SBC para Cursos de Graduação[@SBC2005], a atuação profissional dos egressos pode ter características da área de computação em três componentes, englobando aspectos gerais, técnicos e ético-sociais. A regulamentação da profissão de informática está em processo de aprovação[@Bigonha2013], mas a SBC consolidou sua posição institucional na formulação dos seguintes princípios, que devem ser observados[@SBC2013]:

1. exercício da profissão de Informática deve ser livre e independer de diploma ou comprovação de educação formal;
1. nenhum conselho de profissão pode criar qualquer impedimento ou restrição ao princípio acima;
1. a área deve ser Auto-Regulada.
