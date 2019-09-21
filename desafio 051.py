pri_termo = int(input('Digite o primeiro termo de sua PA: '))
razao = int(input('Digite a razão de sua PA: '))
num_termos = int(input('Digite a quantidade de termos que você deseja: '))
ult_termo = pri_termo + (num_termos - 1) * razao
for c in range(pri_termo, ult_termo + 1, razao):
   print('{}'.format(c), end='-> ')
print('FIM')