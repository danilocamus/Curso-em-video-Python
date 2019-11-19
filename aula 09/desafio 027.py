n = str(input('Digite seu nome completo: ')).strip()
div = n.split()
print('O primeiro nome é: {}'.format(div[0].upper()))
print('O ultimo nome é: {}'.format(div[len(div)-1].upper()))