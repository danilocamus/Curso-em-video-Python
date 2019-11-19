cont = 0


while True:
    n = int(input('Digite a tabuada: '))
    if n < 0:
        break
    while cont < 10:
        cont += 1
        print(f'{n} x {cont} = {n * cont}')


    cont -= 10

