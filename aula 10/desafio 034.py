print('Programa para calcular aumento salarial'.upper())
sal = float(input('Digite seu salário: '))
aumento1 = sal * 110 / 100
aumento2 = sal * 115 / 100
if sal > 1250:
    print('Seu salário antigo era de R$ {} e agora é de R$ {}'.format(sal, aumento1))
else:
    print('Seu salário antigo era de R$ {} e agora é de R$ {}'.format(sal, aumento2))