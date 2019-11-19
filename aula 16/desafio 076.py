listagem = ('Arroz', 10, 'Feijão', 6, 'Leite', 3, 'Ovos', 11)
print('=-' * 30)
print('LISTA DE PREÇOS')
print('=-' * 30)
for p in range (0, len(listagem)):
    if p % 2 == 0:
        print(f'{listagem[p]:.<25}', end='')
    else:
        print(f'R$ {listagem[p]:.2f}')