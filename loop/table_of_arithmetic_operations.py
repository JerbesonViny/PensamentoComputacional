first_number = int(input("Digite o primeiro numero: "))
second_number = int(input("Digite o segundo numero: "))

if first_number > second_number:
  first_number, second_number = second_number, first_number

for number in range(first_number, second_number + 1):
  print(f'=-=-=-= Tabuada de {number} =-=-=-=')

  for j in range(1, 11):
    print(f'{number} x {j} = {number*j}')