ALFABETO = "abcdefghijklmnopqrstuvwxyz"


def letra_ausente(texto):
    presenca = {}
    letras_ausentes = []

    for letra in ALFABETO:
        presenca[letra] = False

    for letra in texto.lower():
        if letra in presenca:
            presenca[letra] = True

    for letra, presente in presenca.items():
        if not presente:
            letras_ausentes.append(letra)

    return letras_ausentes


print('=== Exercício 4 – Letra ausente do alfabeto ===')
print()

casos = [
    ('três letras', 'abc', 'defghijklmnopqrstuvwxyz'),
    ('letra repetida', 'aaaa', 'bcdefghijklmnopqrstuvwxyz'),
    ('pangrama completo', 'The quick brown fox jumps over the lazy dog', ''),
    ('só maiúsculas, falta o g', 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DO', 'g'),
    ('com ruído', 'Ab, C! 123 d?', 'efghijklmnopqrstuvwxyz'),
    ('string vazia', '', 'abcdefghijklmnopqrstuvwxyz'),
]

for nome, entrada, esperado in casos:
    resultado = ''.join(letra_ausente(entrada))

    print(f'Caso: {nome}')
    print(f'  Entrada:    "{entrada}"')
    print(f'  Ausentes:   {resultado if resultado else "(nenhuma)"}')
    print(f'  Quantidade: {len(resultado)}')
    print(f'  Confere:    {resultado == esperado}')
    print()
