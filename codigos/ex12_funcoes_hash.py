M = 10


def h1(k):
    return k % M


def h2(k):
    return (k * 7) % M


def h3(k):
    return (k * k) % M


def distribuir(chaves, funcao):
    contagem = [0] * M
    for k in chaves:
        contagem[funcao(k)] += 1
    return contagem


def posicoes_usadas(contagem):
    usadas = 0
    for quantidade in contagem:
        if quantidade > 0:
            usadas += 1
    return usadas


print('=== Exercício 12 – Análise de funções hash e distribuição (M = 10) ===')
print()

print('Posição de cada chave de 0 a 9')
print(f'{"k":<6}{"h1":<6}{"h2":<6}{"h3"}')
print('-' * 24)
for k in range(10):
    print(f'{k:<6}{h1(k):<6}{h2(k):<6}{h3(k)}')
print()

conjuntos = [
    ('Chaves consecutivas de 0 a 99', range(0, 100)),
    ('Múltiplos de 5 (0, 5, 10, ... 95)', range(0, 100, 5)),
    ('Múltiplos de 10 (0, 10, 20, ... 90)', range(0, 100, 10)),
    ('Apenas números pares de 0 a 98', range(0, 100, 2)),
]

funcoes = [('h1', h1), ('h2', h2), ('h3', h3)]

for nome, chaves in conjuntos:
    print(f'{nome} ({len(chaves)} chaves)')
    print('  Quantidade de chaves em cada posição de 0 a 9')
    for nome_funcao, funcao in funcoes:
        contagem = distribuir(chaves, funcao)
        usadas = posicoes_usadas(contagem)
        maior = max(contagem)
        print(f'  {nome_funcao}: {contagem}  posições usadas: {usadas}  maior ocupação: {maior}')
    print()