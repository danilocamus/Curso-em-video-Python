def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s)')


n = str(input('Digite o nome do jogador: '))
g = str(input('Quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)



'''
def ficha(nome = 'desconhecido', gol = 0):

    if nome == '':

        nome = '<desconhecido>'

    if gol == '':

        gol = '0'

    return f'O jogador {nome} fez {gol} gols no campeonato'



jogador = str(input('Nome do jogador: '))

gols = str(input('Número de gols: '))

print(ficha(jogador, gols))'''

