import xml.etree.ElementTree as ET

root = ET.fromstring(input())
ans = {'red': 0 , 'green': 0, 'blue': 0}

def func(dic, res, level=1):
    dic[res.attrib['color']] += level
    for i in res.findall('cube'):
        func(ans, i, level+1)

func(ans, root)
print(ans['red'], ans['green'], ans['blue'])
