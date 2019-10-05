# min -куча, хранит кортеж из двух 
# объектов: (сам предмет, приоритет)
class Heap:
    def __init__(self):
        self.data = []
        self.size = 0
    
    def siftDown(self, i):
        ind_min = i
        while 2 * i + 1 < self.size:
            if self.data[2 * i + 1][1] < self.data[ind_min][1]:
                ind_min = 2 * i + 1
            if 2 * i + 2 < self.size and self.data[2 * i + 2][1] < self.data[ind_min][1]:
                ind_min = 2 * i + 2
            if ind_min != i:
                self.data[i], self.data[ind_min] = self.data[ind_min], self.data[i]
                i = ind_min
            else:
                break 

    def siftUp(self, i): 
        while i > 0 and self.data[(i - 1) // 2][1] > self.data[i][1]:
            self.data[i], self.data[(i - 1) // 2] = self.data[(i - 1) // 2], self.data[i]
            i = (i - 1) // 2
            
    def insert(self, a):
        self.data.append(a)
        self.siftUp(self.size)
        self.size += 1
    
    def extractMax(self):
        if self.size > 1:
            ans = self.data[0] 
            self.data[0] = self.data.pop()
            self.size -= 1
            self.siftDown(0)
            return ans 
        if self.size:
            self.size -= 1
            return self.data.pop()
            
    def getMax(self):
        if self.size:
            return self.data[0]
            
    def remove(self, i):
        if 0 <= i < self.size:
            self.data[i] = (self.getMax()[0], self.getMax()[1] + 1)
            self.siftUp(i)
            self.extractMax()
        
    def changePr(self, i, p):
        if 0 <= i < self.size:
            self.data[i] = (self.data[i][0], self.data[i][1] + p)
            if p > 0:
                self.siftUp(i)
            else: 
                siftDown(i)