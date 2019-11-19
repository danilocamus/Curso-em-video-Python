i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print(20 * '=-')
s = 0
for d in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de tudo é {}'.format(s))