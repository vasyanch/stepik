s = input(''); t = input('')
i = s.find(t) + 1; ch = 0
while i > 0:
    ch += 1
    i = s.find(t, i) + 1
print(ch)
