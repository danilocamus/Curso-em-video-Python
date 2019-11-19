cadastro = list()
maisPesado = menosPesado = 0
dados = list()
cont = 0
while True:
    sair = ' '
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if cont == 0:
        maisPesado = menosPesado = dados[1]
    else:
        if dados[1] > maisPesado:
            maisPesado = dados[1]
        if dados[1] < menosPesado:
            menosPesado = dados[1]
    cadastro.append(dados.copy())
    dados.clear()
    cont += 1

    while not sair or sair not in 'SsNn':
        sair = str(input('Você deseja continuar? [S/N]').strip().upper())
    if sair in 'Nn':
        break
print(f'Ao todo foram cadastrados {len(cadastro)} pessoas')
print(f'O maior peso foi de {maisPesado} Kg. Peso do(a) ', end='')
for p in cadastro:
    if p[1] == maisPesado:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menosPesado} Kg. Peso do(a) ', end='')
for pe in cadastro:
    if pe[1] == menosPesado:
        print(f'[{pe[0]}]', end='')
