def is_odd(number: int) -> bool:
  return number % 2 != 0

first_number = int(input("n1: "))
second_number = int(input("n2: "))

texts = {}

quantity_of_prime_numbers_in_interval = 0
for number in range(first_number, second_number + 1):
  if is_odd(number): 
    quantity_of_prime_numbers_in_interval +=1

if quantity_of_prime_numbers_in_interval == 1:
  texts["exists"] = "existe"
  texts["numbers"] = "numero"
  texts["primes"] = "primo"
else:
  texts["exists"] = "existem"
  texts["numbers"] = "numeros"
  texts["primes"] = "primos"

print(f'{texts["exists"]} {quantity_of_prime_numbers_in_interval} {texts["numbers"]} {texts["primes"]} entre {first_number} e {second_number}')