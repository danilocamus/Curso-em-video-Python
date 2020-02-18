from time import sleep
def contador(ini, fim, pas):
    print(f'Contando de {ini} até {fim} de {pas}')
    cont = ini
    if ini < fim:
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += pas
        print('FIM')
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= 1
    print('FIM')


contador(1, 10, 1)
contador(10, 0, -2)
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
