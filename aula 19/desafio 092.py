from datetime import datetime

cadastro = dict()
now = datetime.now()
cadastro['nome'] = str(input('Digite o nome: '))

ano_nascimento = int(input('Digite o ano de nascimento: '))

cadastro['idade'] = datetime.now().year - ano_nascimento
cadastro['ctps'] = int(input('Digite o número da carteira profissional ou digite [ 0 ] caso não tenha: '))

if cadastro['ctps'] != 0:
    cadastro['ano_contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposentadoria'] = (cadastro['ano_contratacao'] + 35) - ano_nascimento
for k, v in cadastro.items():
    print(f'O campo {k} tem valor {v}')
