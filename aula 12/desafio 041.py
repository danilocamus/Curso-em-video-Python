print('Categorias Federaão Nacional de Natação'.upper())
nasc = int(input('Digite o ano de seu nascimento: '))
idade = 2019 - nasc
if idade <= 9:
    print('Você possui {} anos de idade. Sua categoria é MIRIM'.format(idade))
elif idade <= 14:
    print('Você possui {} anos de idade. Sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('Você possui {} anos de idade. Sua categoria é JUNIOR'.format(idade))
elif idade <= 20:
    print('Você possui {} anos de idade. Sua categoria é SÊNIOR'.format(idade))
else:
    print('Você possui {} anos de idade. Sua categoria é MASTER'.format(idade))