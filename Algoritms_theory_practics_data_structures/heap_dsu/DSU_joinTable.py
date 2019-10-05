# Струкура данных - система непересекающихся множеств на основе массива.
# Использованы эвристики сжатия пути и объединения по рангу


class DSU:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # ранк - это глубина дерева

    def make_set(self):
        self.parent.append(len(self.parent))
        self.rank.append(0)

    def find_set(self, v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.rank[a] < self.rank[b]:
                a, b = b, a
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1


if __name__ == '__main__':
    n_, m = map(int, input().split())
    sizes = [None] * n_
    dsu = DSU(n_)
    mx = 0
    for i, q in enumerate(map(int, input().split())):
        sizes[i] = q
        mx = max(q, mx)
    for j in range(m):
        # print(j)
        des_, sour_ = map(int, input().split())
        des = dsu.find_set(des_ - 1)
        sour = dsu.find_set(sour_ - 1)
        if des != sour:
            sz = sizes[dsu.find_set(des)]+ sizes[dsu.find_set(sour)]
            dsu.union_sets(des, sour)
            sizes[dsu.find_set(des)] = sz
            mx = max(mx, sizes[dsu.find_set(des)])
        print(mx)