num = list()

for d in range(0, 5):
    num.append(int(input(f'Digite um numero para a posição {d}: ')))
print(f'O maior valor da lista é {max(num)} e está na posição {num.index(max(num))}')
print(f'O menor valor da lista é {min(num)} e está na posição {num.index(min(num))}')

print(f'Os elementos da lista são: {num}')
print(f'O maior valor digitado foi {max(num)} nas posições ', end='')
for c, x in enumerate(num):
    if x == max(num):
        print(f'{c} - ', end='')
print()
print(f'O menor valor digitado foi {min(num)} nas posições ', end='')
for c, x in enumerate(num):
    if x == min(num):
        print(f'{c} - ', end='')
print()

