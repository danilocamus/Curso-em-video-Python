cadastro = dict()
listagem = list()
mulheres = list()

media = 0

soma = 0
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F] ').upper().strip())
        if cadastro['sexo'] in 'MF':
            break
        print('Digite apenas M ou F')
    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro['nome'])

    cadastro['idade'] = int(input('Idade: '))

    soma += cadastro['idade']
    listagem .append(cadastro.copy())
    cadastro.clear()

    while True:
        continuar = str(input('Deseja continuar cadastrando? ')).upper()[0]
        if continuar in 'SN':
            break
        print('Responda apenas S ou N')
    if continuar == 'N':
        break
media = soma / len(listagem)
print(listagem)
print(f'Foram cadastradas {len(listagem)} pessoas')

print(f'A média de idade do grupo é de {soma / len(listagem):.1f} anos.')
print(f'As mulheres cadastradas foram: {mulheres}')
print('Lista de pessoas tem a idade acima da média: ')

for i in listagem:
    if i['idade'] >= media:
        print('   ', end='')
        for k, v in i.items():
            print(f'{k} = {v}', end='')
        print()
print('Fim do Programa')
# for i in range(len(listagem)):
#     if listagem[i]['idade'] > media:
#         print(f'Nome: {listagem[i]["nome"]}; Sexo: {listagem[i]["sexo"]}; Idade: {listagem[i]["idade"]}')