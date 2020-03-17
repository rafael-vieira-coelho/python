'''
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
'''
if __name__ == '__main__':
	n = int(input())
	student_marks = {}
	for _ in range(n):
		name, *line = input().split()
		scores = list(map(float, line))
		m = sum(scores)/len(scores)
		student_marks[name] = m
	query_name = input()
	print("%.2f" % student_marks[query_name])
