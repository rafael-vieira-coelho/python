f = open("Alice.txt", "r")
c = 0
for linha in f:
	if 'alice' in linha.lower():
		print (linha)
		c += 1
print('O total de alice é: ', c)
