print('Comparação de números inteiros')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número ({}) é maior que o segundo número ({})'.format(n1, n2))
elif n2 > n1:
    print('O segundo numéro ({}) é maior que o primeiro ({})'.format(n2, n1))
else:
    print('Os dois números são iguais.')