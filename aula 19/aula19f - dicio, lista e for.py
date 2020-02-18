estado = dict()
brasil = list()

# adiciona dicionarios dentro de uma lista
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # faz uma copia do dicionario
print(brasil)
print('=-' * 23)
# comando par mostrar todos os elementos da lista
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print('-=' * 23)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()