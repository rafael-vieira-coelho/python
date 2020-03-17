def potencia(x, n):		
	if (n == 0):
		return 1
	return x * potencia(x, n - 1)

def main():
	print('Potencia de 3 na 5:', potencia(3,5))
	
main()	
