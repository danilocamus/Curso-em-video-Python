from random import randint
num = randint(1, 10), randint(1, 10), randint(1,10), randint(1, 10), randint(1, 10)
print('Os valores spteados foram: ')
for n in num:
    print(f'{n} ', end='')
maior = sorted(num)
menor = sorted(num)
print(f'\nO maior número sorteado é {maior[4]}\nO menor número sorteado é {menor[0]}')

#print(f'O maior valor sorteado foi {max(num)}')
#print(f'O menor valor sorteado foi {min(num)}')