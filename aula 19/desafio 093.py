player = dict()
gols = list()

player['nome'] = str(input('Digite o nome: '))
player['partidas'] = int(input(f'Quantas partidas {player["nome"]} jogou? '))

for i in range(0, player['partidas']):
    gols.append(int(input(f'     Quantos gols na partida {i+1}? ')))
    
print('=-' * 22)
player['gols'] = gols[:]
player['total'] = sum(gols)
print(player)

print('=-' * 22)

for k, v in player.items():
    print(f'O campo {k} tem valor {v}')
print('=-' * 22)

print(f'O jogador {player["nome"]} jogou {player["partidas"]} partidas')
for a in range(0, player['partidas']):
    print(f'      => Na partida {a+1} fez {gols[a]} gols')

print(f'Foi um total de {player["total"]} gols.')