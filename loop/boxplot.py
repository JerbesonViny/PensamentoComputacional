from dataclasses import dataclass
import math

@dataclass
class Quartiles:
  first_quartile: int
  third_quartile: int

@dataclass
class Limits:
  down: int
  up: int

def get_quartiles(numbers: list[int]) -> Quartiles:
  quantity_of_numbers_in_array = len(numbers)

  first_quartile_ref = math.floor(quantity_of_numbers_in_array * (1/4))
  third_quartile_ref = math.floor(quantity_of_numbers_in_array * (3/4))

  first_quartile = 0
  third_quartile = 0
  for index, number in enumerate(numbers):

    if index == first_quartile_ref:
      first_quartile = number
  
    elif index == third_quartile_ref:
      third_quartile = number
    
  return Quartiles(first_quartile, third_quartile)

def get_interquartile(quartiles: Quartiles) -> int:
  return quartiles.third_quartile - quartiles.first_quartile

def get_limits(numbers: list[int], quartiles: Quartiles) -> Limits:
  down_limit = 0
  upper_limit = 0
  interquartile = get_interquartile(quartiles)

  for number in numbers:

    if number >= (quartiles.first_quartile - interquartile) and down_limit == 0:
      down_limit = number

    if number <= (quartiles.third_quartile + interquartile):
      upper_limit = number
  
  return Limits(down_limit, upper_limit)

def is_odd(number: int | float) -> bool:
  return True if number % 2 != 0 else False


def get_median(numbers: list[int]) -> float:
  numbers.sort()
  quantity_of_elements_in_array = len(numbers)
  center_of_array = quantity_of_elements_in_array // 2

  if is_odd(quantity_of_elements_in_array):
    return numbers[center_of_array]
  
  else:
    return (numbers[center_of_array] + numbers[center_of_array-1]) / 2



quantity_of_numbers = int(input('Informe a quantidade de valores que desejas passar: '))

while True:
  numbers = list(map(int, input('Digite os dados: ').split(' ')))

  if len(numbers) != quantity_of_numbers:
    print(f'Erro: Era esperado que fossem informados {quantity_of_numbers}, mas somente {len(numbers)} foram passados.\nTente novamente...')
  
  else:
    for index, number in enumerate(numbers):
      if index != 0 and number < numbers[index-1]:
        raise Exception('Erro: O conjunto tem de estar em ordem crescente.')
      
    break

quartiles = get_quartiles(numbers)
limits = get_limits(numbers, quartiles)
median = get_median(numbers)

print(f'Limite inferior: {limits.down}')
print(f'1o quartil: {quartiles.first_quartile}')
print(f'Mediana: {int(median)}')
print(f'3o quartil: {quartiles.third_quartile}')
print(f'Limite superior: {limits.up}')