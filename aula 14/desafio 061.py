'''pri_termo = int(input('Digite o valor do primeiro termo: '))
raz = int(input('Digite o valor da razão: '))
qnt_termos = int(input('Digite a quantidade de termos da sua PA: '))
pa = pri_termo
ultimo_termo = pri_termo + (qnt_termos - 1) * raz
while pa != ultimo_termo:
    if pa == pri_termo:
        print(pri_termo, end=' - ')
    pa += raz
    print(pa, end=' - ')
print('FIM')
'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(primeiro),end='') # ou no lugar da variavel primeiro, posso usar a var termo
    primeiro += razao # ou termo += razao
    cont += 1
print('FIM')