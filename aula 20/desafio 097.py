def mensagem(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('=' * tam)


mensagem(str(input('Digite uma mensagem: ')))