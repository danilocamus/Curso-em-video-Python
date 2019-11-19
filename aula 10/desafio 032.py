print((10 * '*'), 'Calculadora de ano bissexto', (10 * '*'))
ano = int(input('Digite um ano para saber se ele é bissexto: '))
sit1 = ano % 4
if (ano % 4) != 0 and ano % 400 != 0:
    print('O ano {} nao é bissexto'.format(ano))
else:
    print('O ano {} é bissexto'.format(ano))