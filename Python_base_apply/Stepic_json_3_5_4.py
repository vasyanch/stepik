import json
data = json.loads(input(''))
def find(a):
    for j in data:
        if a['name'] in j['parents']:
            ans[i['name']].add(j['name'])
            find(j)
ans = {}
for i in data:
    ans[i['name']] = {1}# i- словарь из списка data
    find(i)
for i in sorted(ans):
    print(i, ':', len(ans[i]))



