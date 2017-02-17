#Cómo se visualizaría en consola la respuesta

tupla_uno = ('Boca Juniors', 19)
tupla_dos = ('River Plate', 'Boca Juniors', 20, 'Independiente', 'Racing Club de Avellaneda')
tupla_tres = ('Alianza Lima', 'River Plate', 'Universitario de Deportes')

rpta = tupla_dos.count(tupla_uno[0]) + tupla_dos.count(tupla_uno[1] + 5) + tupla_dos.count(tupla_tres[1])

print(rpta)

'''
RPTA:
2
'''
