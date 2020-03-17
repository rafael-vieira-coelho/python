filename = 'Alice.txt' 
try: 
	with open(filename) as f_obj: 
		contents = f_obj.read() 
		words = contents.split() 
		num_words = len(words)
		print('O arquivo ' + filename + ' tem ' + str(num_words) + ' palavras.')
except FileNotFoundError: 
	msg = 'Desculpe, o arquivo ' + filename + ' não existe.' 
	print(msg)
