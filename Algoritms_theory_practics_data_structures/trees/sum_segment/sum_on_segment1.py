# tree.data = [(key, parent, left, right)]
from collections import namedtuple
Node = namedtuple('Node', 'key parent left right')


class SearchTree:

    def __init__(self, n):
        self.data = [None for _ in range(n)]
        self.max_size = n
        self.stack = [j for j in range(n - 1, -1, -1)]  # хранит свободные места в списке верщин self.data
        self.root = -1

    def search(self, key):
        '''

        :param key:
        :return: if key in tree return index key, else return
        index node which become parent for this key in case run
        tree.insert(key)

        '''
        if len(self.stack) < self.max_size:
            i = self.root
            j = i
            while i > -1:
                if self.data[i].key == key:
                    return i
                if self.data[i].key > key:
                    j = i
                    i = self.data[i].left
                else:
                    j = i
                    i = self.data[i].right
            return j

    def insert(self, key):
        if self.stack:
            k = self.search(key)
            if k is None:
                self.root = self.stack.pop()
                self.data[self.root] = Node(key, -1, -1, -1)
                return None
            if self.data[k].key == key:
                return None
            vak = self.stack.pop()
            if self.data[k].key <= key:
                self.data[vak] = Node(key, k, -1, -1)
                self.data[k] = Node(self.data[k].key, self.data[k].parent, self.data[k].left, vak)
            else:
                self.data[vak] = Node(key, k, -1, -1)
                self.data[k] = Node(self.data[k].key, self.data[k].parent, vak, self.data[k].right)

    def remove(self, key):
        k = self.search(key)
        if k is not None:
            if self.data[k].key != key:
                return None
            if self.data[k].left != -1 or self.data[k].right != -1:
                if self.data[k].left != -1 and self.data[k].right != -1:
                    var = self.max_el(self.data[k].left)
                    self.data[var], self.data[k] = Node(self.data[k].key, self.data[var].parent,
                                                        self.data[var].left, self.data[var].right), \
                            Node(self.data[var].key, self.data[k].parent, self.data[k].left, self.data[k].right)
                    par = self.data[var].parent
                    son = self.data[var].left
                    if par != k:
                        if son != -1:
                            self.data[par] = Node(self.data[par].key, self.data[par].parent, self.data[par].left, son)
                            self.data[son] = Node(self.data[son].key, par, self.data[son].left, self.data[son].right)
                        else:
                            self.data[par] = Node(self.data[par].key, self.data[par].parent, self.data[par].left, -1)
                    else:
                        if son != -1:
                            self.data[par] = Node(self.data[par].key, self.data[par].parent, son, self.data[par].right)
                            self.data[son] = Node(self.data[son].key, par, self.data[son].left, self.data[son].right)
                        else:
                            self.data[par] = Node(self.data[par].key, self.data[par].parent, -1, self.data[par].right)
                    k = var
                else:
                    son = max(self.data[k].left, self.data[k].right)
                    par = self.data[k].parent
                    if par != -1:
                        self.data[son] = Node(self.data[son].key, par, self.data[son].left, self.data[son].right)
                        if self.data[son].key < self.data[par].key:
                            self.data[par] = Node(self.data[par].key, self.data[par].parent, son, self.data[par].right)
                        else:
                            self.data[par] = Node(self.data[par].key, self.data[par].parent, self.data[par].left, son)
                    else:
                        self.data[son] = Node(self.data[son].key, -1, self.data[son].left, self.data[son].right)
                        self.root = son
            else:
                par = self.data[k].parent
                if par != -1:
                    if self.data[par].key > self.data[k].key:
                        self.data[par] = Node(self.data[par].key, self.data[par].parent, -1, self.data[par].right)
                    else:
                        self.data[par] = Node(self.data[par].key, self.data[par].parent, self.data[par].left, -1)
            self.data[k] = None
            self.stack.append(k)

    def max_el(self, i=None):
        if i is None:
            i = self.root
        if self.data[i] is not None:
            while self.data[i].right != -1:
                i = self.data[i].right
        return i

    def min_el(self, i=None):
        if i is None:
            i = self.root
        if self.data[i] is not None:
            while self.data[i].left != -1:
                i = self.data[i].left
        return i

    def next(self, key):
        ans = None
        i = self.search(key)
        if i is None or self.data[i].key != key:
            return ans
        if self.data[i].right != -1:
            ans = self.data[self.min_el(self.data[i].right)].key
        else:
            if self.data[i].parent != -1:
                par = self.data[i].parent
                while par != -1 and self.data[par].right == i:
                    i = par
                    par = self.data[i].parent
                if par != -1:
                    ans = self.data[par].key
        return ans


if __name__ == '__main__':
    m = int(input())
    tree = SearchTree(m)
    s = 0 
    for x in range(m):
        query = input().split()
        if query[0] == '+':
            y = (int(query[1]) + s) % 1000000001 
            tree.insert(y)
        elif query[0] == '-':
            y = (int(query[1]) + s) % 1000000001
            tree.remove(y)
        elif query[0] == '?':
            y = (int(query[1]) + s) % 1000000001
            if tree.search(y) is not None and tree.data[tree.search(y)].key == y:
                print('Found')
            else:
                print('Not found')
        else:
            l = (int(query[1]) + s) % 1000000001
            r = (int(query[2]) + s) % 1000000001
            if tree.search(l) is not None:
                st = tree.data[tree.search(l)].key
                while st is not None and st < l:
                    st = tree.next(st)
                if st is None:
                    s = 0
                else:
                    if st <= r:
                        s = st
                        nx = tree.next(st)
                        while nx is not None and nx <= r:
                            s += nx
                            nx = tree.next(nx)
                    else:
                        s = 0
            else:
                s = 0
            print(s)
