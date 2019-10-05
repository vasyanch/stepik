'''
   Дана частичная выборка из датасета зафиксированных
   преступлений, совершенных в городе Чикаго с 2001 года
   по настоящее время. Одним из атрибутов преступления
   является его тип – Primary Type. необходимо узнать тип
   преступления, которое было зафиксировано максимальное
   число раз в 2015 году.
'''
import csv, re
lst = []
with open('Crimes.csv') as f:
    for i in csv.reader(f):
        if re.search(r'2015\b', i[2]):
            lst.append(i[5])
d = 0 
for i in set(lst):
    if lst.count(i) > d:
        d = lst.count(i)
        ans = i
print(ans)


#for i in range(len(lst)):
 #  print(lst[i], end = '\n')

