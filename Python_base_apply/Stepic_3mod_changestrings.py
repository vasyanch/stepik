c = input(''); a = input(''); b = input('')
i = 0
while a in c:
    if a in b:
        print('Impossible')
        break
    else:
        c = c.replace(a, b)
        i += 1
else: print(i)

