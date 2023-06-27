first_text = input("Digite o texto A: ")
second_text = input("Digite o texto A: ")

length_first_text = len(first_text)
length_second_text = len(second_text)
first_union_second = first_text + second_text

first_text_contains_second_text = second_text in first_text
second_text_contains_first_text = first_text in second_text

first_letter_of_first_text = first_text[0]
first_letter_of_second_text = second_text[0]

last_letter_of_first_text = first_text[-1]
last_letter_of_second_text = second_text[-1]

print(f'tamanho(A) - tamanho(B) = {length_first_text - length_second_text}')
print(f'A + B = {first_union_second}')
print(f'A contem B = {first_text_contains_second_text}')
print(f'B contem A = {second_text_contains_first_text}')
print(f'Primeira letra de A = {first_letter_of_first_text}')
print(f'Primeira letra de B = {first_letter_of_second_text}')
print(f'Ultima letra de A = {last_letter_of_first_text}')
print(f'Ultima letra de B = {last_letter_of_second_text}')