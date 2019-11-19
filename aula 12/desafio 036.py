print('Calculo para Empréstimo')
val = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é seu salário? '))
anos = int(input('Em quantos anos será o financiamento? '))
prest_mens = val / (anos * 12)
val_prest = (sal * 30) / 100
print('Você pretende comprar uma casa no valor de R$ {:.2f} em {} anos'.format(val, anos), end=' ')
print('O valor da sua prestação será de R$ {:.2f} mensais'.format(prest_mens))
if prest_mens <= val_prest:
    print('Empréstimo Aprovado!')
else:
    print('Empréstimo Negado')