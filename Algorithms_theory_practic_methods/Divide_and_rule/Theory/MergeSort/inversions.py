'''
    Фун. mergeSort реализует алгоритм сортировки слиянием.
    Время работы данного алгоритма O(nlog(n)).
    Первая строка содержит число 1 ≤ n ≤ 10*5,
    вторая — массив A[1…n], содержащий натуральные числа,
    не превосходящие 10*9. Необходимо посчитать число
    пар индексов 1 ≤ i < j ≤n, для которых A[i] > A[j].
    (Такая пара элементов называется инверсией массива.
    Количество инверсий в массиве является в некотором смысле
    его мерой неупорядоченности: например, в упорядоченном по
    неубыванию массиве инверсий нет вообще, а в массиве,
    упорядоченном по убыванию, инверсию образуют
    каждые два элемента.)
'''

import array
def mergeSort(massif, acc=0):
    if len(massif) > 1:
        m = len(massif) // 2
        return merge(mergeSort(massif[0:m]),
                     mergeSort(massif[m:len(massif)]))
    else:
        return (massif, acc)


def merge(a, b):
    ans = array.array('q')
    acc = a[1] + b[1]
    a = a[0]
    b = b[0]
    i = 0
    j = 0
    len_ = len(a)
    while i < len_ and j < len(b):
        if a[i] <= b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1
            acc += len_ - i 
    if i == len_:
        ans += b[j:]
    else:
        ans += a[i:]
    return (ans, acc)


def main():
    n = input()
    massif = array.array('q',(map(int, input().split())))
    print(mergeSort(massif)[1])

if __name__ == '__main__':
    main()
