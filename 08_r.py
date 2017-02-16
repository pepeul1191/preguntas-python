#Cómo se visualizaría en consola la respuesta


f = open("data.txt" , "r")

seleccion = []

for linea in f:
	datos = linea.split("::")
	jugador = {"anio_sub20" : datos[0], "nombre" : datos[1] + " " + datos[2], "club" : datos[3]}
	seleccion.append(jugador)

jugadores = []

for jugador in seleccion:
	jugadores.append(jugador["nombre"])

mayor_caracteres = 0
mayor_jugador = ""

for jugador in jugadores:
	if len(jugador) > mayor_caracteres:
		mayor_caracteres = len(jugador)
		mayor_jugador = jugador

print(mayor_jugador)

'''
RPTA:
Javier Saviola
'''