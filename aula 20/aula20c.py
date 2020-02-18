def contador(* num): # dessa forma a função ira colocar incontaveis paramentros
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')
    print('=-' * 23)
def contador1(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    print('--' * 23)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
    print('+*' * 23)

contador(2, 2, 5)
contador(1, 6)
contador(9, 9, 3, 5, 2)

contador1(3, 5, 0)
contador1(8, 7)
contador1(3, 9, 1, 9, 0)

soma(10, 2, 1)
soma(8, 7)