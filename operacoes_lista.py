"""
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""
if __name__ == '__main__':
	n = int(input())
	lista = []
	for _ in range(n):
		cmds = input().split()
		cmd = cmds[0]
		if cmd == 'insert':
			lista.insert(int(cmds[1]), int(cmds[2]))
		elif cmd == 'print':
			print(lista)
		elif cmd == 'remove':
			lista.remove(int(cmds[1]))
		elif cmd == 'sort':
			lista.sort()
		elif cmd == 'pop':
			lista.pop()
		elif cmd == 'reverse':					
			lista.reverse()
		elif cmd == 'append':
			lista.append(int(cmds[1]))	
