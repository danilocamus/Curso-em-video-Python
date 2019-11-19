nome = str(input('Qual é o seu nome? ').lower())
if nome == 'danilo':
    print('Belo nome!')
elif nome == 'julia' or nome == 'maria' or nome == 'amanda':
    print('Seu nome é bem popular')
elif nome in 'ana barbara paola olivia':
    print('Mto bonito o seu nome')
else:
    print('Seu nome não é nada demais')
print('Have a nice day {}!'.format(nome))