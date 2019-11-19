print('Verificaçção de Triângulos')
a = int(input('Digite o comprrimento da reta A: '))
b = int(input('Digite o comprimento da reta B: '))
c = int(input('Digite o comprimento da reta C: '))
if a < (b + c) and b < (c + a) and c < (b + a):
    print('As retas podem formar um triângulo')
    if a == b == c:
        print('As retas formam um triângulo EQUILÁTERO')
    elif a == b and a != c or a == c and a != b:
        print('As retas formam um triânguilo ISÓSCELES')
    elif a != b and a != c and c != b:  # a != b != c != a:
        print('As retas formam um triângulo ESCALENO')
else:
    print('As retas não formam triângulo')