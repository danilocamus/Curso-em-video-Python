name = str(input('Digite seu nome: '))
div = name.split()
print('Olá {}'.format(div[0].capitalize()))
n = int(input('Digite um numero para analisar se é PAR ou ÍMPAR: '))
#n = n % 2
if n % 2 == 0:
    print('O numero {} é par'.format(n))
else:
    print('O numero {} é Impar'.format(n))