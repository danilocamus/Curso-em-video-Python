parImpar = [[], []]
for a in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        parImpar[0].append(n)
    else:
        parImpar[1].append(n)
parImpar[0].sort()
parImpar[1].sort()
print(f'Os números pares são: {parImpar[0]}\n'
      f'Os números ímpares são: {parImpar[1]}')