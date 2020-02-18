from random import randint
lst = list()


def sorteia(lista):
    for a in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')


def somaPar(somar):
    soma = 0
    for p in somar:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores pares de {somar} temos {soma}')


sorteia(lst)
somaPar(lst)
