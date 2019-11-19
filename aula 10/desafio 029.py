vel = int(input('Qual era a velocidade do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print('O limite de velocidade é 80, sua velocidade era {}, portando você deverá pagar R$ {} de multa '
          .format(vel, multa))
else:
    print('Velocidade permitida')