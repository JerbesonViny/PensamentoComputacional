import copy
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

def is_valid_withdraw(withdrawn_value: float, balance: float) -> bool:
  return withdrawn_value <= balance

def is_valid_deposit(deposit_value: float) -> bool:
  return deposit_value > 0

def display_options() -> int:
  print('Qual operacao voce deseja realizar?\n' \
  '1 - SAQUE\n'
  '2 - DEPOSITO\n'
  '3 - SALDO\n'
  '4 - SAIR'
  )

  return int(input('Escolha: '))

def display_balance(balance: float) -> None:
  print(f'O seu saldo atual é de: {locale.currency(balance)}')


def withdraw(balance: float):
  new_balance = copy.deepcopy(balance)
  withdrawn_value = float(input('Qual valor você deseja sacar? '))
  
  if is_valid_withdraw(withdrawn_value, balance):
    new_balance -= withdrawn_value
    print(f'Saque autorizado. Agora o seu saldo atual é de: {locale.currency(new_balance)}')
  else:
    print('Saldo insuficiente.')
  
  return new_balance


def deposit(balance):
  new_balance = copy.deepcopy(balance)
  deposit_value = float(input('Qual o valor que você quer depositar? '))

  if is_valid_deposit(deposit_value):
    new_balance += deposit_value
    print(f'O seu saldo agora é de: {locale.currency(new_balance)}')
  else:
    print('Valor inválido')
  
  return new_balance

def process_option(option: int, balance: float) -> None:
  options = {
    1: 'Withdraw',
    2: 'Deposit',
    3: 'Display balance',
    4: 'Logout'
  }

  if option not in options.keys():
    print('Opção inválida, tente novamente!')

  elif options[option] == 'Withdraw':
    return withdraw(balance)

  elif options[option] == 'Deposit':
    return deposit(balance)

  elif options[option] == 'Display balance':
    display_balance(balance)
    

def main():
  option = 0
  balance = 1000
  
  while True:
    option = display_options()

    if option == 4:
      print('Obrigado por usar os serviços do Caixa Eletrônico')
      break
    
    elif option in [1, 2]:
      balance = process_option(option, balance)

    else:
      process_option(option, balance)

main()