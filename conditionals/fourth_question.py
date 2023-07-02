text = input("Informe um texto: ")
length_text = len(text)

first_index = int(input("Informe o primeiro numero: "))
second_index = int(input("Informe o segundo numero: "))

if first_index > second_index:
    first_index, second_index = second_index, first_index

if (first_index >= length_text) or (second_index >= length_text):
    print(f'Erro! Os indices precisam ser menores do que o tamanho do texto ({length_text})')
else:
    print('Partes')
    print(f'Parte 1: {text[0:first_index]}')
    print(f'Parte 2: {text[0:second_index]}')
    print(f'Parte 3: {text[first_index:second_index]}')
    print(f'Parte 4: {text[first_index::]}')
    print(f'Parte 5: {text[second_index::]}')
