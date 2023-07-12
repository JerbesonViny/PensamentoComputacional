import copy

def generate_parts(numbers: list[int], separator_element: int) -> list[list[int]]:
  parts = []
  part = []

  for number in numbers:
    if number == separator_element:
      if part:
        parts.append(copy.deepcopy(part))

        part.clear()
    else:
      part.append(number)
  
  if part: 
    parts.append(copy.deepcopy(part))

  return parts

def display_parts(numbers: list[int], separator_element: int):
  parts = generate_parts(numbers, separator_element)

  if parts:

    for part in parts:
      print(' '.join(str(value) for value in part))

  else: 
    print('Nenhuma')

quantity_of_inputs = int(input('Informe a quantidade de valores que queres passar como entrada: '))
numbers = []

print('Informe a sequencia: ')
for _ in range(quantity_of_inputs):
  number = int(input(''))

  numbers.append(number)

separator_element = int(input('Informe o elemento separador: '))

print('Sequencia resultante: ')
display_parts(numbers, separator_element)