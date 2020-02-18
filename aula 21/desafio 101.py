def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if idade >= 16 and idade < 18 or idade >= 60:
        return f'Você possui {idade} anos e o voto é opcional'
    elif idade >= 18 and idade < 60:
        return f'Você possui {idade} anos e o voto é obrigatorio'
    else:
        return f'Você possui {idade} anos e ainda NÂO VOTA'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

#print(ano)


