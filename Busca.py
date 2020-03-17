import random

#busca sequencial
def sequential_search(vet, num):
	for i in range(len(vet)):
		if (vet[i] == num):
			return True
	return False		

# busca binária iterativa
def binary_search_ite(vet, num):
	esquerda = 0
	direita = len(vet)	
	while esquerda <= direita:
		meio = (esquerda + direita) // 2
		aux_num = vet[meio]
		if num == aux_num:
			return meio
		elif num > aux_num:
			esquerda = meio + 1
		elif num < aux_num:
			direita = meio - 1
	return None	

# busca binária recursiva
def binary_search_rec(vet, num, esquerda, direita):
	if (direita < esquerda):
		return None
	meio = (esquerda + direita) // 2
	aux_num = vet[meio]
	if num == aux_num:
		return meio
	elif num > aux_num:
		return binary_search_rec(vet, num, meio + 1, direita)

	return binary_search_rec(vet, num, esquerda, meio - 1)

# Programa Principal
def main():
	#vet = [i for i in range(1, 1000001)]
	#num = random.choice(vet)
	#print('Numero escolhido: %d' % num)
	#print('Tentativa (iterativo): %d' % binary_search_ite(vet, num))
	#print('Tentativa (recursivo): %d' % binary_search_rec(vet, num, 0, len(vet), 1))
	seq = [4, 10, 80, 90, 91, 99, 100, 101]
	testes = [50]
	for t in testes:
		if (binary_search_ite(seq, t) != None):
			print('Valor encontrado!')
		else:
			print('Valor não encontrado')	

main()
