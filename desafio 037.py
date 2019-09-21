print('Calculadora de Conversão')
n = int(input('Digite um número para convertermos: '))
print('''Escolha uma opção para converter
[ 1 ] Converte o número para BINÁRIO
[ 2 ] Converte o número para OCTAL
[ 3 ] Converte o númeo para HEXADECIMAL''')
opt = int(input('Digite sua opção: '))
if opt == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(n, bin(n)[2:]))
elif opt == 2:
    print('O número {} convertido para OCTAL é {}'.format(n, oct(n)[2:]))
elif opt == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    print('Opção Inválida. Tente Novamente')