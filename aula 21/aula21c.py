def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A local vale {a}')
    print(f'B local vale {b}')
    print(f'C local vale {c}')

a = 5
teste(a)
print(f'A global vale {a}')
