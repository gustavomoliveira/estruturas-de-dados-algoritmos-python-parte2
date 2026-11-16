import random


def maior_unico(arr):
    maior = None
    comparacoes = 0

    for i in range(len(arr)):
        atual = arr[i]
        contador = 0

        for j in range(len(arr)):
            comparacoes += 1

            if arr[j] == atual:
                contador += 1

        if contador == 1:
            if (maior is None) or (atual > maior):
                maior = atual

    return maior, comparacoes


def maior_unico_otimizado(arr):
    contagens = {}
    leitura_escrita = 0
    entrada_visitada = 0

    for numero in arr:
        contagens[numero] = contagens.get(numero, 0) + 1
        leitura_escrita += 2  # 1 leitura (get) + 1 escrita (atribuição)

    maior = None

    for numero, quantidade in contagens.items():
        entrada_visitada += 1
        if quantidade == 1:
            if maior is None or numero > maior:
                maior = numero

    return maior, leitura_escrita, entrada_visitada


def gerar_cenarios(tamanho):
    random.seed(42)

    distintos = random.sample(range(tamanho * 10), tamanho)

    com_repeticoes = []
    for _ in range(tamanho):
        com_repeticoes.append(random.randint(0, tamanho // 4))

    sem_unico = []
    for valor in range(tamanho // 2):
        sem_unico.append(valor)
        sem_unico.append(valor)
    random.shuffle(sem_unico)

    return {
        'todos distintos': distintos,
        'com repetições': com_repeticoes,
        'sem valor único': sem_unico,
    }


print('=== Exercício 1 – Maior número único: aninhada x hash table ===')
print()

tamanhos = [10, 20, 40, 80, 160, 320]

print('--- Comparação por tamanho de lista ---')
print(
    f'{"N":<6}{"Cenário":<18}{"D":<6}{"Maior":<8}{"Comp. (aninh.)":<16}{"Leit/Esc":<10}{"Entradas":<10}{"Total (hash)":<14}{"Iguais":<6}')
print('-' * 94)

for tamanho in tamanhos:
    for nome, lista in gerar_cenarios(tamanho).items():
        maior_a, comparacoes = maior_unico(lista)
        maior_b, leitura_escrita, entradas = maior_unico_otimizado(lista)
        distintos = len(set(lista))
        total_hash = leitura_escrita + entradas
        iguais = maior_a == maior_b
        print(
            f'{tamanho:<6}{nome:<18}{distintos:<6}{str(maior_a):<8}{comparacoes:<16}{leitura_escrita:<10}{entradas:<10}{total_hash:<14}{iguais}')
    print()
