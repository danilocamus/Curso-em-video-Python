alunos = list()
dados = dict()
while True:
    sair = ' '
    dados['nome'] = str(input('Digite o nome do aluno: '))
    dados['media'] = float(input(f'Digite a média do(a) {dados["nome"]} '))
    if dados['media'] < 7:
        dados['situacao'] = str('reprovado')
    else:
        dados['situacao'] = str('aprovado')
    alunos.append(dados.copy())
    while sair not in 'SsNn':
        sair = str(input('Deseja continuar? [S/N]').upper().strip()[0])
    if sair in 'N':
        break
print(alunos[0])
print(alunos[1])
print(dados)
for a in alunos:
    for k, v in a.items():
        print(f'{k} é igual a {v}')
    print()