class HashTable:

    def __init__(self, m):
        self.data = [[] for _ in range(m)]
        self.m = m

    def hash_fun(self, s, x, p):
        h = 0
        for j, v in enumerate(s):
            h = (h + (ord(v) * (x ** j))) % p
        return h % self.m

    def add(self, s):
        hs = self.hash_fun(s, 263, 1000000007)
        if s in self.data[hs]:
            return
        else:
            self.data[hs].insert(0, s)

    def remove(self, s):
        hs = self.hash_fun(s, 263, 1000000007)
        if s in self.data[hs]:
            self.data[hs].remove(s)

    def find(self, s):
        hs = self.hash_fun(s, 263, 1000000007)
        if s in self.data[hs]:
            return 'yes'
        else:
            return 'no'

    def check(self, i):
        if self.data[i]:
            for j in self.data[i]:
                print(j, end=' ')
        else:
            print()


if __name__ == '__main__':
    m_ = int(input())
    table = HashTable(m_)
    for _ in range(int(input())):
        cur = input().split()
        if cur[0] == 'add':
            table.add(cur[1])
        elif cur[0] == 'del':
            table.remove(cur[1])
        elif cur[0] == 'find':
            print(table.find(cur[1]))
        elif cur[0] == 'check':
            table.check(int(cur[1]))
