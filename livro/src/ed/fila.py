#     @author: Guilherme N. Ramos (gnramos@unb.br)
#
# Implementação ingênua de uma fila usando lista duplamente encadeada cíclica.

from lista_dec import LDEC


class Fila:
    """Define uma classe com o comportamento FIFO."""
    def __init__(self):
        self.front = LDEC()

    def vazia(self):  # O(1)
        return self.front.vazia()

    def enqueue(self, dado):  # O(1)
        self.front.insere_final(dado)

    def dequeue(self):  # O(1)
        return self.front.remove_inicio()

    # Viabilizando iteração pythônica.
    def __contains__(self, dado):  # O(n)
        return dado in self.front

    def __len__(self):  # O(1)
        return len(self.front)

    def __str__(self):  # O(n)
        return '<-'.join(f'[{dado}]' for dado in self.front)
