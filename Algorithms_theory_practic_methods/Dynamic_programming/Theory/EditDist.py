# Вычислите расстояние редактирования двух данных непустых строк длины не
# более 10^2, содержащих строчные буквы латинского алфавита.
# Рекурсивное решение.


def edit_dist(i, j):
    if D[i][j] == float('inf'):
        if i == 0:
            D[i][j] = j
        elif j == 0:
            D[i][j] = i
        else:
            ins = edit_dist(i, j - 1) + 1
            del_ = edit_dist(i - 1, j) + 1
            sub = edit_dist(i - 1, j - 1) + int((lambda x, y: not(x == y))(a[i - 1], b[j - 1]))
            D[i][j] = min(ins, del_, sub)
        return D[i][j]
    else:
        return D[i][j]


if __name__ == '__main__':
    a = input()
    b = input()
    n = len(a)
    m = len(b)
    D = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
    print(edit_dist(n, m))
