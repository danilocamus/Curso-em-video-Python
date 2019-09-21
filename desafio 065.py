decisao = str('S')
num = 0
c = 0
media = float(0)
soma = 0
maior = menor = 0
while decisao == 'S':
    num = int(input('Digite um valor: '))
    if c == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    decisao = str(input('Você quer continuar a digitar valores? [ S ] [ N ] ')).upper().strip()[0]
    soma += num
    c += 1
    media = soma / c

print('Você digitou {} números.\nA média desses números é {:.2f}\n'.format(c, media))
print('O maior número digitado foi {}\nO menor número digitado foi {}'.format(maior, menor))
