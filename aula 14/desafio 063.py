n1 = 0
n2 = 1
n3 = n1 + n2
num = int(input('Quantos termos de Fibonacci você deseja ver? '))
cont = 0
while cont < num:

    print('{} -> '.format(n1),end='')
    n1 = n2
    n2 = n3
    n3 = n1 + n2

    cont += 1
print('FIM')