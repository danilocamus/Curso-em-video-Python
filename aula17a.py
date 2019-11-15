num = [2, 5, 9, 1]
num[2] = 3 #o valor na posição 2 da lista é substituido por outro valor
num.append(7) #adiciona um valor ao final da lista
num.sort() #orrganiza os valores em ordem crescente
num.sort(reverse=True) #organiza em ordem reversa, decrescente
num.insert(2, 0) # insere na posição 2 o valor 0
#num.pop() #remove o ultimo elemento da lista
#num.pop(1)  #remove da lista o valor na posição 1
del num[0]
num.remove(2) #remove o primeiro valor 2 da lista
if 4 in num:
    num.remove(4)
else:
    print('Não há numero 5 na lista')
print(num)