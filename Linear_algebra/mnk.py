from fractions import Fraction


def mul(b, st):
    st = [_ * b for _ in st]
    return st


def sum_(st1, st2):
    st = [st1[i] + st2[i] for i in range(len(st1))]
    return st


def gauss(mat, n_, m_):
    for c in range(n_):
        # print(mat[c])
        if c < m_ and mat[c][c] == 0:
            z = c
            for z in range(c + 1, n_):
                if mat[z][c] != 0:
                    mat[c], mat[z] = mat[z], mat[c]
                    z = -1
                    break
            if z == n_ - 1:
                continue
        for s in range(c + 1, n_):
            if c < m_:
                if mat[s][c] == 0:
                    continue
                b = Fraction(-mat[s][c], mat[c][c])
                mat[s] = sum_(mul(b, mat[c]), mat[s])

    ans = [1] * m_
    for t in range(m_ - 1, -1, -1):
        # print(t)
        v = mat[t][m_]
        for h in range(t + 1, m_):
            v = v - (mat[t][h] * ans[h])
        ans[t] = Fraction(v, mat[t][t])
    return ' '.join([str(float(i)) for i in ans])


def mnk_mat(matrix_, n, m):
    ans = [0]*m
    for w in range(m):
        line = [0]*(m + 1)
        for p in range(m+1):
            el = 0
            for _ in range(n):
                el += matrix_[_][p] * matrix_[_][w]
            line[p] = el
        ans[w] = line
    return ans, m, m


if __name__ == '__main__':
    n, m = map(int, input().split())  # n - кол-во уравнений, m - кол-во переменных
    matrix = []
    for j in range(n):
        matrix.append(list(map(Fraction, input().split())))
    sas = mnk_mat(matrix, n, m)
    print(gauss(*sas))