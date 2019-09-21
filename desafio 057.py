sexo = str(input('Informe o sexo da pessoa: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Valor inválido. Informe o sexo novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))