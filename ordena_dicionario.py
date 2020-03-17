'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
'''
if __name__ == '__main__':
	m = {}
	for _ in range(int(input())):
		name = input()
		score = float(input())
		m[name] = score
	print(m)
	sorted_m = sorted(m.items(), key=lambda kv: kv[1])
	print(sorted_m)
	reverse_sorted_m = sorted(m.items(), key=lambda kv: kv[1], reverse=True)
	print(reverse_sorted_m)
