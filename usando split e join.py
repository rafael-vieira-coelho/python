def split_and_join(line):
    lista = line.split(' ')
    return '-'.join(lista)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
