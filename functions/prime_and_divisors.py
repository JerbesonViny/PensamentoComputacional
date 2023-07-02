def get_divisors(number):
  divisors = []

  for divisor in range(1, number+1):
    if number % divisor == 0:
      divisors.append(divisor)

  return divisors

def is_prime_number(number: int) -> bool:
  if number == 0 or number == 1:
    return False
  
  divisors = get_divisors(number)

  return True if len(divisors) == 2 else False

quantity_of_numbers = int(input('Qual o valor de N? '))

numbers = []
print('Digite os valores: ')
for i in range(quantity_of_numbers):
  number = int(input())

  numbers.append(number)

print('A classificacao eh: ')
for number in numbers:
  
  if is_prime_number(number):
    print(f'{number} eh primo')
  else:
    print(f'{number} nao eh primo, os divisores sao: {get_divisors(number)}')