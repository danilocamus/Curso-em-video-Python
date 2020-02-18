from random import randint
from operator import itemgetter

jogadores = {'j1': randint(1, 6), 'j2': randint(1, 6), 'j3': randint(1, 6), 'j4': randint(1, 6)}
vencedores = list()
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} sorteou {v}')
vencedores = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(vencedores)
for i, v in enumerate(vencedores): # i de indice, v de valor
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
# for i, v in enumerate(sorted(jogadores, key=itemgetter(1), reverse=True)):
#     print(f' {v} {jogadores[jogadores]}')
print(v[1])