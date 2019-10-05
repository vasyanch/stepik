from fractions import Fraction


def mul(b, st):
    st = [_ * b for _ in st]
    return st


def sum_(st1, st2):
    st = [st1[i] + st2[i] for i in range(len(st1))]
    return st


def det(mat, st, n):
    if st == n - 1:
        return mat[st][st]
    z = 1  # знак
    if mat[st][st] == 0:
        for q in range(st + 1, n):
            if mat[q][st] != 0:
                mat[st], mat[q] = mat[q], mat[st]
                z = - 1
                break
            if q == n - 1:
                return 0
    for s in range(st + 1, n):
        if mat[s][st] == 0:
            continue
        b = Fraction(-mat[s][st], mat[st][st])
        mat[s] = sum_(mul(b, mat[st]), mat[s])
        #  print(mat)
    return z * mat[st][st] * det(mat, st + 1, n)


if __name__ == '__main__':
    n = int(input())
    matrix = [0] * n
    for _ in range(n):
        matrix[_] = list(map(int, input().split()))
    print(int(det(matrix, 0, n)))
