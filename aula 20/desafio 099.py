def maior(*numeros):
    m = max(numeros)
    count = 0
    mai = 0
    print('Analisando os valores passados...')
    for valores in numeros:
        print(f'{valores} ', end='')
        # if count == 0:
        #     mai = valores
        # else:
        #     if valores > mai:
        #         mai = valores
        count += 1
    print(f'Foram informados ao total {count} valores')
    print(f'O maior valor passado foi {m}')
    # print(f'o valor maior é {mai}')
    print('=-' * 33)

maior(2, 3, 8, 10, 1, 6, 16, 7)
maior(2, 6, 1, 19, 5)
maior(1, 9, 7, 32, 56, 2)