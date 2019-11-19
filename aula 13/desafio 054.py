from datetime import datetime
maior = 0
menor = 0
quant = int(input('Digite quantas pessoas você quer analisar: '))
data = datetime.now()
for c in range(1, quant + 1):
    idade = int(input('Informe o ano de nascimento da pessoa {}: '.format(c)))
    if (data.year - idade) < 18:
        maior += 1
    else:
        menor += 1
print('{} pessoa(s) são de maior.\n{} pessoa(s) são de menor.'.format(maior, menor))