# time limit exceeded, no accept for time
class Node:
    def __init__(self, key, parent=-1, left=-1, right=-1):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def in_order(root):
    if root.left != -1:
        in_order(root.left)
    print(root.key)
    if root.right != -1:
        in_order(root.right)


class SplayTree:
    def __init__(self, root=None):
        self.root = root

    def search(self, key, flag=True):
        if self.root is not None:
            i = self.root
            j = i
            while i != -1:
                if i.key == key:
                    return i
                if i.key > key:
                    j = i
                    i = i.left
                else:
                    j = i
                    i = i.right
            if flag:
                self.splay(j)
            return j

    def insert(self, key):
        k = self.search(key, False)
        if k is None:
            self.root = Node(key)
        else:
            if k.key == key:
                return None
            if k.key > key:
                k.left = Node(key, k)
                self.splay(k.left)
            else:
                k.right = Node(key, k)
                self.splay(k.right)

    def remove(self, key):
        k = self.search(key)
        if k is not None:
            if k.key != key:
                return None
            if k.left != -1 or k.right != -1:
                if k.left != -1 and k.right != -1:
                    var = self.max_el(k.left)
                    k.key, var.key = var.key, k.key
                    par = var.parent
                    son = var.left
                    if par.key == k.key:
                        par.left = son
                    else:
                        par.right = son
                    if son != -1:
                        son.parent = par
                else:
                    if k.left == -1:
                        son = k.right
                    else:
                        son = k.left
                    par = k.parent
                    if par != -1:
                        son.parent = par
                        if k.key < par.key:
                            par.left = son
                        else:
                            par.right = son
                    else:
                        son.parent = -1
                        self.root = son
            else:
                par = k.parent
                if par != -1:
                    if par.key > k.key:
                        par.left = -1
                    else:
                        par.right = -1
                else:
                    self.root = None

    def max_el(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            while node.right != -1:
                node = node.right
        return node

    def min_el(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            while node.left != -1:
                node = node.left
        return node

    def next_el(self, key):
        ans = None
        i = self.search(key)
        if i is None or i.key != key:
            return None
        if i.right != -1:
            ans = self.min_el(i.right).key
        else:
            par = i.parent
            while par != -1 and par.right != -1 and par.right == i:
                i = par
                par = i.parent
            if par != -1:
                ans = par.key
        return ans

    def zig(self, node):
        self.root = node
        par = node.parent
        par.parent, par.left = node, node.right
        node.parent, node.right = -1, par

    def zag(self, node):
        self.root = node
        par = node.parent
        par.parent, par.right = node, node.right
        node.parent, node.left = -1, par

    def zigzig(self, node):
        par = node.parent
        grandpa = par.parent
        new_par = grandpa.parent
        grandpa.parent, grandpa.left = par, par.right
        par.parent, par.left, par.right = node, node.right, grandpa
        node.parent, node.right = new_par, par
        if new_par != -1:
            if new_par.key > node.key:
                new_par.left = node
            else:
                new_par.right = node
        else:
            self.root = node

    def zigzag(self, node):
        par = node.parent
        grandpa = par.parent
        new_par = grandpa.parent
        grandpa.parent, grandpa.right = node, node.left
        par.parent, par.left = node, node.right
        node.parent, node.left, node.right = new_par, grandpa, par
        if new_par != -1:
            if new_par.key > node.key:
                new_par.left = node
            else:
                new_par.right = node
        else:
            self.root = node

    def zagzig(self, node):
        par = node.parent
        grandpa = par.parent
        new_par = grandpa.parent
        grandpa.parent, grandpa.left = node, node.right
        par.parent, par.right = node, node.left
        node.parent, node.left, node.right = new_par, par, grandpa
        if new_par != -1:
            if new_par.key > node.key:
                new_par.left = node
            else:
                new_par.right = node
        else:
            self.root = node

    def zagzag(self, node):
        par = node.parent
        grandpa = par.parent
        new_par = grandpa.parent
        grandpa.parent, grandpa.right = par, par.left
        par.parent, par.left, par.right = node, grandpa, node.left
        node.parent, node.left = new_par, par
        if new_par != -1:
            if new_par.key > node.key:
                new_par.left = node
            else:
                new_par.right = node
        else:
            self.root = node

    def splay(self, node):
        while node.parent != -1:
            par = node.parent
            if par.left != -1 and par.left.key == node.key:  # node - left son
                if par.parent == -1:
                    self.zig(node)
                else:
                    if par.parent.left != -1 and par.parent.left.key == par.key:
                        self.zigzig(node)
                    else:
                        self.zigzag(node)
            else:  # node - right son
                if par.parent == -1:
                    self.zag(node)
                else:
                    if par.parent.left != -1 and par.parent.left.key == par.key:
                        self.zagzig(node)
                    else:
                        self.zagzag(node)
        

if __name__ == '__main__':
    m = int(input())
    tree = SplayTree()
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
            if tree.search(y) is not None and tree.search(y).key == y:
                print('Found')
            else:
                print('Not found')
        else:
            l = (int(query[1]) + s) % 1000000001
            r = (int(query[2]) + s) % 1000000001
            if tree.search(l) is not None:
                st = tree.search(l).key
                while st is not None and st < l:
                    st = tree.next_el(st)
                if st is None:
                    s = 0
                else:
                    if st <= r:
                        s = st
                        nx = tree.next_el(st)
                        while nx is not None and nx <= r:
                            s += nx
                            nx = tree.next_el(nx)
                    else:
                        s = 0
            else:
                s = 0
            print(s)
