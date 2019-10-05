n = int(input())
classes, answer = {}, []
for i in range(n):
    d  = input()
    if ':' in d:
        d0, d_ = d.split(':')[0].rstrip(), d.split(':')[1].lstrip().split()
        if d0 in list(classes.keys()):
            for i in d_:
                classes[d0].add(i)
                if i in list(classes.keys()):
                    classes[d0] = classes[d0] | classes[i]
                else:
                    classes[i] = set()
            for i in list(classes.keys()):
                if d0 in classes[i]:
                    classes[i] = classes[i] | classes[d0]            
        else:
            classes[d0] = set()
            for i in d_:
                classes[d0].add(i)
                if i in list(classes.keys()):
                    classes[d0] = classes[d0] | classes[i]
                else:
                    classes[i] = set()
    else:
        classes[d] = set()
print(classes)
q = int(input())
for i in range(q):
    call = input().split()
    if call[0] in classes[call[1]]:
        answer.append('Yes')
    else:
        answer.append('No')
for i in answer:
    print(i, end = '\n')
