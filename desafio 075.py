
posiTres = 0
pares = 0
numero = int(input('primeiro valor: ')), int(input('Segundo valor: ')), int(input('Terceirro valor: ')),\
         int(input('Terceiro valor: '))
print(30 * '=-')
print(f'O valor 9 apareceu {numero.count(9)} vez(es)')
print(30 * '=-')
if 3 in numero:
   print(f'O valor 3 apareceu na posição {numero.index(3)+1}')
else:
    print('Não foi digitado o valor 3')
print(30 * '=-')
print(f'os valores pares digitados foram: ', end='')
for p in numero:
    if p % 2 == 0:
        print(p, end='')
