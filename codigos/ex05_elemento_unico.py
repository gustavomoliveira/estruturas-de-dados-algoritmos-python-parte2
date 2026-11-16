def primeiro_nao_repetido(texto):
    contagens = {}

    for caractere in texto:
        contagens[caractere] = contagens.get(caractere, 0) + 1

    for caractere in texto:
        if contagens[caractere] == 1:
            return caractere

    return None

print('=== Exercício 5 – Primeiro caractere não repetido ===')
print()

casos = [
    ('um repetido e um único', 'swiss', 'w'),
    ('primeiro caractere repetido', 'teeter', 'r'),
    ('dois únicos, vale o primeiro', 'abacbd', 'c'),
    ('primeiro já é o único', 'programming', 'p'),
    ('único no fim', 'aabbc', 'c'),
    ('maiúscula e minúscula', 'Aa', 'A'),
    ('um caractere só', 'z', 'z'),
    ('todos repetidos', 'aabbcc', None),
    ('string vazia', '', None),
    ('string grande', 'x' * 100_000 + 'y' + 'x' * 100_000, 'y'),
]

for nome, entrada, esperado in casos:
    resultado = primeiro_nao_repetido(entrada)

    if len(entrada) <= 20:
        descricao = f'"{entrada}"'
    else:
        descricao = f'{len(entrada)} caracteres'

    print(f'Caso: {nome}')
    print(f'  Entrada:   {descricao}')
    print(f'  Resultado: {resultado}')
    print(f'  Esperado:  {esperado}')
    print(f'  Confere:   {resultado == esperado}')
    print()