from math import pow
op = float(input('Digite o comprimento do cateto oposto: '))
adj =  float(input('Digite o comprimento do cateto adjacente: '))
cat = pow(op, 2) + pow(adj, 2)
print('O comprimento da hipotenusa é {}'.format(cat))