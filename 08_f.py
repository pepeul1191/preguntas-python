#Cómo se visualizaría en consola la respuesta

cadena = 'Un gran poder conlleva una gran responsabilidad'
diccionario = {'Ben Parker': 12}

b = cadena.split('po')

for i in b:
	if i in diccionario:
		diccionario[i] *= 37
	else:
		diccionario[i] = 13

print(diccionario)

'''
RPTA:
{'der conlleva una gran res': 13, 'nsabilidad': 13, 'Un gran ': 13, 'Ben Parker': 12}
'''
