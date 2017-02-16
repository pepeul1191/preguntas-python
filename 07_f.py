#Cómo se visualizaría en consola la respuesta
f = open("data.txt" , "r")

seleccion = []

for linea in f:
	datos = linea.split("::")
	anio = datos[0]
	seleccion.append(int(anio))

seleccion.sort(reverse=True)

print(seleccion[2])

'''
RPTA:
2005
'''