def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(2, 14)


def somatoria(* num):
    so = 0
    for n in num:
        so += n
    print(f'{num}, {so}')

somatoria(4, 5, 10)