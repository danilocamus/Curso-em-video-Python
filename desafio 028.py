import random
num = int(input('Tente adivinhar o numero escolhido pelo computador de 0 a 5: '))
n = random.randint(0,5)
if num == n:
    print('Parabéns, vc acertou, o numero era {}'.format(num))
else:
    print('Você errou, o número era {}'.format(n))