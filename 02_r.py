#Determinar que valor se imprimiría en la consola

lista = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']

x = 33
y = 3
valor = x % y

if valor in lista:
	print(lista[-5:-2])
else:
	print(lista[1:3])

'''
RPTA:
['B', 'C', 'D']
'''