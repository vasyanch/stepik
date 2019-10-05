import re, sys
'''
for line in sys.stdin:
    if len(re.findall('cat', line.rstrip())) >=2:
        print(line)
'''
'''
for line in sys.stdin:
    if re.search(r'\bcat\b', line.rstrip()):
        print(line.rstrip())
'''
'''
for line in sys.stdin:
    if re.search(r'z.{3}z', line.rstrip()):
        print(line.rstrip())
'''
'''
for line in sys.stdin:
    if re.search(r'\\', line.rstrip()):
        print(line.rstrip())
'''
'''
for line in sys.stdin:
    if re.search(r'\b(\w+)\1\b', line.rstrip()):
        print(line.rstrip())
'''
'''
for line in sys.stdin:
    print(re.sub(r'human','computer', line.rstrip()))
'''
'''
for line in sys.stdin:
    print(re.sub(r'\ba+\b','argh', line.rstrip(), 1, re.IGNORECASE))
'''
'''
for line in sys.stdin:
    print(re.sub(r'\b(\w)(\w)', r'\2\1', line.rstrip()))
'''
'''
    В каждой строке из станд. потока ввода заменяет
    все вхождения нескольких одинаковых букв на одну эту букву.
for line in sys.stdin:
    print(re.sub(r'(\w)\1+', r'\1', line.rstrip()))
'''
'''
for line in sys.stdin:
    if re.match(r'(1(01*0)*1|0)+', line.rstrip()):
        print(line.rstrip())
'''


        
