from dataclasses import dataclass

@dataclass
class Proximity:
  min: int
  max: int
  distance: int

def read_values() -> list[int]:
  quantity_of_values = int(input('Digite a quantidade de entradas que desejas passar: '))

  values = []
  for _ in range(quantity_of_values):
    number = int(input())

    values.append(number)

  return values

def get_proximity_of_numbers(numbers: list[int]) -> dict[int, Proximity]:
  proximity = {}
  numbers.sort()

  for index, number in enumerate(numbers[1::]):
    max_number = number
    min_number = numbers[index]
    distance = (max_number) - (min_number)

    proximity[index+1] = Proximity(max=max_number, min=min_number, distance=distance)
  
  return proximity


def get_pair(numbers: list[int]) -> list[int]:
  proximity = get_proximity_of_numbers(numbers)

  value = proximity[1]
  for key in proximity.keys():

    if proximity[key].distance < value.distance:
      value = proximity[key]

  return [value.max, value.min]


if __name__ == "__main__":
  numbers = read_values()
  upper_value, down_value = get_pair(numbers)

  print(f'Par mais proximo: {upper_value} e {down_value}')