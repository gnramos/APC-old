## Avaliação

A avaliação visa garantir que a solução algorítmica é adequada, ou seja, que resolve o problema. Há diversas propriedades que podem/devem ser verificadas.

* Corretude: o algoritmo é correto se fornece o resultado correto para toda entrada válida[@Cormen2009].
* Eficiência: o algoritmo é eficiente se consome o mínimo de recursos possíveis para fornecer um resultado; geralmente o foco é em *tempo* (o quão rápido é sua execução).
* Usabilidade: o quão fácil é para usar, lembrar e aprender o algoritmo[@Jain2023].

A corretude é a principal característica, as demais não têm importância se a solução que não resolve o problema. Também é um conceito ardiloso[@Cormen2013] pois pode depender do contexto. Por exemplo, um algoritmo que aproxima o valor de $\pi$ pode ser correto num contexto em que a precisão de 2 casas decimais é suficiente (por exemplo, apresentando resultados simples à pessoas), mas incorreto em outro onde a precisão necessariamente deve ser bem maior (como calculando trajetórias de naves espaciais). A eficiência não é o foco da parte inicial mas será discutida no capítulo de estruturas de dados, e pode ser uma característica fundamental da solução em certos contexto (como o piloto automático de uma aeronave). Noções de usabilidade e legibilidade do código permeiam o texto e serão destacadas quando apropriado.

Esta verificação é um processo complexo, que pode ser feita de diversas formas. A mais simples é testar o resultado obtido para situações conhecidas, e fazer isso na totalidade das condições possíveis ou numa abrangência adequada. Quando isto não é possível (talvez por que demore demais), há outras formas, como verificar as situações antes (pré-condição) e depois (pós-condição) de cada passo no algoritmo, ele será correto se e somente se ambas forem verdadeiras.
