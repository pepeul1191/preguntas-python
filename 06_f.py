#Indique el resultado de la función 'funcion_dificil' si el primer argumento es 5 y el segundo 3

def numerador(x, n):
	return (x**n)/(n+1)

def denominador(n):
	return (n+1)

def funcion_dificil(x, n):	
	acumulador = 0
	for temp in range(0, n): 
		num=  numerador(temp, x)
		den = denominador(temp) 
		division = num / den
		#print(division)
		acumulador = acumulador + division
	
	return acumulador

print(funcion_dificil(5, 3))

'''
RPTA:
1.861
'''