matriz = [
			['A', 'B', 'C', 'D'],
			['E', 'F', 'G', 'H'],
			['I', 'J', 'K', 'L'],
			['M', 'N', 'O', 'P'],
		]

for num in range(1,5):
	x = num % 2
	if x == 0:
		print(matriz[x][num // 2]) 

'''
RPTA:
B
C
'''