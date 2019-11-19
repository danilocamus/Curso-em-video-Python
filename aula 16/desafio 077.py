palavras = ('curso', 'aprender', 'lista', 'python', 'programar', 'olimpia', 'carro', 'estacionamento',
            'oliva', 'azeite', 'bicicleta')


vogais = 'a', 'e', 'i', 'o', 'u'
for c in palavras:
    print(f'\nNa palavra {c} temos a(as) vogais: ', end='')
    for v in c:
        if v in vogais:
            print(v, end='')
