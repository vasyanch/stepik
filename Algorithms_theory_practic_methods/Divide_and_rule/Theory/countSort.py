'''
    Алгоритм сортировки подсчетом. Время раблты O(n+m),
    где n это длина массива, а m это количество различных элементов
    во входном массиве(длина диапозона в переделах которого лежат
    все значения во входном массиве).
    Зад.:
     Первая строка содержит число 1 ≤ n ≤ 10*4, вторая — n натуральных
     чисел, не превышающих 10. Выведите упорядоченную по неубыванию
     последовательность этих чисел.
'''

def countSort(lst, m):
    n = len(lst)
    b = [0 for i in range(m)]
    ans = [0 for i in range(n)]
    for i in lst:
        b[i] = b[i] + 1
    print(b)
    for j in range(1, m):
        b[j] += b[j-1]
    print(b)
    for i in range(n-1, -1, -1):
        ans[b[lst[i]] - 1] = lst[i]
        b[lst[i]] -= 1
    return ans 


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    print(' '.join(str(i) for i in countSort(lst, 11)))

if __name__ == '__main__':
    main()
        
