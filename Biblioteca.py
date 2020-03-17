def simetrica(matriz):
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j] != matriz[j][i]:
				return False
	return True
	
def mostra_matriz(m):
	for i in range(len(m)):
		for j in range(len(m[i])):
			print(m[i][j],' ', end="")
		print()
	
def ler_matriz(n):
	return ler_matriz2(n, n)

def ler_matriz2(m, n):
	matriz = []
	for i in range(m):
		linha = []
		for j in range(n):
			print('Valor [', i, ',', j, ']:', end="")
			valor = int(input())
			linha.append(valor)
		matriz.append(linha)	
	return matriz

def conta_linhas_zeros(matriz, m, n):
	contador = 0
	for i in range(m):
		tem_zero = True
		for j in range(n):
			if matriz[i][j] != 0:
				tem_zero = False
				break
		if tem_zero:
			contador += 1
	return contador	

def conta_colunas_zeros(matriz, m, n):
	contador = 0
	for j in range(n):
		tem_zero = True
		for i in range(m):
			if matriz[i][j] != 0:
				tem_zero = False
				break
		if tem_zero:
			contador += 1
	return contador	


def multiplica_matriz(a, b):
	num_linhas_a = len(a)
	num_linhas_b = len(b)
	num_colunas_a = len(a[0])
	num_colunas_b = len(b[0])
	if num_colunas_a != num_linhas_b:
		return None
	c = []	
	for i in range(num_linhas_a):
		linha = []
		for j in range(num_colunas_b):	
			linha.append(0)
			for k in range(num_colunas_a):
				linha[j] += a[i][k] * b[k][j]
		c.append(linha)	
	return c

