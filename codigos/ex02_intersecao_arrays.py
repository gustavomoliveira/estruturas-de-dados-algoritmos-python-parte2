def intersecao(primeiro_array, segundo_array):
    disponiveis = {}
    comuns = {}

    for elemento in primeiro_array:
        disponiveis[elemento] = disponiveis.get(elemento, 0) + 1

    for elemento in segundo_array:
        if disponiveis.get(elemento, 0) > 0:
            disponiveis[elemento] -= 1
            comuns[elemento] = comuns.get(elemento, 0) + 1

    return comuns

def gerar_arrays(tamanho):
    primeiro_array = list(range(tamanho))
    segundo_array = list(range(tamanho // 2, tamanho + tamanho // 2))
    return primeiro_array, segundo_array


print('=== Exercício 2 – Interseção de arrays com hash table ===')
print()
print('Os arrays são construídos para que o resultado seja conhecido de antemão:')
print('o primeiro vai de 0 a N-1 e o segundo de N/2 a N+N/2-1, então só')
print('os números de N/2 a N-1 estão nos dois, cada um com contagem 1.')
print()

primeiro_com_repeticoes = [3, 3, 3, 5, 5, 8, 1, 1, 9, 9, 9, 9]
segundo_com_repeticoes = [9, 3, 5, 5, 5, 2, 9, 1, 1, 1, 3, 9, 6, 9, 9]
esperado_repeticoes = {3: 2, 5: 2, 1: 2, 9: 4}

resultado = intersecao(primeiro_com_repeticoes, segundo_com_repeticoes)
print('Caso com repetições:')
print(f'  Primeiro array: {primeiro_com_repeticoes}')
print(f'  Segundo array:  {segundo_com_repeticoes}')
print(f'  Resultado: {resultado}')
print(f'  Esperado:  {esperado_repeticoes}')
print(f'  Confere:   {resultado == esperado_repeticoes}')
print()

print(f'{"N":<10}{"Em comum esperado":<20}{"Em comum obtido":<18}{"Todos com contagem 1":<22}{"Confere"}')
print('-' * 80)

for tamanho in [1_000, 10_000, 100_000, 1_000_000]:
    primeiro, segundo = gerar_arrays(tamanho)
    resultado = intersecao(primeiro, segundo)

    esperado = tamanho // 2
    todos_um = all(quantidade == 1 for quantidade in resultado.values())
    confere = len(resultado) == esperado and todos_um

    print(f'{tamanho:<10}{esperado:<20}{len(resultado):<18}{str(todos_um):<22}{confere}')