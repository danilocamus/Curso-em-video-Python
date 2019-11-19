print('TABUADA')
tab = int(input('Digite um número para saber sua tabudada: '))
for c in range(1, 11):
    mult = c * tab
    print('{} x {} = {}'.format(tab, c, mult))