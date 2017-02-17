#Cómo se visualizaría en consola la respuesta

cadena = 'En una zarzamorera estaba una mariposa zarzarrosa y alicantosa.'
diccionario = {'Salvador Caracuel': 144}

b = cadena.split('po')

for i in b:
	if i in diccionario:
		diccinoario[i] *= 78
	else:
		diccionario[i] = 98

print(diccionario)

'''
RPTA:
{'sa zarzarrosa y alicantosa.': 98, 'Salvador Caracuel': 144, 'En una zarzamorera estaba una mari': 98}
'''
