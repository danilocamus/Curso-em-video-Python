import random
import time

jogo = []
n = int(input('Quantos jogos você deseja fazer? '))
print(f'=-=-=-=- VAMOS SORTEAR {n} JOGOS =-=-=-=-')
for i in range(0, n):
    jogo.append(sorted(random.sample(range(1, 61), 6)))
    print(f'Jogo {i+1}: {jogo[i]}')
    time.sleep(1)
print('=-=-=-=- GOOD LUCK =-=-=-=-')