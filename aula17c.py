valores = list()
# cria uma lista de 5 elementos, na qual o usuário coloca os valores.
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

#lê em qual posição esta cada elemento da lista
for p, d in enumerate(valores):
    print(f'Na posição {p} esta o valor {d}')
print('Final da lista')