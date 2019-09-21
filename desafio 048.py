print('Calcular a soma de números ímpares múltiplos de 3 entre 1 e 500')
'''
soma = 0
cont = 0
for c in range(0, 501, 3):
    cont = cont + 1
    print(c)
    soma += c # ou soma = soma + c
print(soma)
print(cont)'''
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('Dentro deste intervalo existem {} números que são múltiplos de 3.\nA soma deles é de {}'.format(
    cont, soma
))