quantity_players = int(input('Quantidade de jogadores: '))
players = []

team_stats = {
  'percentage_of_successful_attacks': 0,
  'percentage_of_successful_blocks': 0,
  'percentage_of_successful_serves': 0,
  'number_of_attacks': 0,
  'number_of_blocks': 0,
  'number_of_serves': 0,
  'number_of_successfully_serves': 0,
  'number_of_successfully_blocks': 0,
  'number_of_successfully_attacks': 0,
}

print('Digite os dados para cada jogador')

for i in range(quantity_players):
  name, number_of_serves, number_of_blocks, \
  number_of_attacks, number_of_successfully_serves, \
  number_of_successfully_blocks, number_of_successfully_attacks = input('').split(' ')

  percentage_of_successful_attacks = int(number_of_successfully_attacks) / int(number_of_attacks)
  percentage_of_successful_blocks = int(number_of_successfully_blocks) / int(number_of_blocks)
  percentage_of_successful_serves = int(number_of_successfully_serves) / int(number_of_serves)

  player = {
    'name': name,
    'number_of_serves': int(number_of_serves),
    'number_of_blocks': int(number_of_blocks),
    'number_of_attacks': int(number_of_attacks),
    'number_of_successfully_serves': int(number_of_successfully_serves),
    'number_of_successfully_blocks': int(number_of_successfully_blocks),
    'number_of_successfully_attacks': int(number_of_successfully_attacks),
    'percentage_of_successful_attacks': percentage_of_successful_attacks,
    'percentage_of_successful_blocks': percentage_of_successful_blocks,
    'percentage_of_successful_serves': percentage_of_successful_serves
  }

  players.append(player)

for player in players:
  team_stats['number_of_attacks'] += player['number_of_attacks']
  team_stats['number_of_blocks'] += player['number_of_blocks']
  team_stats['number_of_serves'] += player['number_of_serves']

  team_stats['number_of_successfully_serves'] += player['number_of_successfully_serves']
  team_stats['number_of_successfully_blocks'] += player['number_of_successfully_blocks']
  team_stats['number_of_successfully_attacks'] += player['number_of_successfully_attacks']

team_stats['percentage_of_successful_attacks'] = round((team_stats['number_of_successfully_attacks'] / team_stats['number_of_attacks']) * 100, 2)
team_stats['percentage_of_successful_blocks'] = round((team_stats['number_of_successfully_blocks'] / team_stats['number_of_blocks']) * 100, 2)
team_stats['percentage_of_successful_serves'] = round((team_stats['number_of_successfully_serves'] / team_stats['number_of_serves']) * 100, 2)

print('As estatisticas do jogo sao as seguintes:')
print('Pontos de Saque: {:.2f} %'.format(team_stats["percentage_of_successful_serves"]))
print('Pontos de Bloqueio: {:.2f} %'.format(team_stats["percentage_of_successful_blocks"]))
print('Pontos de Ataque: {:.2f} %'.format(team_stats["percentage_of_successful_attacks"]))