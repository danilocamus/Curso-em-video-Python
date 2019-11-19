frase = str('Curso em Video Python')
print(frase[9])
print(frase[9:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13)) #conta do 0 ao 12 quantas letras 'o' a frase possui
print(frase.find('deo')) #indica a posição onde se inicia a frase procurada
print(frase.find('android'))#se a frase buscada n existe, ele retorna o valor -1
print('Curso' in frase) #existe a palavra curso na frase?
print(frase.replace('Python', 'Android')) #troca a palavra Python por Android
print(frase.upper())#deixa a frase em maiusculo
print(frase.lower())#deixa a frase em minusculo
print(frase.capitalize()) #deixa somente a primeira letra da frase maiuscula
print(frase.title())#onde tiver espaço ele faz uma quebra, e deixa a primeira letra de cada palvra em maiuscula
print(frase.strip())#remove os espaços antes da frase e do final da frase
print(frase.rstrip())#remove os espaoos inuteis do lado direito, ou seja os do final da frase
print(frase.lstrip())#remove os espaços inuteis do lado esquerdo, ou seja os iniciais
print(frase.split())#faz uma divisao na string considerando os espaços. Cada palavra dividida é colocada em uma lista
print('-'.join(frase))#junta todas as palavras e coloca o '-' como separador de cada palavra
print('''em Ipsum is simply dummy text of the printing and typesetting industry.
 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
 when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
''')