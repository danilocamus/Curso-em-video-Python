peso = 0
maior = 0
menor = 0
qnt = int(input('Digite quantas pessoas você quer analisar: '))
for c in range(1, qnt + 1):
    peso = int(input('Digite o peso da pessoa {}: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))