def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 6, 7, 1, 9, 3]


dobra(valores)
print(valores)
