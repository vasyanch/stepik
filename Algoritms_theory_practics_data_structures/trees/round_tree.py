# (key, left_child, right_child)


def in_order(v, tree):
    if tree[v][1] != -1:
        in_order(tree[v][1], tree)
    print(tree[v][0], end=' ')
    if tree[v][2] != -1:
        in_order(tree[v][2], tree)


def pre_order(v, tree):
    print(tree[v][0], end=' ')
    if tree[v][1] != -1:
        pre_order(tree[v][1], tree)
    if tree[v][2] != -1:
        pre_order(tree[v][2], tree)


def post_order(v, tree):
    if tree[v][1] != -1:
        post_order(tree[v][1], tree)
    if tree[v][2] != -1:
        post_order(tree[v][2], tree)
    print(tree[v][0], end=' ')


if __name__ == '__main__':
    n = int(input())
    tree = []
    ans = ''
    for _ in range(n):
        h = tuple(map(int, input().split()))
        tree.append(h)
    in_order(0, tree)
    print(end='\n')
    pre_order(0, tree)
    print(end='\n')
    post_order(0, tree)
