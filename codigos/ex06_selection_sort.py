import random


def selection_sort(lista):
    resultado = lista.copy()
    comparacoes = 0
    trocas = 0

    for i in range(len(resultado) - 1):
        indice_menor = i

        for j in range(i + 1, len(resultado)):
            comparacoes += 1
            if resultado[j] < resultado[indice_menor]:
                indice_menor = j

        if indice_menor != i:
            auxiliar = resultado[i]
            resultado[i] = resultado[indice_menor]
            resultado[indice_menor] = auxiliar
            trocas += 1

    return resultado, comparacoes, trocas


print('=== Exercício 6 – Selection Sort com contagem de comparações e trocas ===')
print()

lista_teste = [64, 25, 12, 22, 11]
ordenada, comparacoes, trocas = selection_sort(lista_teste)
print('Teste pequeno:')
print(f'  Entrada:     {lista_teste}')
print(f'  Saída:       {ordenada}')
print(f'  Comparações: {comparacoes}')
print(f'  Trocas:      {trocas}')
print()

random.seed(42)

print(f'{"N":<8}{"Estado inicial":<18}{"Comparações":<14}{"Trocas":<9}{"Ordenou"}')
print('-' * 56)

for tamanho in [100, 200, 400]:
    casos = [
        ('aleatória', random.sample(range(tamanho * 10), tamanho)),
        ('já ordenada', list(range(tamanho))),
        ('invertida', list(range(tamanho, 0, -1))),
    ]

    for nome, lista in casos:
        ordenada, comparacoes, trocas = selection_sort(lista)
        ordenou = ordenada == sorted(lista)
        print(f'{tamanho:<8}{nome:<18}{comparacoes:<14}{trocas:<9}{ordenou}')
    print()
