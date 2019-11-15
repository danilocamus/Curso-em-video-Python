numlist = list()
while True:
    leave = ' '
    num = int(input('Digite um numero para colocar na lista: '))
    if num not in numlist:
        numlist.append(num)
        print('Valor adicionado a lista!')
    else:
        print('Numeros repetidos não são aceitos. Coloque outro número')

    while leave not in 'SsNn':
        leave = str(input('Você deseja continuar colocando numeros na lista? [S/N] '))
    if leave in 'Nn':
       break
print('-=' * 40)
print(f'Os números da sua lista são:\n{sorted(numlist)}')