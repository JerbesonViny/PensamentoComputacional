def is_odd(number: int) -> bool:
  return number % 2 != 0

def is_prime_number(number: int) -> bool:
  if number == 0 or number == 1:
    return False
  
  number_of_divisors = 1

  for divisor in range(2, number+1):
    if number % divisor == 0:
      number_of_divisors += 1

      if number_of_divisors == 2 and divisor != number:
        return False
    
  return True
    
first_number = int(input("Informe o primeiro numero: "))
second_number = int(input("Informe o segundo numero: "))


if first_number > second_number:
  first_number, second_number = second_number, first_number

odd_non_prime_numbers = []
for number in range(first_number, second_number+1):
  
  if is_odd(number) and not is_prime_number(number):
    odd_non_prime_numbers.append(str(number))

print(f'Numeros impares nao primos [{first_number}-{second_number}]: {", ".join(odd_non_prime_numbers)}')