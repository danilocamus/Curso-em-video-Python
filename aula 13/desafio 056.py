med_idade = 0
hom_velho = ''
mais_velho = 0
mul_sub20 = 0
for c in range(1, 5):
    print('----- PESSOA {} -----'.format(c))
    nome0 = str(input('Nome: ')).strip().upper()
    idade0 = int(input('Idade: '))
    sexo0 = str(input('Sexo [M/F]: ').strip())
    if idade0 < 20 and sexo0 in 'Ff':
        mul_sub20 += 1
    med_idade += idade0
    if sexo0 in 'Mm':
       if idade0 > mais_velho:
            mais_velho = idade0
            hom_velho = nome0
print('A média de idade do grupo é de {} anos.\nO homem mais velho do grupo se chama {}.\n'
      'Existem {} mulheres com menos de 20 anos.'.format(med_idade / 4, hom_velho, mul_sub20))