# попробовать переписать еще короче с помощью цикла for
# то есть за один проход по списку пакетов, асимптотика будет таже


class Queue:
    def __init__(self, size):
        self.data = [None] * size
        self.start = 0
        self.end = 0
        self.num = 0
        self.size = size

    def push_back(self, a):
        if self.num < self.size:
            self.data[self.end] = a
            self.end = (self.end + 1) % self.size
            self.num += 1

    def pop_front(self):
        if self.num > 0:
            ans = self.data[self.start]
            self.start = (self.start + 1) % self.size
            self.num -= 1
            return ans

    def empty(self):
        return self.num


def do(p, size, n):
    q = Queue(size)
    ans = [None] * n
    ch = 0  # время окончания обработки k - го пакета
    k = 0
    while k < n:
        if q.empty() < size:
            if ch < p[k][0]:
                ch = p[k][0] + p[k][1]
            else:
                ch = ch + p[k][1]
            q.push_back(ch)
            ans[k] = ch - p[k][1]
            k += 1
        else:
            z = q.pop_front()
            while k < n and z > p[k][0]:
                ans[k] = -1
                k += 1
    return ans


if __name__ == '__main__':
    size_, n_ = list(map(int, input().split()))
    packages = [tuple(map(int, input().split())) for x in range(n_)]
    if packages:
        for i in do(packages, size_, n_):
            print(i)
