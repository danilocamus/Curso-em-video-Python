num = 0
n1 = int(input('Digite o PRIMEIRO número: '))
n2 = int(input('Digite o SEGUNDO número: '))
while num != 5:
    print('Escolha uma das opções a seguir: ')
    print('[ 1 ] SOMAR os dois valores\n'
          '[ 2 ] MULTIPLICAR os dois valores\n'
          '[ 3 ] qual é o MAIOR dentre os dois valores\n'
          '[ 4 ] MUDAR os valores\n'
          '[ 5 ] Sair do programa')
    num = int(input())
    if num == 1:
        print('A soma de {} + {} é {}'.format(n1, n2, n1 + n2))
    elif num == 2:
        print('A multiplicação de {} x {} resulta no valor {}'.format(n1, n2, n1 * n2))
    elif num == 3:
        if n1 > n2:
            print('O primeio valor ({}) é MAIOR que o segundo valor ({})'.format(n1, n2))
        else:
            print('O segundo valor ({}) é o MAIOR que o primeiro valor ({})'.format(n2, n1))
    elif num == 4:
        n1 = int(input('Digite o PRIMEIRO valor: '))
        n2 = int(input('Digite o SEGUNDO valor: '))
    elif num == 5:
        print('FINALIZANDO...')
    else:
        print('Opção inválida. Tente novamente')
print('FIM DO PROGRAMA!')