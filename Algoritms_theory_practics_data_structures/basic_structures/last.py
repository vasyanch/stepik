'''
    Максимум в склоьзящем окне
    Очередь реализована с помощью двух стеков
    с поддержкой максимума. Время работы O(n).
    Нативный алгоритм дает оценку O(n*m), где
    n - размер массива, а m - размер окна.
'''


class Stack:
    def __init__(self):
        self.data = []
        self.m = []

    def push(self, a):
        self.data.append(a)
        if self.m:
            self.m.append(max(a, self.m[-1]))
        else:
            self.m.append(a)

    def pop(self):
        if self.data:
            self.m.pop()
            return self.data.pop()

    def empty(self):
        return not bool(self.data)

    def get_max(self):
        if self.m:
            return self.m[-1]


class Queue:
    def __init__(self, size):
        self.come = Stack()
        self.out = Stack()
        self.num = 0
        self.size = size

    def push_back(self, a):
        if self.num < self.size:
            self.come.push(a)
            self.num += 1

    def pop_front(self):
        if self.out.empty():
            while not self.come.empty():
                self.out.push(self.come.pop())
            if not self.out.empty():
                self.num -= 1
                return self.out.pop()
        else:
            self.num -= 1
            return self.out.pop()

    def empty(self):
        return self.come.empty() and self.out.empty()

    def max_(self):
        if self.come.data and self.out.data:
            return max(self.come.get_max(), self.out.get_max())
        if self.out.data:
            return self.out.get_max()
        if self.come.data:
            return self.come.get_max()


def petr(mas, m, n):
    q = Queue(m)
    ans = [None] * (n - m + 1)
    for l in range(m):
        q.push_back(mas[l])
    ans[0] = q.max_()
    for j in range(m, n):
        q.pop_front()
        q.push_back(mas[j])
        ans[j - (m - 1)] = q.max_()
    return ans


if __name__ == '__main__':
    n_ = int(input())
    mas_ = list(map(int, input().split()))
    m_ = int(input())
    [print(i, end=' ') for i in petr(mas_, m_, n_)]