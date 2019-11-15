idade = 0
cont18 = 0
cont_homem = 0
cont_mulher20 = 0
while True:
    print('CADASTRO DE PESSOAS')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
        cont_mulher20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar cadastando? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'{cont18} Pessoas com mais de 18 anos.\n{cont_homem} homens cadastrados\n'
      f'{cont_mulher20} Mulheres com menos de 20 anos')