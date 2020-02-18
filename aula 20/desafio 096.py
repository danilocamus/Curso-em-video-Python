def area(c, l):
    total = c * l
    print('Area de Terreno')
    print(f'A área de um terreno de {c}x{l} é de {total}M')


area(float(input('Digite o cumprimento do terreno: ')), float(input('Digite a largura: ')))


largura = float(input('Digite a largura (m): '))
cumprimento = float(input('Digite o cumprimento (m): '))
area(largura, cumprimento)