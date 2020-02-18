alunos = {'nome': 'Joana', 'média': 7, 'ID': 10}
print(f'A aluna {alunos["nome"]} tem média {alunos["média"]} e seu ID é {alunos["ID"]}')
del alunos['média']
for k, v in alunos.items():
    print(f'{k} = {v}')
alunos['ID'] = 14
print(alunos.items())
alunos['idade'] = 24 # adiconando uma nova key no dicionario
print(alunos)