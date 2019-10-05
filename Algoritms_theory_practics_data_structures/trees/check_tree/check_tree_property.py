'''
не проходит по времени так как каждая вершина проверяется
поиском что приводит к асимптотике O(n*log(n))
'''


class search_Tree:
    def __init__(self, n):
        self.data = [None for i in range(n)]
        self.max_size = n
        self.size = 0

    def search(self, key):
        '''
        :param key:
        :return: if key in tree return index key, else return index node which become parent for this key in case run
        tree.insert(key)
        '''
        if self.size != 0:
            i = 0
            j = 0
            while i > -1:
                if self.data[i][0] == key:
                    return i
                elif self.data[i][0] > key:
                    if self.data[i][1] != -1:
                        j = i
                        i = self.data[i][1]
                    else:
                        j = i
                        i = -1
                else:
                    if self.data[i][2] != -1:
                        j = i
                        i = self.data[i][2]
                    else:
                        j = i
                        i = -1
            return j

    def insert(self, key):
        if self.size == 0:
            self.data[0][0] = key
            self.size += 1
        else:
            k = self.search(key)
            if self.data[k][0] == key:
                return None
            if self.data[k][0] < key:
                self.data[self.size][0] = key
                self.data[k][2] = self.size
                #self.data[self.size][1] = k
                self.size += 1
            else:
                self.data[self.size][0] = key
                self.data[k][1] = self.size
                #self.data[self.size][1] = k
                self.size += 1


if __name__ == '__main__':
    n = int(input())
    tree = search_Tree(n)
    ans = 'CORRECT'
    for j in range(n):
        h = tuple(map(int, input().split()))
        tree.data[j] = h
        #v[0], v[2], v[3] = h[0], h[1], h[2]
        tree.size += 1
        '''if h[1] != -1:
            tree.data[h[1]][1] = j
        if h[2] != -1:
            tree.data[h[2]][1] = j'''
        try:
            if not (tree.search(h[0]) == j):
                #print(tree.search(v[0]))
                ans = 'INCORRECT'
                break
        except TypeError:
            ans = 'INCORRECT'
            break
    print(ans)
    #print(tree.data)
