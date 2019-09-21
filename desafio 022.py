nome = str(input('Digite seu nome completo: '))

print(format(nome.upper()))
print(format(nome.lower()))
print(len(nome.replace(' ', '')))
dividido = nome.split()
print(len(dividido[0]))