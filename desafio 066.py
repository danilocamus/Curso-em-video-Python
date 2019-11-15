soma = cont = n = 0
while True:
    n = int(input('Digite um número para somar, ou [ 999 ] para sair: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números. A soma de todos eles é {soma}')