#include <stdio.h>

def multiplica(a, b):
	if (b == 0):
		return b
	elif (b == 1):
		return a
	else: 
		return a + multiplica(a, b-1)

def main():
	print("forneca valores para a e b")
	a, b = int(input('Valor de a:')), int(input('Valor de b:'))
	resultado = multiplica(a,b)
	print("resultado da multiplicação = %d" % resultado)
	return 0;

main()
