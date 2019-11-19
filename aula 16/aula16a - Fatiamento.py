'''Tuplas são imutáveis.'''
linguagens = ('Python', 'JavaScript', 'C#', 'PHP')
print(linguagens[1]) #mostra a tupla que esta no índice 1 nesse caso o JavaScript
print(linguagens[0][1]) #mostra a tupla de indice 0 e o caractere de índice 1 dessa tupla
print(linguagens[1:3])
print(linguagens[1:])
print(linguagens[-2:])
print(len(linguagens))
for cont in range(0, len(linguagens)):
    print(f'Eu vou aprender {linguagens[cont]} na posição {cont}')
print(20 * '-=')
