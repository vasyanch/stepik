import requests, re
a = input('')
b = input('')
req1 = requests.get(a)
req2 = requests.get(b)
f = re.findall(r'<a href=".+"', req1.text)
l = 0
for i in f:
    req = requests.get(i[9:-1])
    if re.search(r'<a href="{}"'.format(b), req.text):
        print('Yes')
        break
    l += 1
if len(f) == l:
    print('No')
        
