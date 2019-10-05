def LISBottomUp(A):
    '''
         Фун. LISBottomUp(A)(Longest Increasing Subsequence)
         получает на вход массив А и находит наибольшую
         возрастающую подпоследовательсность элементов
         массив А. В ввиде результата возвращает длину
         подпосл-ти и массив L содержащий
         индексы(в массиве А) элеметов найденной
         подпосл-ти. Для восстановления
         подпосл-ти(создания массива L) используется
         массив prev, который для каждого элемента
         подпосл. хранит индекс предшествующего
         ему элемента в подпосл.. Время работы O(n^2).
    '''
    n = len(A)
    D = [0 for i in range(n)]
    prev = [-1 for i in range(n)]
    for i in range(n):
        D[i] = 1
        for j in range(i):
            if A[j] < A[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
                prev[i] = j
# D это список такой что D[i] хранит длину НВП заканчивающейся в A[i]
# prev - список такой что prev[i] хранит индекс предыдущего члена
#        подпоследовательности.
    ans = max(D)# ans - хранит длину НВП т.к. нах-ся макс. знач. в D
# Ниже описанна процедура восстановления ответа с помощью массива prev
    L = [0 for i in range(ans)]
    k = D.index(ans)
    j = ans - 1
    while k > 0:
        L[j] = k
        j -= 1
        k = prev[k]
    return ans, L


def LISBottomUp_a(A):
    '''
  Для восстановления подпосл-ти не используется массив prev.
Вместо этого используется условие
A[i] < A[k] and D[i] == D[k] - 1
однозначно определяющее след. элемент подпосл-ти.
Также массив L содержит не индесы, а элементы(из А)
подпосл-ти. ВРемя работы O(n^2).
    '''
    n = len(A)
    D = [0 for i in range(n)]
    for i in range(n):
        D[i] = 1
        for j in range(i):
            if A[j] < A[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    ans = max(D)
    L = [0 for i in range(ans)]
    k = D.index(ans)
    j = ans - 1
    L[j] = A[k]
    while k > 0:
        j -= 1
        for i in range(k - 1, -1, -1):
            if A[i] < A[k] and D[i] == D[k] - 1:
                k = i
                L[j] = A[k]
                break
    return ans, L



if __name__ == '__main__':
    print(LISBottomUp([1, 2, 3, 4, 3, 6, 1, 5, 12, 12, 23, 23]))
    print(LISBottomUp_a([1, 2, 3, 4, 3, 6, 12, 12, 23, 23]))


