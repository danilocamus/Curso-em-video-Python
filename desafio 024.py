n = str(input('Digite o nome de sua cidade: '))
div = n.split()
print('A cidade é {}\nEla possui santo no nome?\n{}'.format(n, 'santo' in div[0].lower()))
