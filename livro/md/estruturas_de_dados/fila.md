# Fila

Uma fila é um [TAD](/programacao/tipos_de_dados/#tipo-abstrato-de-dado) que, como a [lista](lista.md), tem o objetivo de organizar um conjunto de dados para facilitar sua manipulação. O diferencial é claro na inserção e remoção de elementos, pois definem um comportamento bem específico.

!!! info "Fila"

    Tipo abstrato de dados cujo processo de inserção e remoção determina um comportamento FIFO (*first in, first out*), onde um elemento é removido na mesma ordem em que foi inserido.

A ideia é simples e presente em nosso cotidiano - frequentemente lidamos com filas em supermercados, bancos, etc. O comportamento esperado é que os elementos são agrupados a medida que chegam, e removidos na mesma ordem para processamento. Qualquer pessoa que chegue se posiciona ao final da fila, e somente a primeira pessoa da fila pode sair dela. Se Alice, Bob e Charlie chegam ao banco nesta ordem, a primeira a ser atendida será Alice, seguida de Bob e então Charlie.

## Implementação

Há diversas formas de se implementar uma fila. É preciso manter um conjunto de dados e controlar inserção e remoção nele. Consideraremos duas formas.

### Fila como um vetor

O uso de um vetor implica em determinar a alocação de uma estrutura de tamanho fixo e a implementação pode ser feita de algumas maneiras. A mais simples é considerar que há um vetor de tamanho $n$ alocado, que o início da fila o elemento na primeira posição do vetor (índice 0) e que o último é o *f*-ésimo elemento ($0 \leq f < n$). A inserção é simples, basta por o novo elemento na posição $f$ do vetor e incrementar este índice. A remoção também é simples, apesar de custosa: retirar o primeiro elemento, mover todos os elementos subsequentes em uma posição e decrementar o índice do último elemento (garantindo assim que uma próxima remoção afete o elemento correto).

=== "Inserção $O(1)$"

    ``` python title="Inserção"
    # A fila tem f elementos (de uma quantidade máxima de n).
    if f < n:
        fila[f] = dado
        f += 1
    ```

=== "Remoção $O(n)$"

    ``` python title="Remoção"
    if f > 0:
        # dado = fila[0]
        for x in range(f):
            fila[f] = fila[f + 1]
        f -= 1
    ```

É possível diminuir o esforço necessário para remoção mantendo um segundo índice $i$, que indicaria a posição do primeiro elemento, e que varia conforme os elementos são removidos. Assim, as posições "inicial" e "final" dos elementos da lista mudam a medida que os elementos são removidos ou acrescentados. Essa implementação é mais complexa, mas implica que tanto remoção quanto inserção são $O(1)$.

### Fila como uma lista

O uso de um vetor implica a alocação de uma quantidade fixa de memória, que pode ser rearranjada posteriormente se necessário. Como este rearranjo tem um custo, é desejável ter um vetor "grande o suficiente" para evitá-lo, mas como estimar adequadamente o quão grande é suficiente? Alocar um vetor tão grande que seja suficiente para a maioria das operações também não é desejável, uma vez que provavelmente implica em uso ineficiente do recurso de memória. Uma alternativa é gerenciar a memória para consumir apenas a quantidade de memória necessária, armazenando os elementos em uma lista simplesmente encadeada.

Neste contexto, pode-se inserir no início (em $O(1)$) e remover do final (em $O(n)$) como com um vetor, ou o contrário, como exemplificado a seguir.


=== "Inserção $O(n)$"

    ``` python title="Inserção"
    if fila:
        aux = fila
        while aux.prox:
            aux = aux.prox
        aux.prox = Elemento(dado)
    else:
        fila = Elemento(dado)
    ```

=== "Remoção $O(1)$"

    ``` python title="Remoção"
    if fila:
        # dado = fila.dado
        fila = fila.prox
    ```

Uma das operações continua como $(O(n))$, pois é preciso percorrer a lista para chegar ao final da fila. Esse esforço pode ser minimizado usando uma estrutura de dados mais adequada ao problema, que permita acesso ao último elemento em $O(1)$: a lista duplamente encadeada cíclica.

=== "Implementação Ingênua"

    Busca uma implementação "pythônica", fornecendo os métodos [str](https://docs.python.org/pt-br/3/reference/datamodel.html?highlight=__str__#object.__str__), [len](https://docs.python.org/pt-br/3/reference/datamodel.html?highlight=__str__#object.__len__) e [contains](https://docs.python.org/pt-br/3/reference/datamodel.html?highlight=__str__#object.__contains__).

=== "Código"

    ``` python title="Fila"
        --8<-- "ed/fila.py"
    ```
