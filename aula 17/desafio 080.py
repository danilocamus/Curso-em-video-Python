numList = list()
for n in range(0, 5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > numList[-1]: #se n for zero OU se o numero digitado for maior que o ultimo valor da lista
        numList.append(num) #adiciona no final da lista o valor passado
    else:
        pos = 0
        while pos < len(numList): #enqto o valor da variavel pos for menor que a lista, ou seja a variavel vai percorrer toda a lista
            if num <= numList[pos]: #vai comparar o valor digitado com cada valor da lista
                numList.insert(pos, num) #se for menor ou igual, insere nessa posição o valor digitado
                break
            pos += 1
print(numList)