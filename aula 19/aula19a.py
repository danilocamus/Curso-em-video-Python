dados = dict()
dados1 = {'nome': 'Aline', 'idade': 25}
print(dados1['nome'], dados1['idade'])
dados1['sexo'] = 'F'
print(dados1)
del dados1['idade']
print(dados1)
filmes = {'titulo': 'Matrix', 'ano': 1999, 'ator': 'Keanu Reeves'}
print(filmes.values()) # retona todos os valores do dicionário
print(filmes.keys()) # retorna as chaves do dicionário
print(filmes.items()) # retorna os valores e as chaves do dicionario
