print('Programa de cáclulo de médias'.upper())
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('A sua média é {:.2f} Você foi {}REPROVADO{}.'.format(media, '\033[31m', '\033[m'))
elif media < 6.9:
    print('Sua média é {:.2f} Você está de {}RECUPERAÇÃO{}.'.format(media, '\033[33m', '\033[m'))
else:
    print('Parabéns, sua média é {:.2f} Você está {}APROVADO{}'.format(media, '\033[32m', '\033[m'))