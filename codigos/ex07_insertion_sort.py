def insertion_sort(lista):
    resultado = lista.copy()
    comparacoes = 0
    deslocamentos = 0

    for i in range(1, len(resultado)):
        chave = resultado[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1
            if resultado[j] <= chave:
                break
            resultado[j + 1] = resultado[j]
            deslocamentos += 1
            j -= 1

        resultado[j + 1] = chave

    return resultado, comparacoes, deslocamentos


print('=== Exercício 7 – Insertion Sort com contagem de comparações e deslocamentos ===')
print()

lista_teste = [5, 2, 4, 1]
ordenada, comparacoes, deslocamentos = insertion_sort(lista_teste)
print('Teste pequeno:')
print(f'  Entrada:       {lista_teste}')
print(f'  Saída:         {ordenada}')
print(f'  Comparações:   {comparacoes}')
print(f'  Deslocamentos: {deslocamentos}')
print()

print(f'{"N":<8}{"Estado inicial":<18}{"Comparações":<14}{"Deslocamentos":<16}{"Ordenou"}')
print('-' * 63)

for tamanho in [100, 200, 400]:
    quase_ordenada = list(range(tamanho))
    for k in range(0, tamanho - 1, 20):
        quase_ordenada[k] = k + 1
        quase_ordenada[k + 1] = k

    casos = [
        ('já ordenada', list(range(tamanho))),
        ('quase ordenada', quase_ordenada),
        ('invertida', list(range(tamanho, 0, -1))),
    ]

    for nome, lista in casos:
        ordenada, comparacoes, deslocamentos = insertion_sort(lista)
        ordenou = ordenada == sorted(lista)
        print(f'{tamanho:<8}{nome:<18}{comparacoes:<14}{deslocamentos:<16}{ordenou}')
    print()