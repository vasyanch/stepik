def LMSBottomUp(A):
    '''
        Данная фун. возвращает длину максимальной
        последовательнократной подпосл-ти посл-ти из списка A.
        Более детально смотри файл LIS.
    '''
    n = len(A)
    D = [0 for i in range(n)]
    for i in range(n):
        D[i] = 1
        for j in range(i):
            if A[i] % A[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    return max(D)


if __name__ == '__main__':
    n = int(input(''))
    A = list(map(int, input('').split()))
    print(LMSBottomUp(A))