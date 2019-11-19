print((10 * '#'),('Programa para verificação de triângulos').upper(),(10 * '#'))
r1 = int(input('Cumprimento da reta A: '))
r2 = int(input('Cumprimento da reta B: '))
r3 = int(input('Cumprimento da reta C: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('As retas\nA {}\nB {}\nC {}\nFormam um triângulo'.format(r1, r2, r3))

else:
    print('As retas não formam um triângulo')