from datetime import date
ano_atual = date.today().year
print('Alistamento Militar')
ano = int(input('Digite o ano de seu nascimento: '))
idade = ano_atual - ano
dife = 18 - idade
if idade < 18:
    print('Você possui {} anos, e poderá se alistar daqui a {} ano(s)'.format(idade, dife))
elif idade > 18:
    print('Você deveria ter se alistado a {} ano(s)'.format(idade - 18))
else:
    print('Você já esta na idade de alistamento')