number_of_days = int(input("Informe uma quantidade de dias: "))

days = number_of_days % 7
weeks = number_of_days // 7

if days == 0 and weeks == 0:
  print(f'{number_of_days} dias {"equivale" if number_of_days == 0 or number_of_days == 1 else "equivalem"} a nenhum dia')

elif weeks != 0 and days == 0:
  print(f'{number_of_days} {"dia" if number_of_days == 1 else "dias"} {"equivale" if number_of_days == 0 or number_of_days == 1 else "equivalem"} a {weeks} {"semana" if weeks == 1 else "semanas"}')

else:
  print(f'{number_of_days} {"dia" if number_of_days == 1 else "dias"} {"equivale" if number_of_days == 0 or number_of_days == 1 else "equivalem"} a {weeks} {"semana" if weeks == 1 else "semanas"} e {days} {"dia" if days == 1 else "dias"}')