name = str(input('Diga seu nome: '))
name_div = name.split()
print('Olá {}'.format(name_div[0]))
dist = float(input('Qual é a distancia de sua viagem? '))
preco1 = dist * 0.5
preco2 = dist * 0.45
if dist <= 200:
    print('Você ira percorrer {} KM e o custo da passagem será R$ {}'.format(dist, preco1))
else:
    print('Você irá percorrer {} KM e o custo da passagem será de R$ {}'.format(dist, preco2))

#print('Você viajará {} KM.\nO preço da viagem será {}'.format(dist,preço1) if dist <= 200 else 'Você irá viajar {} KM\nO preço da viagem será {}'
#      .format(dist,preço2))
