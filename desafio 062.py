'''inicio = int(input('Digite o valor inicial da PA: '))
razao = int(input('Digite a razao da PA: '))
cont = 1
num = int(input('Digite quantos termos você quer ler: '))
while cont <= num:
    print('{} -> '.format(inicio), end='')
    inicio += razao
    cont += 1
    if cont == num + 1:
        print('Quantos termos a mais você deseja ver? Digite [ 0 ] para sair')
        num += int(input())

print('PA finalizada. {} termos lidos'.format(cont))
'''
inicio = int(input('Digite o valor inicial da PA: '))
razao = int(input('Digite a razao da PA: '))
cont = 1
num = int(input('Digite quantos termos você quer ler: '))
total = 0
while num != 0:
    total += num
    while cont <= total:
        print('{} -> '.format(inicio), end='')
        inicio += razao
        cont += 1

    print('PAUSE')
    num = int(input('Quantos termo a mais você quer ver? '))

print('PA finalizada. {} termos lidos'.format(total))