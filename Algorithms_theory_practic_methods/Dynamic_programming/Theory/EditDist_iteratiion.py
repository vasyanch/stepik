# Вычислите расстояние редактирования двух данных непустых строк длины не
# более 10^2, содержащих строчные буквы латинского алфавита.
# Итеративное решение.


def edit_dist(c, k):
    n, m = len(c), len(k)
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for _ in range(m+1):
        d[0][_] = _
    for _ in range(n+1):
        d[_][0] = _
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            ins = d[i][j - 1] + 1
            del_ = d[i - 1][j] + 1
            sub = d[i - 1][j - 1] + int((lambda x, y: not (x == y))(c[i - 1], k[j - 1]))
            d[i][j] = min(ins, del_, sub)
    return d[n][m]


if __name__ == '__main__':
    a = input()
    b = input()
    print(edit_dist(a, b))
