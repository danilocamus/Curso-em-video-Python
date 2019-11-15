import random
ia = 0
tot = 0
vit = 0
while True:
    n = int(input('Digite um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    ia = random.randint(0, 10)
    tot = (n + ia) % 2
    if tot == 0:
        if pi in 'P':
            print(f'Você jogou {n} e escolheu PAR. O computador escolheu {ia} e ÍMPAR. Total de {n + ia}')
            print('Parabéns, você VENCEU!')
            vit += 1
        elif pi in 'I':
            print(f'Você jogou {n} e escolheu ÍMPAR. O computador escolheu {ia} e PAR. Total de {n + ia}')
            print('Você PERDEU!')
            break
    if tot == 1:
        if pi in 'I':
            print(f'Você jogou {n} e escolheu ÍMPAR. O computador escolheu {ia} e PAR. Total de {n + ia}')
            print('Você VENCEU!')
            vit += 1
        elif pi in 'P':
            print(f'Você jogou {n} e escolheu PAR. O computador escolheu {ia} e ÍMPAR. Total de {n + ia}')
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Fim de Jogo. Você venceu um total de {vit} vez(es)')