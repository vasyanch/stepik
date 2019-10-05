class Stack:
    def __init__(self):
        self.data = []

    def push(self, a):
        self.data.append(a)

    def pop(self):
        return self.data.pop()

    def empty(self):
        return not bool(len(self.data))

    def top(self):
        if len(self.data):
            return self.data[-1]
        else:
            return None


def brackets(_string):
    a = Stack()
    ind = []
    for i, v in enumerate(_string):
        if v in('(', '{', '['):
            a.push(v)
            ind.append(i + 1)
        elif v in (')', '}', ']'):
            if a.empty():
                return i + 1
            b = a.top()
            if b + v == '()'or b + v == '[]' or b + v == '{}':
                a.pop()
                ind.pop()
            else:
                return i + 1
    if a.empty():
        return 'Success'
    else:
        return ind[-1]


if __name__ == '__main__':
    s = input()
    print(brackets(s))