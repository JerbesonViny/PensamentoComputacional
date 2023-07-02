def is_triangular(number):
  sum_of_numbers = 0
  n = 1

  while sum_of_numbers < number:
    sum_of_numbers += n
    
    if sum_of_numbers == number:
      return True
    
    n += 1

  return False

number = int(input("Informe um numero inteiro positivo: "))

if is_triangular(number):
  print('eh triangular')
else:
  print('nao eh triangular')