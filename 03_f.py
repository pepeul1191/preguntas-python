#Determinar que valor se imprimiría en la consola

numerador = 26
denominador = 5

x = 26//5
y = 26%5

lenguajes = ['PHP', 'Perl', 'Python']

if x < y:
	lenguajes.append('Lua')
else:
	lenguajes.pop(2)

lenguajes.append(len(lenguajes))

print(lenguajes)

'''
RPTA:
['PHP', 'Perl',2]
'''