from math import sin, cos, tan, radians

ang = float(input('Digite um angulo: '))
seno = sin(radians(ang))
print('O angulo de {}, possui o seno de {:.2f}'.format(ang,seno))
cosseno = cos(radians(ang))
print('O angulo de {}, possui o cosseno de {:.2f}'.format(ang,cosseno))
tangente = tan(radians(ang))
print('O angulo de {} possui tangente de {:.2f}'.format(ang,tangente))