from fractions import Fraction


def mul(b, st):
    st = [_ * b for _ in st]
    return st


def sum_(st1, st2):
    st = [st1[i] + st2[i] for i in range(len(st1))]
    return st


def gauss(mat, n_, m_):
    for c in range(min(n_, m_)):
        if mat[c][c] == 0:
            for z in range(c + 1, n_):
                if mat[z][c] != 0:
                    mat[c], mat[z] = mat[z], mat[c]
                    z = -1
                    break
            if z == n_ - 1:
                continue
        for s in range(c + 1, n_):
            if mat[s][c] == 0:
                continue
            b = Fraction(-mat[s][c], mat[c][c])
            mat[s] = sum_(mul(b, mat[c]), mat[s])
    # print(mat)
    # print(n_)
    for k in range(n_ - 1, -1, -1):
        for g in range(0, m_ + 1):
            if mat[k][g] != 0.0:
                # print(k, g)
                q = k
                if g == m_:
                    return 'NO'
                break
        if mat[k][g] == 0:
            continue
        else:
            break
    # print(q)
    if q < m_ - 1:
        return 'INF'
    else:
        ans = [1] * m_
        for t in range(m_ - 1, -1, -1):
            # print(t)
            v = mat[t][m_]
            for h in range(t + 1, m_):
                v = v - (mat[t][h] * ans[h])
            ans[t] = Fraction(v, mat[t][t])
        return 'YES\n' + ' '.join([str(float(i)) for i in ans])


if __name__ == '__main__':
    n, m = map(int, input().split())  # n - кол-во уравнений, m - кол-во переменных
    matrix = []
    for j in range(n):
        matrix.append(list(map(Fraction, input().split())))
    print(gauss(matrix, n, m))
