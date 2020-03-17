def swap_case(s):
    ns = ''
    for p in s:
        if p.isupper():
            ns += p.lower()
        elif p.islower():
            ns += p.upper()
        else:
            ns += p        
    return ns

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
