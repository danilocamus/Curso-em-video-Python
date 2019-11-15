lista =[]
listaPares = []
listaImpares = []
while True:
    sair = ' '
    num = int(input('Digite um valor: '))
    lista.append(num)
    while sair not in 'SsNn':
        sair = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if sair in 'Nn':
        break

for p in lista: #percorre todas as posições na lista

    if p % 2 == 0: #se a varriavel que esta na posição p for divisivel por 2
        listaPares.append(p) #coloca o valor dessa variavel em outra lista
    else:
        listaImpares.append(p)

print(f'A lista normal é {lista}')
print(f'A lista de pares é {listaPares}')
print(f'A lista de impares é {listaImpares}')