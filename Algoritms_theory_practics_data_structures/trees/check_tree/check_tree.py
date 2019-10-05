'''
не проходит по времени так как каждая вершина проверяется
поиском что приводит к асимптотике O(n*log(n))
'''


import sys
sys.setrecursionlimit(10000)


def search(tree, key, i=0):
    if tree[i][0] == key:
        return i
    if tree[i][0] > key:
        if tree[i][1] != -1:
             i = search(tree, key, tree[i][1])
    else:
        if tree[i][2] != -1:
            i = search(tree, key, tree[i][2])
    return i


if __name__ == '__main__':
    n = int(input())
    tree_ = []
    ans = 'CORRECT'
    for _ in range(n):
        h = tuple(map(int, input().split()))
        tree_.append(h)
    #print(tree_)
    #print(search(tree_, 4))
    for i, v in enumerate(tree_):
        if search(tree_, v[0]) != i:
            ans = 'INCORRECT'
            break
    print(ans)