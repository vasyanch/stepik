'''
    Очередь с приоритетами. Написанно на базе массива. Полное двоичное max-дерево.
    Скорость выполнения всех операций O(log(n)).

        Первая строка входа содержит число операций 1 ≤ n ≤ 10^5. Каждая из
        последующих n строк задает операцию одного из следующих двух типов:
            Insert x, где 0 ≤ x ≤ 10^9 — целое число;
            ExtractMax.
        Первая операция добавляет число x в очередь с приоритетами,
        вторая — извлекает максимальное число и выводит его.
'''


class MyHeap:
    def __init__(self, data=['heap']):
        self.data = data
        self.len_ = 1

    def extract_max(self):
        if self.len_ > 2:
            ans = self.data[1]
            self.data[1] = self.data.pop(-1)
            self.len_ -= 1
            self.siftdown(1)
        else:
            ans = self.data.pop(1)
            self.len_ -=1
        return ans

    def insert(self, x):
        self.len_ += 1
        self.data.append(x)
        self.siftup(self.len_ - 1)

    def siftup(self, i):
        while 1 < i and self.data[i] > self.data[i // 2]:
            self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
            i //= 2
        return None

    def siftdown(self, j):
        while 2*j < self.len_:
            k = j
            if self.data[j] < self.data[2 * j]:
                k = 2 * j
            if 2 * j + 1 < self.len_ and self.data[2*j+1] > self.data[k]:
                k = 2 * j + 1
            if k == j:
                break
            else:
                self.data[j], self.data[k] = self.data[k], self.data[j]
                j = k
        return None


def main():
    heap = MyHeap()
    for i in range(int(input(''))):
        s = input('').strip()
        if s == 'ExtractMax':  # операция которую необходимо выполнить
            print(heap.extract_max())
        else:
            s = s.split(' ')
            heap.insert(int(s[1]))

if __name__ == '__main__':
    main()