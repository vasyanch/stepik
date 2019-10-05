from random import random 
class MyList():
    def __iter__(self):
        return self
    def __init__(self, k):
        self.k = k
        self.i = 0
    def __next__(self):
        if self.i < len(self.k):
            self.i += 2
            return self.k[self.i - 2], self.k[self.i-1]
        else:
            raise StopIteration

exp = MyList([1, 2, 3, 4])

def generator(k):
    for i in range(k):
        yield random()
gen = generator(3)


