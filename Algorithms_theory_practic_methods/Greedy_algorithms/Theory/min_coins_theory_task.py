n = int(input(''))
lst = [25, 10, 5, 1]
ans = {}
for i in lst:
    if n == 0:
        break
    a = int(n/i)
    if a >= 1:
        n -= a * i
        #print(n)
        ans[i] = a
        #print(ans)
for key in ans.keys():
    print(key, '=>', ans[key])
