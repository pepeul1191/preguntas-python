#Cómo se visualizaría en consola la impresión de las siguientes variables 

lista = [('Boca Juniors', "Municipal"), ('Boca Juniors', 'Universitario'), ('River Plate', 'Sport Huancayo'), ('Independiente', 'Alianza Lima')]
diccionario = {('Boca Junios', 'Universitario'):789}

for ref in lista:
	if ref[0] in diccionario:
		diccionario[ref[0]].append(ref[1])
	elif 50//1000 == 00 and 50%10007 == 50 and 50/1000==0.05:
		diccionario[ref[1]] = [ref[1][0]]

print(diccionario)

'''
RPTA:
{('Boca Junios', 'Universitario'): 789, 'Sport Huancayo': ['S'], 'Alianza Lima': ['A'], 'Municipal': ['M'], 'Universitario': ['U']}
'''
