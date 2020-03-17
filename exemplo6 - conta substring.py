'''
ABCDCDC
CDC
2
'''


def count_substring(string, sub_string):
	c = 0
	i = 0
	while i < len(string):
		if string[i] == sub_string[0]:
			eh_sub = True
			i_old = 0
			j = i
			while j < len(string) and i_old < len(sub_string) and string[j] == sub_string[i_old]:
				i_old += 1
				j += 1
			if i_old == len(sub_string):
				c += 1
		i += 1
	return c

if __name__ == '__main__':
	string = input().strip()
	sub_string = input().strip()

	count = count_substring(string, sub_string)
	print(count)
