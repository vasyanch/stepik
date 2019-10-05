def knapsack_without_repsBU(W, lst):
    n = len(lst)
    d = [[None for _ in range(n + 1)] for _ in range(W + 1)]
    for i in range(n + 1):
        d[0][i] = 0
    for i in range(W + 1):
        d[i][0] = 0
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            d[w][i] = d[w][i - 1]
            if lst[i - 1] <= w:
                d[w][i] = max(d[w][i], d[w - lst[i - 1]][i - 1] + lst[i - 1])
    return d[W][n]


if __name__ == '__main__':
    vol, n_ = map(int, input().split())
    s = list(map(int, input().split()))
    print(knapsack_without_repsBU(vol, s))