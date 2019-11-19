fatorial = 1
n = int(input('Digite um valor numerico para fatorar: '))
cont = n
print('Calculando {}! = '.format(n), end='')
while cont > 0:
    fatorial = fatorial * cont
    #n = n * cont
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1
print('{}'.format(fatorial))