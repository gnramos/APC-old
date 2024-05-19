## Generalização

Generalizar é criar modelos, regras, princípios ou teorias que se adequem à uma classe de problemas partir de padrões observados em instâncias específicas do problema. A ideia é que, partindo de uma solução correta, esta seja adaptada de modo que possa ser aplicada em problemas similares.

Por exemplo, um triângulo equilátero tem os 3 ângulos internos iguais a 60° e as 3 linhas com o mesmo comprimento. A partir disso, é relativamente simples definir um algoritmo que desenhe um. Da mesma forma, um quadrado tem os 4 ângulos internos iguais a 90° e as 4 linhas com o mesmo comprimento, e também é simples desenhar um, basta criar linhas com os ângulos adequados. Considerando o pentágono regular, é possível perceber que as soluções são muito similares... A solução proposta constrói o desenho de modo que cada linha continua a partir do fim da linha anterior, usando o ângulo externo do polígono para a rotação.

![Ângulos interno/externo](/img/AnguloExterno.png "Ângulos interno/externo"){ width="50%" } |
:------:|
Propriedade dos ângulos interno/externo |

=== "Triângulo"

    ``` linguagem-natural title="Triângulo Equilátero"
    ângulo_interno = 60°
    ângulo_externo = 180° - ângulo_interno
    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo no sentido anti-horário.
    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo no sentido anti-horário.
    Desenhe uma linha de comprimento L.
    ```

=== "Quadrado"

    ``` linguagem-natural title="Quadrado"
    ângulo_interno = 90°
    ângulo_externo = 180° - ângulo_interno
    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo no sentido anti-horário.
    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo no sentido anti-horário.
    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo no sentido anti-horário.
    Desenhe uma linha de comprimento L.
    ```

=== "Pentágono"

    ``` linguagem-natural title="Pentágono Regular"
    ângulo_interno = 72°
    ângulo_externo = 180° - ângulo_interno
    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo no sentido anti-horário.
    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo no sentido anti-horário.
    Desenhe uma linha de comprimento L.
    Gire a caneta em 1ângulo_externo no sentido anti-horário.
    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo no sentido anti-horário.
    Desenhe uma linha de comprimento L.
    ```

Nos algoritmos, os ângulos e a quantidade de linhas são diferentes, mas também é possível reconhecer um padrão nas instruções. A propriedade geométrica de polígonos determina que [id> a soma de todos os ângulos externos de um polígono é 360°](https://pt.wikipedia.org/wiki/%C3%82ngulos_internos_e_externos#Propriedades), e como os ângulos são iguais, é possível determinar o ângulo para cada forma geométrica apenas com a informação de quantos lados ela tem. Assim, pode-se rescrever os algoritmos e chegar a uma solução genérica que atende qualquer polígono regular.

=== "Triângulo"

    ``` linguagem-natural title="Triângulo Equilátero"
    ângulo_externo = 360 / 3

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.
    ```

=== "Quadrado"

    ``` linguagem-natural title="Retângulo Regular"
    ângulo_externo = 360 / 4

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.
    ```

=== "Pentágono"

    ``` linguagem-natural title="Pentágono Regular"
    ângulo_externo = 360 / 5

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.

    Desenhe uma linha de comprimento L.
    Gire a caneta em ângulo_externo graus no sentido anti-horário.
    ```

=== "Polígono"

    ``` linguagem-natural title="Polígono Regular"
    ângulo_externo = 360 / número_de_lados

    Repita número_de_lados vezes:
        Desenhe uma linha de comprimento L.
        Gire a caneta em ângulo_externo graus no sentido anti-horário.
    ```

=== "Python + Turtle"

    ``` python title="Polígono Regular"
    --8<-- "turtle/poligono_regular.py:7:11"
    ```
