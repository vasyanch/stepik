n = int(input())
namespaces = {'global':[None, 'global']}
answer = []
def get(a, b): #a = d[2], b = d[1]
    if b == None:
        answer.append(None)
    else:    
        if a in namespaces[b]:
            answer.append(namespaces[b][1])
        else:
            get(a,namespaces[b][0]) 
for i in range(n):
    d = input().split()
    if d[0] == 'create':
        namespaces[d[1]] = [d[2], d[1]]
    elif d[0] == 'add':
        namespaces[d[1]].append(d[2])
    elif d[0] == 'get':
        get(d[2], d[1])
for i in answer:
    print(i, end = '\n')


print(namespaces)

