class Pilha:
    def __init__(self):
        self.__itens = []

    def esta_vazia(self):
        return len(self.__itens) == 0

    def empilhar(self, valor):
        self.__itens.append(valor)

    def desempilhar(self):
        if self.esta_vazia():
            raise Exception('underflow: a pilha está vazia')
        return self.__itens.pop()

    def topo(self):
        if self.esta_vazia():
            raise Exception('underflow: a pilha está vazia, não há topo')
        return self.__itens[-1]

    def estado(self):
        return f'itens={self.__itens}'


def inverter_string(texto):
    pilha = Pilha()
    invertido = ''

    for caractere in texto:
        pilha.empilhar(caractere)

    while not pilha.esta_vazia():
        invertido += pilha.desempilhar()

    return invertido


print('=== Exercício 11 – Reversão de string utilizando pilha ===')
print()

testes = [
    ('palavra simples', 'abc', 'cba'),
    ('frase com espaços', 'estrutura de dados', 'sodad ed aruturtse'),
    ('com acento', 'ação', 'oãça'),
    ('com números e símbolos', 'ab12!', '!21ba'),
    ('palíndromo', 'arara', 'arara'),
    ('um caractere', 'x', 'x'),
    ('string vazia', '', ''),
]

for nome, entrada, esperado in testes:
    resultado = inverter_string(entrada)
    print(f'{nome}')
    print(f'  Entrada:   "{entrada}"')
    print(f'  Saída:     "{resultado}"')
    print(f'  Esperado:  "{esperado}"')
    print(f'  Correto:   {resultado == esperado}')
    print()

longa = 'a' * 500 + 'b' * 500
esperada_longa = 'b' * 500 + 'a' * 500
resultado_longa = inverter_string(longa)
print('string longa (500 "a" seguidos de 500 "b")')
print(f'  Tamanho da entrada: {len(longa)}')
print(f'  Tamanho da saída:   {len(resultado_longa)}')
print(f'  Correto:            {resultado_longa == esperada_longa}')