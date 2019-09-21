print('Programa para ler números pares')
a = int(input('Digite de onde se inicia a contagem: '))
b = int(input('Digite o número que termina a contagem de pares: '))
if a >= b or a == b:
    print('O valor inicial não pode ser maior ou igual o valor final. Escolha outros números')
else:
    for c in range(a, b + 1):
        if c % 2 == 0:
            print(c)
'''
print('Programa para ler números pares de 1 a 50')
for c in range (2, 50, 2):
    print(c)'''