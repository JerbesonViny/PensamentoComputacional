quantity_inputs = int(input("Informe a quantidade de numeros que deseja passar como entrada: "))
numbers = []

for i in range(quantity_inputs):
  number = int(input())

  numbers.append(number)

option = int(input('Primeira opcao: '))
first_index = int(input('Qual o A? '))
second_index = int(input('Qual o B? '))

if option == 0:
  print(f'{numbers[first_index-1]} + {numbers[second_index-1]} = {numbers[first_index-1] + numbers[second_index-1]}')
else:
  print(f'{numbers[first_index-1]} * {numbers[second_index-1]} = {numbers[first_index-1] * numbers[second_index-1]}')