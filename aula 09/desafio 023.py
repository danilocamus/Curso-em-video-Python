n = str(input('Digite um numero de 0 a 9999: '))
#sep = n.split()

print('''O numero digitado é: {}\n Ele possui:\n {} unidade(s)\n {} dezena(s)\n {} centena(s)\n {} milhar'''
.format(n, n[3], n[2], n[1], n[0]))
