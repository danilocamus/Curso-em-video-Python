nome = ('d', 'a', 'n', 'i', 'l', 'o')
linguagens = ('Python', 'JavaScript', 'C#', 'PHP')
for pos, c in enumerate(nome):
    print(f'{c} está na posição/índice {pos}')
print(30 * '=-')
for pos, c in enumerate(linguagens):
    print(f'{c} está na posição/índice {pos}')
print(30 * '=-')
for cont in range(0, len(linguagens)):
    print(f'Eu vou aprender {linguagens[cont]} na posição {cont}')
#print(sorted(nome)) # organiza a tupla em ordem alfabetica
print(30 * '=-')
for c in nome:
    print(f'{c}', end=' ')
