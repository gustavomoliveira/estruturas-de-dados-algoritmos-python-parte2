def primeiro_duplicado(array):
    vistos = {}

    for elemento in array:
        if elemento in vistos:
            return elemento

        vistos[elemento] = True

    return None

print('=== Exercício 3 – Primeiro valor duplicado ===')
print()

casos = [
    ('duplicado no meio', ["maçã", "banana", "laranja", "uva", "banana", "pera"], "banana"),
    ('duplicado no fim', ["rio", "sol", "mar", "lua", "vento", "chuva", "rio"], "rio"),
    ('duplicados vizinhos', ["gato", "gato", "cachorro", "peixe", "pássaro"], "gato"),
    ('maiúsculas distintas', ["Ana", "ana", "Bia", "Caio", "Bia"], "Bia"),
    ('array grande', [f"item{i}" for i in range(10_000)] + ["item1234"], "item1234"),
    ('sem duplicados', ["a", "b", "c"], None),
]

for nome, entrada, esperado in casos:
    resultado = primeiro_duplicado(entrada)

    if len(entrada) <= 10:
        descricao = str(entrada)
    else:
        descricao = f'{len(entrada)} elementos'

    print(f'Caso: {nome}')
    print(f'  Entrada:   {descricao}')
    print(f'  Resultado: {resultado}')
    print(f'  Esperado:  {esperado}')
    print(f'  Confere:   {resultado == esperado}')
    print()
