# Оход in-order подходит для проверки бинарного дерева в котором нет одинаковых ключей
from collections import namedtuple


def correct(tree):
    if tree:
        node, stack, old = 0, [], None
        while node >= 0 or stack:
            if node >= 0:
                stack.append(node)
                node = tree[node].left
                continue
            node = stack.pop()
            cur = tree[node].key
            node = tree[node].right
            if old and cur < old:
                return 'INCORRECT'
            old = cur
    return 'CORRECT'


if __name__ == '__main__':
    n = int(input())
    Node = namedtuple('Node', 'key left right')
    tree = []
    for _ in range(n):
        tree.append(Node(*map(int, input().split())))
    print(correct(tree))
