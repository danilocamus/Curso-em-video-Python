mais_barato = ''
tot = 0
mais_mil = 0
cont = 0
menor = 0
while True:

    cont += 1
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto: R$'))
    tot += preco
    if cont == 1 or preco < menor:
        menor = preco
        mais_barato = nome

    if preco >= 1000:
        mais_mil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja cadastrando? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Total gasto {tot}.\n{mais_mil} Produto(s) custam mais de 1000.\n{mais_barato} É o produto mais barato')