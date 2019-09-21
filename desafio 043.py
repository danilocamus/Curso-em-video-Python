print('Programa de Cálculo de IMC')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura ** 2)
print('Seu índice de IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO IDEAL')
elif imc <= 25:
    print('Você está no seu PESO IDEAL')
elif imc  <= 30:
    print('Você está com SOBREPESO')
elif imc <= 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')