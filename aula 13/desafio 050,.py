soma = 0
cont = 0
cont_par = 0
for c in range(1, 7):
    num = int(input('Informe o {} número: '.format(c)))
    cont += 1
    if num % 2 == 0:
        cont_par += 1
        soma = soma + num
print('Foram informados {} números. Sendo {} pares. A soma de todos os pares é {}'.format(cont, cont_par,
                                                                                          soma))