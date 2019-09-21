import math
n = int(input('Digite um numero: '))
raiz = math.sqrt(n)
print('A raiz de {} é {:.2f} !'.format(n, raiz))
print('A raiz arredondada pra cima de {} é {:.2f} !'.format(n, math.ceil(raiz)))
print('A raiz pra baixo de {} é {:.2f} !'.format(n, math.floor(raiz)))
