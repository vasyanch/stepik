import sys
sys.setrecursionlimit(10000)


def height(lst, root):
    if lst[root] is None:
        return 1
    elif lst[root] is int:
        return lst[root]
    else:
        hgt = 0
        for _ in lst[root]:
            hgt = max(hgt, height(lst, _))
        lst[root] = hgt
    return 1 + hgt


if __name__ == '__main__':
    n = int(input())
    tree_ = list(map(int, input().split()))
    lst_child = [None] * len(tree_)
    for i, v in enumerate(tree_):
        if v == -1:
            root_ = i
        else:
            if lst_child[v] is None:
                lst_child[v] = []
            lst_child[v].append(i)
    print(height(lst_child, root_))
    print(lst_child)