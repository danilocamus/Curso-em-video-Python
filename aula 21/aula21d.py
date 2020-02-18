'''def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(2, 2)
somar(7)
'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 4, 1)
r2 = somar(1, 9)
r3 = somar(2, 4)
print(f'{r1}, {r2}, {r3}')
print(somar(3, 2, 8))

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(3)
f2 = fatorial(7)
f3 = fatorial(4)
print(f'Os resultados são {f1}, {f2}, {f3}')