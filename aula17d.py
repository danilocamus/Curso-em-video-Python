a = [2, 3, 4, 7]
b = a # Faz uma ligação entre a lista da variavel a na variavel b. Se vc mudar uma, muda as duas
c = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

c = a[:] # desse jeito, vc cria uma copia da lista a na variavel c
c[3] = 1
print(f'Lista C: {c}')