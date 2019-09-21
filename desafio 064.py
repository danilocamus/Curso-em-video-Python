c = 0
flag = 0
soma = 0
n = 0
while flag != 999:
    n = int(input('Digite um numero inteiro. Para sair digite o valor ''999: '))
    if n != 999:
        soma += n
        c += 1
    else:
        flag = 999
print('{} numeros foram digitados. A soma total é de {}'.format(c, soma))


'''
num = cont = soma = 0
num = int(input('Digite um numero. Para sair digite [ 999 ]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero. Para sair digite [ 999 ]: '))
print('você digitou {} numero. A soma deles é de {}.'.format(cont, soma))
'''