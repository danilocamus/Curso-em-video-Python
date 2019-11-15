matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
sum = 0
maior = 0
linha = 0
for l1 in range(0, 3):
    for col1 in range(0, 3):
        matriz[l1][col1] = int(input(f'Digite um número para a linha {l1} coluna {col1}: '))

        # fazendo o programa somar números pares
        if matriz[l1][col1] % 2 == 0:
            soma += matriz[l1][col1]

        # fazendo o progama somar os números da última coluna
        sum += matriz[l1][2]

        # verificando o maior número da segunda linha
        linha = matriz[1][col1]
        if linha > maior:
            maior = linha

print('#$' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()


print(f'a soma dos números pares é {soma}')
print(f'a soma dos valores da terceira coluna é {sum}')
print(f'O maior valor da segunda linha é {maior}')