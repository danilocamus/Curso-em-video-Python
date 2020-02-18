pessoas = {'nome': 'camila', 'sexo': 'F', 'idade': 28}
print(pessoas['idade'])
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos de idade')

print('-=' * 22)
print('Usando values()')
for v in pessoas.values():
    print('-', v)
print('=-' * 21)
print('Usando o items()')
for i in pessoas.items():
    print('-', i)
print('-=' * 21)
print('forma diferente de mostrar items')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=' * 21)
print('Usando o keys()')
for k in pessoas.keys():
    print('-', k)