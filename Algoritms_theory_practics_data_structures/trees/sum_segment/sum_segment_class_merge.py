# operation Splay() https://habr.com/company/compscicenter/blog/210296/
class Node:
    def __init__(self, key, parent=-1, left=-1, right=-1):
        self.key = self.sum = key
        self.parent = parent
        self.left = left
        self.right = right


class SplayTree:
    def __init__(self, root=None):
        self.root = root

    def search(self, key, flag=True):
        if self.root is not None:
            i = self.root
            j = i
            while i != -1:
                if i.key == key:
                    j = i
                    break
                if i.key > key:
                    j = i
                    i = i.left
                else:
                    j = i
                    i = i.right
            if flag:
                self.splay(j)
            return j

    def update_sum(self, g, add):
        while g.parent != -1:
            g.sum += add
            g = g.parent
        g.sum += add

    def insert(self, key):
        k = self.search(key, False)
        if k is None:
            self.root = Node(key)
        else:
            if k.key == key:
                return None
            if k.key > key:
                k.left = Node(key, k)
                self.update_sum(k, key)
                self.splay(k.left)
            else:
                k.right = Node(key, k)
                self.update_sum(k, key)
                self.splay(k.right)

    def remove(self, key):
        k = self.search(key)
        if k is not None:
            if k.key != key:
                return None
            else:
                if self.root.left == -1 and self.root.right == -1:
                    self.root = None
                elif self.root.left == -1 and self.root.right != -1:
                    self.root = self.root.right
                    self.root.parent = -1
                elif self.root.left != -1 and self.root.right == -1:
                    self.root = self.root.left
                    self.root.parent = -1
                else:
                    self.root.right.parent = -1
                    t2 = SplayTree(self.root.right)
                    self.root = self.root.left
                    self.root.parent = -1
                    self.merge(t2)

    def max_el(self, node):
        if node is not None:
            while node.right != -1:
                node = node.right
        return node

    def min_el(self, node):
        if node is not None:
            while node.left != -1:
                node = node.left
        return node

    def next_el(self, key):
        a = None
        i = self.search(key)
        if i is None or i.key != key:
            return None
        if i.right != -1:
            a = self.min_el(i.right).key
        else:
            par = i.parent
            while par != -1 and par.right != -1 and par.right == i:
                i = par
                par = i.parent
            if par != -1:
                a = par.key
        return a

    def merge(self, t2):
        if self.root is not None and t2.root is not None:
            if self.max_el(self.root).key < t2.min_el(t2.root).key:
                new_root = self.max_el(self.root)
                self.splay(new_root)
                self.root.right, t2.root.parent = t2.root, self.root
                self.root.sum += t2.root.sum
            if self.min_el(self.root).key > t2.max_el(t2.root).key:
                new_root = t2.max_el(t2.root)
                t2.splay(new_root)
                t2.root.right, self.root.parent = self.root, t2.root
                t2.root.sum += self.root.sum
                self.root = t2.root

    def rotate(self, node):
        parent = node.parent
        grandparent = parent.parent
        if grandparent == -1:
            self.root = node
        else:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node
        node.parent = grandparent
        parent.sum -= node.sum
        if parent.left == node:
            if node.right != -1:
                parent.sum += node.right.sum
                node.sum -= node.right.sum
                node.right.parent = parent
            node.right, parent.parent, parent.left = parent, node, node.right
        else:
            if node.left != -1:
                parent.sum += node.left.sum
                node.sum -= node.left.sum
                node.left.parent = parent
            node.left, parent.parent, parent.right = parent, node, node.left
        node.sum += parent.sum

    def splay(self, node):
        while node.parent != -1:
            parent = node.parent
            grandparent = parent.parent
            if grandparent == -1:
                self.rotate(node)
            else:
                zig_zig = (grandparent.left == parent) == (parent.left == node)
                if zig_zig:
                    self.rotate(parent)
                    self.rotate(node)
                else:
                    self.rotate(node)
                    self.rotate(node)


if __name__ == '__main__':
    m = int(input())
    tree = SplayTree()
    s = 0
    for x in range(m):
        query = input().split()
        l = (int(query[1]) + s) % 1000000001
        if query[0] == '+':
            tree.insert(l)
        elif query[0] == '-':
            tree.remove(l)
        elif query[0] == '?':
            ans = tree.search(l)
            if ans is not None and ans.key == l:
                print('Found')
            else:
                print('Not found')
        else:
            r = (int(query[2]) + s) % 1000000001
            if tree.search(l) is not None:
                if l > tree.max_el(tree.root).key or tree.min_el(tree.root).key > r:
                    s = 0
                else:
                    s = tree.root.sum
                    if tree.root.left != -1:
                        s -= tree.root.left.sum
                    if l > tree.root.key:
                        s -= tree.root.key
                    tree.search(r)
                    if tree.root.right != -1:
                        s -= tree.root.right.sum
                    if r < tree.root.key:
                        s -= tree.root.key
            else:
                s = 0
            print(s)
