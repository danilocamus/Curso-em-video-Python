times = ('Flamengo', 'Palmeiras', 'Santos', 'Corinthians', 'Internacional', 'São Paulo', 'Gremio',
         'Bahia', 'Athletico-PR', 'Atlético', 'Botafogo', 'Goias', 'Vasco da Gama', 'Ceará SC',
         'Fortaleza', 'Fluminense', 'CSA', 'Cruzeiro', 'Avaí', 'Chapecoense')
cont = 1
ultimos = len(times) - 4
print('=-' * 30)
print('Os 5 primeiros colocados do campeonato são: ')
for c in range(0, 5):
    print(f'{cont} - {times[c]}')
    cont += 1
print('=-' * 30)
print(f'Os 4 últimos colocados da tabela são: {times[-4:]}')
print('=-' * 30)
print('Os times em ordem alfábetica:')
print(sorted(times))
print('=-' * 30)
print(f'O Chapecoense se encontra na {times.index("Chapecoense")+1} posição')