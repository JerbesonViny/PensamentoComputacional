numbers = []
quantity_input_numbers = 3

if quantity_input_numbers % 2 == 0 and quantity_input_numbers != 0:
  quantity_input_numbers -= quantity_input_numbers

for index in range(quantity_input_numbers):
  number = int(input(f'n{index+1}: '))

  numbers.append(number)

numbers.sort()
numbers_quantity = len(numbers)
half_numbers_quantity = numbers_quantity // 2
highest_number = max(numbers)
lower_number = min(numbers)
middle_number = numbers[half_numbers_quantity]

if highest_number == middle_number and middle_number == lower_number:
  print(f'Todos sao iguais a {middle_number}')
else:
  print(f'maior: {highest_number}')
  print(f'menor: {lower_number}')

  if highest_number == middle_number or lower_number == middle_number:
    print('Nao ha elementos do meio')
  else:
    print(f'meio: {middle_number}')