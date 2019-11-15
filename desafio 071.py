cedulas = 50
saque = int(input('Digite o valor a ser sacado: '))
totced = 0
total = saque
while True:
    if total >= cedulas:
        total -= cedulas
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cédulas de R$ {cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totced = 0
        if total == 0:
            break