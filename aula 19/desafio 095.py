players = dict()
cadastro = list()
gols = list()
while True:
    players.clear()
    players['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {players["nome"]} jogou? '))
    gols.clear()

    for i in range(0, tot):
        gols.append(int(input(f'      Quantos gols na partida {i+1}: ')))

    players['gols'] = gols[:]
    players['total'] = sum(gols)

    cadastro.append(players.copy())

    while True:
        continuar = str(input('Deseja continuar cadastrando? ')).upper()[0]
        if continuar in 'SN':
            break
        print('Responda apenas S ou N')
    if continuar == 'N':
        break
print('=-' * 33)
print('cod ', end='')
for b in players.keys():
    print(f'{b:<15}', end='')
print()
for k, v in enumerate(cadastro):
    print(f'{k:>3} - ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    opc = int(input('Mostrar dados de qual jogador? [999 para sair]'))
    if opc == 999:
        break
    if opc >= len(cadastro):
        print(f'Nao existe jogador com código {opc}')
    else:
        print(f'Levantamento do jogador {cadastro[opc]["nome"]}')
        for i, g in enumerate(cadastro[opc]["gols"]):
            print(f'     no jogo {i+1} fez {g} gols.')
print('programa encerrado')