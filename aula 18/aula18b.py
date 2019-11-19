'''jeito errado de copiar uma lista e modificar a copia.
    o pessoas.append(teste) esta criando uma ligação entre as 2 listas, entao se vc modificar uma
    modifica outra.'''
teste = list()
teste.append('Aline')
teste.append(25)
pessoas = list()
pessoas.append(teste[:]) #com essa estrutura vc cria uma copia da lista teste, caso contrario criaria ligação
teste[0] = 'Vicky'
teste[1] = 26
pessoas.append(teste[:]) #cria uma cópia da lista teste
print(pessoas)


