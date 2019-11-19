valores = []
#valor = list() outra forma de criar uma lista vazia

numeros = list(range(2, 8)) # cria uma lista com numeros de 2 ate 7
print(numeros)

valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}-', end='\n')

for p, d in enumerate(valores):
    print(f'\nNa posição {p} esta o valor {d}!')
print('\nFinal da Lista')