def fatorial(n):
	if (n == 0):
		return 1
	print('%d * fatorial(%d)' % (n, (n - 1)))
	return n * fatorial(n - 1)

def main():
	print('O fatorial de 5 é %d' % fatorial(5))
        
main()    
