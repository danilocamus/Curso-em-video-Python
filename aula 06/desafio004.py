algo = input('Digite algo para ser avaliado: ')

print('o tipo primitivo de {} é {}'.format((algo),type(algo)))
print('{} é numerico? {} '.format((algo),algo.isnumeric()))
print('{} tem letras? {} '.format((algo),algo.isalpha()))
print('{} possui letras ou numeros? {} '.format((algo),algo.isalnum()))
print('{} é composto somente por letras maiusculas? {} '.format((algo),algo.isupper()))
print('{} é composto somente por espaços em branco? {} '.format((algo),algo.isspace()))
print('{} é composto somente por letras minusculas? {} '.format((algo),algo.islower()))
