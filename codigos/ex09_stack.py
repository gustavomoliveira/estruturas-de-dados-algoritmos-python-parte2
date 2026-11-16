class Stack:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__itens = [None] * capacidade
        self.__tamanho = 0

    def esta_vazia(self):
        return self.__tamanho == 0

    def esta_cheia(self):
        return self.__tamanho == self.__capacidade

    def empilhar(self, valor):
        if self.esta_cheia():
            raise Exception('overflow: a pilha está cheia')
        self.__itens[self.__tamanho] = valor
        self.__tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            raise Exception('underflow: a pilha está vazia')
        self.__tamanho -= 1
        valor = self.__itens[self.__tamanho]
        self.__itens[self.__tamanho] = None
        return valor

    def topo(self):
        if self.esta_vazia():
            raise Exception('underflow: a pilha está vazia, não há topo')
        return self.__itens[self.__tamanho - 1]

    def estado(self):
        return f'itens={self.__itens}  tamanho={self.__tamanho}  capacidade={self.__capacidade}'


print('=== Exercício 9 – Pilha com capacidade fixa e controle de erros ===')
print()

pilha = Stack(3)
print('Pilha criada com capacidade 3')
print(f'  Estado: {pilha.estado()}')
print()

operacoes = [
    ('empilhar', 10),
    ('empilhar', 20),
    ('empilhar', 30),
    ('empilhar', 40),
    ('topo', None),
    ('desempilhar', None),
    ('desempilhar', None),
    ('desempilhar', None),
    ('desempilhar', None),
]

for nome, valor in operacoes:
    try:
        if nome == 'empilhar':
            pilha.empilhar(valor)
            descricao = f'empilhar({valor})'
        elif nome == 'desempilhar':
            removido = pilha.desempilhar()
            descricao = f'desempilhar() devolveu {removido}'
        else:
            descricao = f'topo() devolveu {pilha.topo()}'
    except Exception as erro:
        descricao = f'{nome} -> ERRO tratado: {erro}'

    print(descricao)
    print(f'  Estado: {pilha.estado()}')
    print()