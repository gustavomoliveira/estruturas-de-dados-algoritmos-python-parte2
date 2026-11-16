class Queue:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__itens = [None] * capacidade
        self.__inicio = 0
        self.__fim = 0
        self.__tamanho = 0

    def esta_vazia(self):
        return self.__tamanho == 0

    def esta_cheia(self):
        return self.__tamanho == self.__capacidade

    def enfileirar(self, valor):
        if self.esta_cheia():
            raise Exception('overflow: a fila está cheia')
        self.__itens[self.__fim] = valor
        self.__fim = (self.__fim + 1) % self.__capacidade
        self.__tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            raise Exception('underflow: a fila está vazia')
        valor = self.__itens[self.__inicio]
        self.__itens[self.__inicio] = None
        self.__inicio = (self.__inicio + 1) % self.__capacidade
        self.__tamanho -= 1
        return valor

    def frente(self):
        if self.esta_vazia():
            raise Exception('underflow: a fila está vazia, não há elemento na frente')
        return self.__itens[self.__inicio]

    def estado(self):
        return f'itens={self.__itens}  inicio={self.__inicio}  fim={self.__fim}  tamanho={self.__tamanho}'


def mostrar(acao, fila):
    print(acao)
    print(f'  Estado: {fila.estado()}')
    print()


print('=== Exercício 10 – Fila com capacidade fixa e ponteiros ===')
print()

fila = Queue(3)
mostrar('Fila criada com capacidade 3', fila)

saidas = []

fila.enfileirar('A')
mostrar('enfileirar(A)', fila)

fila.enfileirar('B')
mostrar('enfileirar(B)', fila)

fila.enfileirar('C')
mostrar('enfileirar(C)', fila)

try:
    fila.enfileirar('X')
except Exception as erro:
    mostrar(f'enfileirar(X) -> ERRO tratado: {erro}', fila)

mostrar(f'frente() devolveu {fila.frente()}', fila)

removido = fila.desenfileirar()
saidas.append(removido)
mostrar(f'desenfileirar() devolveu {removido}', fila)

removido = fila.desenfileirar()
saidas.append(removido)
mostrar(f'desenfileirar() devolveu {removido}', fila)

fila.enfileirar('D')
mostrar('enfileirar(D)', fila)

fila.enfileirar('E')
mostrar('enfileirar(E)', fila)

removido = fila.desenfileirar()
saidas.append(removido)
mostrar(f'desenfileirar() devolveu {removido}', fila)

removido = fila.desenfileirar()
saidas.append(removido)
mostrar(f'desenfileirar() devolveu {removido}', fila)

removido = fila.desenfileirar()
saidas.append(removido)
mostrar(f'desenfileirar() devolveu {removido}', fila)

try:
    fila.desenfileirar()
except Exception as erro:
    mostrar(f'desenfileirar() -> ERRO tratado: {erro}', fila)

entradas = ['A', 'B', 'C', 'D', 'E']
print('Validação do FIFO')
print(f'  Ordem em que entraram: {entradas}')
print(f'  Ordem em que saíram:   {saidas}')
print(f'  FIFO respeitado:       {entradas == saidas}')