def leiaInt(msg):
    ok = False # começa com valor falso ate digitar um numero valido inteiro
    valor = 0
    while True:
        n1 = str(input(msg)) # variavel n recebe da variavel msg um valor no formato string
        if n1.isnumeric(): # se o valor da variavel n for um numero
            valor = int(n1) # recebe o numero da variavel n
            ok = True # a variavel recebe verdadeiro pois foi digitado um numero aceito
        else:
            print('ERRO! Digite um número inteiro') # caso nao seja digitado um numero valido aparece msg de erro
        if ok: # se a variavel ok for True o loop acaba
            break
    return valor


n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')
