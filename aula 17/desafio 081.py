lista = []
cont = 0
while True:
    sair = ' '
    lista.append(int(input('Digite um valor para pôr na lista: ')))
    cont += 1
    while sair not in 'SsNn':
        sair = str(input('Você deseja continuar? [S/N] '))
    if sair in 'Nn':
        break
print(f'Foram digitados {cont} números')
lista.sort(reverse=True)
print(f'A lista em forma decrescente é {lista}')
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não esta na lista')