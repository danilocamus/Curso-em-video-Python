linguagens = ('Python', 'JavaScript', 'C#', 'PHP')
a = (2, 5, 7)
b = (9, 6, 3, 5)
c = a + b #concatena as tuplas
print(c)
print(b + a)
print(len(c))
print(c.count(5)) #conta qntas vezes aparece o numero 5 na tupla c
print(c.index(5)) # em que posição esta o primeiro numero 5 da tupla c
print(c.index(5, 6)) #em qual posição esta o primeiro 5 contando a partir da posição 6
print(sorted(linguagens)) # organiza a tupla em ordem alfabetica
