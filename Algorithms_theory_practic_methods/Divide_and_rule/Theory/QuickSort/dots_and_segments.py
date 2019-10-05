'''
    Задача:
        В первой строке задано два целых числа 1 ≤ n ≤ 50000
        и 1 ≤ m ≤ 50000 — количество отрезков и точек на прямой,
        соответственно. Следующие n строк содержат по два
        целых числа a_i и b_i (a_i ≤ b_i) — координаты концов
        отрезков. Последняя строка содержит m целых чисел —
        координаты точек. Все координаты не превышают 10^8
        по модулю. Точка считается принадлежащей отрезку,
        если она находится внутри него или на границе.
        Для каждой точки в порядке появления во вводе выведите,
        скольким отрезкам она принадлежит

        Фун. bin_search реализует двоичный поиск и возвращает
    кол-во чисел меньших или равных числу b в массиве massif.
        Фун. bin_search_1 реализует двоичный поиск и возвращает
    кол-во чисел меньших числa b в массиве massif.  
'''

#from QuickSort import test
from random import randint
import array


def bin_search(massif, b):
    n = len(massif)
    m = 0
    while n > m:
        i = (n + m) // 2
        if b >= massif[i]:
            m = i + 1
        else:
            n = i
            i -= 1 
    if n == 0:
        return 0
    else:
        return i + 1


def bin_search_1(massif, b):
    n = len(massif)
    m = 0
    while n > m:
        i = (n + m) // 2
        if b > massif[i]:
            m = i + 1
        else:
            n = i
            i -= 1 
    if n == 0:
        return 0
    else:
        return i + 1 


def quickSort(lst, l=0, r=0):
    while l < r:
        _ = randint(l, r-1)
        lst[l], lst[_] = lst[_], lst[l]
        m, q = partition(lst, l, r)
        if m - l > r - q:
            quickSort(lst, q+1, r)
            r = m
        else:
            quickSort(lst, l, m)
            l = q + 1
    return lst
 

def partition(lst, l, r):
    x = lst[l]
    j = l
    q = l
    for i in range(l+1, r):
        if lst[i] < x:
            j += 1
            lst[j], lst[i] = lst[i], lst[j]
            q += 1
            if q > j:
                lst[q], lst[i] = lst[i], lst[q]
        elif lst[i] == x:
                q += 1
                lst[q], lst[i] = lst[i], lst[q]
    lst[j], lst[l] = lst[l], lst[j]
    return j, q


def main():
    n, m = map(int, input().split())
    start = array.array('q')
    finish = array.array('q')
    for i in range(n):
        d = input().split()
        start.append(int(d[0]))
        finish.append(int(d[1]))
    st = quickSort(start, r=len(start))
    fn = quickSort(finish, r=len(finish))
    print(' '.join(str(bin_search(st, i) - bin_search_1(fn, i))
                   for i in map(int, input().split())))

if __name__ == '__main__':
    main()

