import random
n1 = str(input('digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
esc = [n1, n2, n3, n4]
rdm = random.choice(esc)

print('O nome sorteado é : {}'.format(rdm))
