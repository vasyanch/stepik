# асимптотика O(log(n))
import sys
sys.setrecursionlimit(15000)


def correct(tree, i=0, c=True):
    mi = tree[i][0]  # min in current undertree
    ma = tree[i][0]  # max in current undertree
    if tree[i][1] != -1:
        cur_mi, cur_ma, c = correct(tree, tree[i][1], c)
        if not c:
            return mi, ma, False
        if tree[i][0] <= cur_ma:
            return mi, ma, False
        mi = cur_mi
        # ma = max(ma, cur_ma)
    if tree[i][2] != -1:
        cur_mi, cur_ma, c = correct(tree, tree[i][2], c)
        if not c:
            return mi, ma, False
        if tree[i][0] > cur_mi:
            return mi, ma, False
        ma = cur_ma
    return mi, ma, c


if __name__ == '__main__':
    n = int(input())
    tree_ = []
    an = 'CORRECT'
    for _ in range(n):
        h = tuple(map(int, input().split()))
        tree_.append(h)
    if tree_:
        if not correct(tree_)[2]:
            an = 'INCORRECT'
    print(an)
