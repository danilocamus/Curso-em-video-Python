import random
computer = random.randint(0, 10)
print('Tente adivinhar número')
acertou = False
palpites = 0
while not acertou:
    player = int(input('Digite o seu palpite: '))
    palpites += 1
    if player == computer:
        acertou = True
print('Acertou com {} palpites'.format(palpites))


'''num = 0
n = 1
cont = 0
while num != n:
    num = int(input('Tente adivinhar o número: '))
    n = random.randint(0, 5)
    cont += 1
print('Ao total foram necessários {} palpites'.format(cont))'''