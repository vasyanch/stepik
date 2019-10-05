class multifilter:
    def judge_half(pos, neg):
        return pos >= neg
    def judge_any(pos, neg):
        return pos >=1
    def judge_all(pos, neg):
        return neg == 0
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.it = iterable
        self.fun = funcs
        self.jud = judge
    def __iter__(self):
            for i in self.it:
                pos = 0
                neg = len(self.fun)
                for func in self.fun:
                    if func(i):
                        pos += 1
                        neg -= 1    
                if self.jud(pos, neg):
                    yield i

