first_text = input("Digite o texto A: ")
second_text = input("Digite o texto B: ")

length_first_text = len(first_text)
length_second_text = len(second_text)

half_length_first_text = length_first_text // 2
half_length_second_text = length_second_text // 2

first_letter_of_first_text = first_text[0]
second_letter_of_second_text = second_text[1]

last_letter_of_first_text = first_text[-1]
last_letter_of_second_text = second_text[-1]

initial_first_text, final_first_text = first_text[0:half_length_first_text], first_text[half_length_first_text::]
initial_second_text, final_second_text = second_text[0:half_length_second_text], second_text[half_length_first_text::]

print(f'Texto A divido em duas partes: {initial_first_text} e {final_first_text}')
print(f'Texto B divido em duas partes: {initial_second_text} e {final_second_text}')
print(f'{initial_first_text} + {final_second_text} = {initial_first_text}{final_second_text}')
print(f'{final_first_text} + {initial_second_text} = {final_first_text}{initial_second_text}')
print(f'{first_letter_of_first_text} + {second_letter_of_second_text} + {last_letter_of_first_text} + {last_letter_of_second_text} = {first_letter_of_first_text}{second_letter_of_second_text}{last_letter_of_first_text}{last_letter_of_second_text}')