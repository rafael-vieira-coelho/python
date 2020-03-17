'''
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
'''

def eh_subconjunto_de(a, b):
	for elem_a in a:
		if elem_a not in b:
			return False
	return True		

for _ in range(int(input())):
	x = input()
	a = set(map(int, input().split()))
	z = input()
	b = set(map(int, input().split()))
	print(a.issubset(b))
	print(eh_subconjunto_de(a, b))
