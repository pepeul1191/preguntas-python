#Determinar que valor se imprimiría en la consola

numerador = 131.34
denominador = 5

x = numerador//denominador
y = numerador%denominador

lenguajes = ['PHP', 'Python', 'Perl']

if x < y:
	lenguajes.append('Lua')
else:
	lenguajes.pop(2)

lenguajes.append(len(lenguajes)**4)

print(lenguajes)

'''
RPTA:
['PHP', 'Python', 16]
'''