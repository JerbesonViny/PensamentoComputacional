names = []
number_of_names = int(input("Digite a quantidade de nomes que voce quer informar: "))

for quantity in range(number_of_names):
  name_input = input("")

  names.append(name_input)

print('Voce digitou: ')
reverse_names = names[::-1]

for name in reverse_names:
  print(name)