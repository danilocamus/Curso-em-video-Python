#nome = str(input('Qual é o seu nome? '))
"""print('olá {:=^20}'.format(nome))
print('olá {:>20}'.format(nome))
print('olá {:<20}!'.format(nome))
print('olá {:20}!'.format(nome))"""

n1 = int(input('valor 1: '))
n2 = int(input('valor 2: '))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n o produto é {}\n e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))