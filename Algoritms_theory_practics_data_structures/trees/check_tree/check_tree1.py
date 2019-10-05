# асимптотика O(log(n))
# обе функции работают, для каждой нужно корректировать вывод
from collections import namedtuple
import sys
sys.setrecursionlimit(15000)


def correct(tree, i=0, c=True):
    mi = tree[i].key  # min in current undertree
    ma = tree[i].key  # max in current undertree
    if tree[i].left != -1:
        cur_mi, cur_ma, c = correct(tree, tree[i].left, c)
        if not c:
            return mi, ma, False
        if tree[i].key < cur_ma:
            return mi, ma, False
        mi = cur_mi
        # ma = max(ma, cur_ma)
    if tree[i].right != -1:
        cur_mi, cur_ma, c = correct(tree, tree[i].right, c)
        if not c:
            return mi, ma, False
        if tree[i].key > cur_mi:
            return mi, ma, False
        ma = cur_ma
    return mi, ma, c


def another_correct(tree, node=0, stack=[], cur=None):
    if tree[node].left != -1:
        stack.append(node)
        if cur is not None:
            val = another_correct(tree, tree[node].left, stack, cur)
        else:
            val = another_correct(tree, tree[node].left, stack)
        node = stack.pop()
        if val is False or val >= tree[node].key:
            return False
    val = tree[node].key
    if cur is not None and val is not False and cur > val:
        return False
    if tree[node].right != -1:
        return another_correct(tree, tree[node].right, cur=val)
    return val


if __name__ == '__main__':
    n = int(input())
    tree_ = []
    Node = namedtuple('Node', 'key left right')
    an = 'CORRECT'
    for _ in range(n):
        tree_.append(Node(*map(int, input().split())))
    if tree_:
        if another_correct(tree_) is False:
            an = 'INCORRECT'
    print(an)
