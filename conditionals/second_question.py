first_text = input("Texto 1: ").lower()
second_text = input("Texto 2: ").lower()
third_text = input("Texto 3: ").lower()

sequence = []

if first_text < second_text and first_text < third_text:
  sequence.append(first_text)
  if second_text < third_text:
    sequence.extend([second_text, third_text])
  else:
    sequence.extend([third_text, second_text])

elif second_text < first_text and second_text < third_text:
  sequence.append(second_text)
  if first_text < third_text:
    sequence.extend([first_text, third_text])
  else:
    sequence.extend([third_text, first_text])

else:
  sequence.append(third_text)
  if second_text < third_text:
    sequence.extend([first_text, second_text])
  else:
    sequence.extend([second_text, first_text])

print('Seguem os textos em ordem:')
for idx, value in enumerate(sequence):
  print(f'{idx+1}o. {value}')