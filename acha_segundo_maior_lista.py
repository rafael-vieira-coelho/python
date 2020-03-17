#5
#2 3 6 6 5
if __name__ == '__main__':
	n = int(input())
	arr = map(int, input().split())
	arr = sorted(arr)
	ultimo = arr[len(arr) - 1]
	pos = -1
	for i in range(len(arr) - 1, -1, -1):
		if ultimo != arr[i]:
			pos = i
			break
	print(arr[pos])
