class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self, a):
        if a > 0:
            super().append(a)
        else:
            raise NonPositiveError

if __name__ == "__main__":
    x = PositiveList()
    x.append(4)
    print(x)
    x.append(-4)
