frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(" ", "")
''' ou
palavras = frase.split()
junto = ''.join()palavras
'''
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == frase:
    print('A frase é  um palindromo')
else:
    print('A frase não um palindromo')

'''
frase = frase.replace(" ", "")
frase = frase[::-1]
print(frase, len(frase))

for c in range(len(frase), 0, -1):
    print(c)'''