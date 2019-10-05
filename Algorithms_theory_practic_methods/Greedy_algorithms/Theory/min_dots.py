'''
    Даный код решают след. задачу:
     По данным n отрезкам необходтмо найти множество точек
     минимального размера, для которого каждый из отрезков
     содержит хотя бы одну точку.
     В первой строке дано число 1≤n≤100  отрезков.
     Каждая из последующих n строк содержит по два числа 0≤l≤r≤10^9,
     задающих начало и конец отрезка. Выведите оптимальное число m
     точек и сами m точек. Если таких множеств точек несколько,
     выведите любое из них.
'''
n = int(input(''))
lst = []
for i in range(n):
    seg = list(map(int, input('').split()))
    seg.reverse()
    lst.append(seg)
lst.sort()
#print(lst)
ans = []
while lst:
    x = lst[0]
    ans.append(x[0])
    lst.remove(x)
    i = 0
    while i < len(lst):
        if x[0] >= lst[i][1] and x[0] <= lst[i][0]: lst.pop(i)
        else: i += 1

print(len(ans))
for i in ans:
    print(i)

   

    #Тот же самый функционал, но в 6 строчек
'''
segments = sorted([sorted(map(int,input().split())) for i in range(int(input()))], key=lambda x: x[1])
dots = [segments.pop(0)[1]]
for l, r in segments:
    if l > dots[-1]:
        dots.append(r)
print(str(len(dots)) + '\n' + ' '.join(map(str, dots)))
'''
