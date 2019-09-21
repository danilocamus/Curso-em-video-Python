print('Cálculo para pagamento: ')
preco = int(input('Digite o preço do produto: '))
print('Digite:\n[ 1 ] para pagar a vista no dinheiro/cheque\n[ 2 ] para pagar à vista no cartão\n'
                '[ 3 ] para pagar em em ate 2x no cartão\n[ 4 ] para pagamento em '
                '3x ou mais')
opt = int(input('OPÇÃO DE PAGAMENTO: '))
if opt == 1:
    print('Para pagamento à vista no dinheiro você terá 10% de desconto.'
          'O valor do pagamento é de R$ {}'.format(preco * 0.90))
    #preco - (preco * 10 / 100)
elif opt == 2:
    print('Para pagamento à vista no cartão você terá 5% de desconto. O preço final será de R$ {}'.format(
        preco * 0.95
    ))
    #preco - (preco * 5 / 100)

elif opt == 3:
    parcela = preco / 2
    print('Pagamento parcelado em 2x de {}. O preço final é de R$ {}'.format(parcela, preco))
elif opt == 4:
    preco = (preco * 120) / 100
    qnt_parc = int(input('Quantas parcelas? '))
    print('Você irá parcelar em {}x de R$ {}. O total será de R$ {}'.format(qnt_parc, preco / qnt_parc, preco))
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
'''print('Calculo de pagamento.')
opt = int(input('Digite [ 1 ] para pagamento no cartão ou [ 2 ] para pagar no dinheiro/cheque'))
opt1 = int(input('Digite [ 1 ] para parcelar no cartão ou [ 2 ] para pagar à vista no dinheiro ou cheque: '))
if opt == 1:
    print('Informe em quantas parcelas você irá pagar: ')
    parcelas = int(input())

print('Digite [ 1 ] para pagamento no cartão ou [ 2 ] se for dinheirro/cheque: ')
op1 = int(input('Você irá pagar no cartão ou Dinheiro/chque? '))
if opt == 1 and op1'''
