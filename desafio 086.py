matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha} e {coluna}: '))
print('=-' * 30)
for li in range(0, 3):
    for col in range(0, 3):
        print(f'[ {matriz[li][col]:^5} ]', end='')
    print()