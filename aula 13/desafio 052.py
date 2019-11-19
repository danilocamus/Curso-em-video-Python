primo = int(input('Digite um numero para saber se é primo: '))
for c in range(1, primo + 1):
    if primo % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')