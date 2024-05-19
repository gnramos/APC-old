## Fluxograma

Outro jeito bastante intuitivo com o uso de figuras geométricas, como pode ser vista nos diagramas abaixo.

```mermaid
flowchart TD
    I([Início]) --> EF{Entende<br>fluxogramas?}
    EF -->|Sim| O[/Ótimo!/] --> F([Fim])
    EF -->|Não| VLS{Vê a linha<br>com 'Sim'?}
    VLS -->|Sim| VLN{E a com<br>'Não'?} -->|Sim| O
    VLS -->|Não| ES[É a outra<br>linha...]  --> VLS
    VLN -->|Não| MJ[/Mas já<br>seguiu várias?!/] --> SS[Siga a seta.] --> VLS
```

Cada forma geométrica tem um significado especifico mas, para facilitar, usaremos apenas as a seguir:

* Terminal: que indica onde o algoritmo inicia e onde termina.
* Dado(s): que indica a comunicação (entrada/saída) de dado(s) com o algoritmo.
* Processo: que indica a execução de uma instrução/tarefa.
* Decisão: que indica a necessidade de se escolher uma (e apenas uma!) das diversas possíveis ações subsequentes.
* Seta: que indica a sequência em que as instruções serão executadas.

``` mermaid
flowchart TD
    I([Terminal]) -->|seta| P[Processo] & D{Decisão} & IO[/Entrada<br>Saída/]
```

Geralmente se usa instruções mais diretas e simples que na descrição narrativa, também em função da limitação das figuras utilizadas. Isso tem dois efeitos muito interessantes: o uso de fluxograma restringe muito a amplitude do entendimento das instruções, facilitando a construção de instruções bem definidas para o algoritmo; mas também restringe o tipo de instruções utilizáveis, dificultando a construção do processo desejado - podem ser necessárias mais instruções para descrever adequadamente um pedaço mais complexo do comportamento.

