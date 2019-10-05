#-*-coding:utf8;-*-
#qpy:3
#qpy:console
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


def do(size, n):
    q = Queue(size)
    for i in range(n):
        arr, dur = map(int, input().split())
        while q.empty() and arr >= q.data[q.start]:
            q.pop_front()
        if q.empty() < size:
            if not q.empty():
                ch =arr  # принимает значение времени начала обработки данного пакета
            print(ch)
            ch = ch + dur
            q.push_back(ch)
        else:
            print(-1)


if __name__ == '__main__':
    size_, n_ = list(map(int, input().split()))
    # packages = [tuple(map(int, input().split())) for x in range(n_)]
    do(size_, n_)