'''
    Задача:
        Дано целое число 1 ≤ n ≤ 10**5 и массив A[1…n], содержащий
    неотрицательные целые числа, не превосходящие 10 ** 9.
    Найдите наибольшую невозрастающую подпоследовательность в A.
    В первой строке выведите её длину k, во второй — её индексы
    1 ≤ i1 < i2 < … < ik ≤ n (таким образом,
    A[i1] ≥ A [i2] ≥ … ≥ A[in].

    Время работы данного алгоритма O(nlogn). Используется метод
    динамического программирования такой, что для массив D(динамика)
    спарведливо что D[i] хранит элемент массива А на который заканчивается
    невозрастающая подпосл. длины i. Нахождение очередного элемнета
    динамики производиться с помощью фун. bin_search_(так как сам массив D
    будет представлять из себя отсортированный по невозрастанию массив).
    Далее идет восстановление ответа с помощью двух массивов pos и prev.
    Более детальная теория по ссылке:
    http://e-maxx.ru/algo/longest_increasing_subseq_log
'''



def bin_search_(massif, b):
    n = len(massif)
    m = 0
    while n - m > 1:
        i = (n + m) // 2
        if b > massif[i]:
            n = i
        else:
            m = i 
    return m 
      
def noincr(A):
    D = [-1 for i in range(len(A) + 1)]
    D[0] = float('inf')
    prev = [-1] * len(A)
    pos = [-1] * (len(A) + 1)
    for i in range(0, len(A)):
        j = bin_search_(D, A[i])
        if A[i] >  D[j + 1]:
                D[j + 1] = A[i]
                pos[j + 1] = i
                prev[i] = pos[j]

    for i,v  in enumerate(D):
        if v == -1:
            break
        l = i
        k = pos[i]
        
    ans = [0] * l
    for i in range(l-1, -1, -1):
        ans[i] = k + 1
        k = prev[k]
                
    return l, ' '.join([str(i) for i in ans])

if __name__ == '__main__':
    n = int(input(''))
    A = list(map(int, input('').split()))
    for i in noincr(A):
        print(i)
 


