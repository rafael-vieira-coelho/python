def entraNumero():
	x = int(input ("Escolha um número: "))
	if x == 17:
		raise Exception("17 é um número ruim")
	return x
	
def main():
	try:
		x = entraNumero()
		print(x)
	except:
		print('Você não pode escolher o 17')
	
main()	
