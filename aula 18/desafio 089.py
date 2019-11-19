ficha = list()

while True:
    sair = ' '
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input(f'Digite a primeira nota do {nome}: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    while sair not in 'SsNn':
        sair = str(input('Deseja continuar? [ S/N ] ').strip())
    if sair in 'Nn':
            break

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('=' * 30)
    opt = int(input('Qual aluno você quer mostrar as notas? (999 interrompe): '))
    if opt == 999:
        break
    if opt <= len(ficha) - 1:
        print(f'Notas de {ficha[opt][0]} são {ficha[opt][1]}')