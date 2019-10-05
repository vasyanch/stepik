def noincr(A):

    d = len(A)
    D = [1] * d
    prev = [-1] * d

    for i in range(1, d):
        for j in range(i):
            if A[i] <= A[j] and D[j] >= D[i]:
                D[i] = D[j] + 1
                prev[i] = j
    k = max(D)              # длина наиб. невозр. посл.
    j = D.index(k)           # индекс в D
    l = [0 for i in range(k)]

    for i in range(k - 1, -1, -1):
        l[i] = j + 1
        j = prev[j]

    return k, ' '.join([str(i) for i in l])
 

if __name__ == '__main__':
    n = int(input(''))
    A = list(map(int, input('').split()))
    for i in noincr(A):
        print(i)


