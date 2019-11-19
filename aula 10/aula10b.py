n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua media é: {:.1f}'.format(m))
if m >= 6:
    print('Parabéns!, Aprovado')
else:
    print('Sua nota foi {}. Você foi reprovado. Estude mais'.format(m))