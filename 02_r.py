#Determinar que valor se imprimiría en la consola

cadena = "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis"

sw = 180//13
cad = cadena.split(' ')

if cad[4][3] == cad [1][1] or sw%10 == 13:
	sw += 1

print(sw)

'''
RPTA:
13
'''
