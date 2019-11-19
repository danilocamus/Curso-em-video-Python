frase = 'Curso em Video Python'
print(frase.upper().count('O'))
frase1 = '   Curso em Video Python   '
print(len(frase.strip()))

#como mudar permanentemente uma string
frase3 = 'Curso em Video Python'
frase3 = frase3.replace('Python', 'Android')
print(frase3)

#mostra a posição da palvra
frase4 = 'Curso em Video Python'
print(frase4.find('Curso'))

#divide a string em listas e mostra o item da lista
frase5 = 'Curso em Video Python'
dividido = frase5.split()
print(dividido[2])
print(dividido[2][3])#pega a string 2 e depois pega a letra da posição 3
