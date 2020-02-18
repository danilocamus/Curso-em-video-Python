aluno = {'nome': 'Aline', 'idade': 26, 'sexo': 'F'}
for k, v in aluno.items():
    print(f'O {k} é {v}')
locadoras = [{'titulo': 'star wars', 'ano': 1977, 'diretor': 'George Lucas'}, {
                'titulo': 'avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}, {
                'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'
}]
print(locadoras[2].values())
print(locadoras[2]['ano'])
print(locadoras[2]['titulo'])
print(aluno['nome'])