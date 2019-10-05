# min -куча, хранит кортеж из двух 
# объектов: (сам предмет, приоритет)


class Heap:
    def __init__(self, max_size):
        self.data = [None] * max_size
        self.size = 0
     
    def siftDown(self, i):
        ind_min = i
        while 2 * i + 1 < self.size:
            if self.data[2 * i + 1] < self.data[ind_min]:
                ind_min = 2 * i + 1
            if 2 * i + 2 < self.size and self.data[2 * i + 2] < self.data[ind_min]:
                ind_min = 2 * i + 2
            if ind_min != i:
                self.data[i], self.data[ind_min] = self.data[ind_min], self.data[i]
                i = ind_min
            else:
                break
 
    def siftUp(self, i): 
        while i > 0 and self.data[(i - 1) // 2] > self.data[i]:
            self.data[i], self.data[(i - 1) // 2] = self.data[(i - 1) // 2], self.data[i]
            i = (i - 1) // 2
             
    def insert(self, a):
        self.data[self.size] = a
        self.siftUp(self.size)
        self.size += 1
     
    def extractMax(self):
        if self.size:
            ans = self.data[0] 
            self.data[0] = self.data[self.size - 1]
            self.size -= 1
            self.siftDown(0)
            return ans
             
    def getMax(self):
        if self.size:
            return self.data[0]
             
    def remove(self, i):
        if 0 <= i < self.size:
            self.data[i] = (self.getMax()[0] + 1, self.data[i][1])
            self.siftUp(i)
            self.extractMax()
         
    def changePr(self, i, p):
        if 0 <= i < self.size:
            self.data[i] = (self.data[i][0] + p, self.data[i][1])
            if p < 0:
                self.siftUp(i)
            else: 
                self.siftDown(i)


def process(n):
    buffer = Heap(n)
    for j in range(n):
        buffer.insert((0, j))
    for i in map(int, input().split()):
        current = buffer.getMax()
        print(current[1], current[0])
        buffer.changePr(0, i)

if __name__ == '__main__':
    n_, m_ = map(int, input().split())
    process(n_)
