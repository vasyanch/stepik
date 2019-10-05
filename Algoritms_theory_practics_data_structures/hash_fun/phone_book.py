n = int(input())
table = [None] * (10 ** 7)
for _ in range(n):
    z = input().split()
    if z[0] == 'add':
        table[int(z[1])] = z[2]
    elif z[0] == 'del':
        table[int(z[1])] = None
    else:
        if table[int(z[1])]:
            print(table[int(z[1])])
        else:
            print('not found')
            
