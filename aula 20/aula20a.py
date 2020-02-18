def mensagem(msg):
    print('=-' * 30)
    print(msg)
    print('-=' * 30)

while True:
    mensagem(str(input('Digite uma mensagem: ')))

    while True:
        continuar = str(input('Deseja continua escrevendo mensagens? ')).upper().strip()
        if continuar in 'SN':
            break
        print('Responda apenas S ou N')
    if continuar == 'N':
        break