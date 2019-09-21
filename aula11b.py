nome = 'Danilo'
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}
print('Olá {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('Olá {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))