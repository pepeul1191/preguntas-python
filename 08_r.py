#Cómo se visualizaría en consola la respuesta


f = open("data.txt" , "r")

seleccion = []

for linea in f:
	datos = linea.split("::")
	jugador = {"anio_sub20" : datos[0], "nombre" : datos[1] + " " + datos[2], "club" : datos[3]}
	seleccion.append(jugador)

clubes = []

for jugador in seleccion:
	clubes.append(jugador["club"])

mayor_caracteres = 0
mayor_club = ""

for club in clubes:
	if len(club) > mayor_caracteres:
		mayor_caracteres = len(club)
		mayor_club = club

print(mayor_club)

'''
RPTA:
Independiente
'''