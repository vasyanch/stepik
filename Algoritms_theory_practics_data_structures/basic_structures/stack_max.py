class Stack:
    def __init__(self):
        self.data = []
        self.m = []

    def push(self, a):
        if self.data:
            self.data.append(a)
            c = self.m[-1]
            if c < a:
                self.m.append(a)
            else:
                self.m.append(c)
        else:
            self.data.append(a)
            self.m.append(a)

    def pop(self):
        self.m.pop()
        return self.data.pop()

    def empty(self):
        return not bool(len(self.data))

    def top(self):
        if len(self.data):
            return self.data[-1]
        else:
            return None

    def get_max(self):
        if self.m:
            return self.m[-1]


if __name__ == '__main__':
    s = Stack()
    ans = []
    for i in range(int(input())):
        z = input()
        if 'pop' == z:
            s.pop()
        elif 'max' == z:
            ans.append(s.get_max())
        else:
            s.push(int(z.split()[1]))
    # print(ans)
    [print(i) for i in ans]




