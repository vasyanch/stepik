def height(parents):

    # parents - список родителей (на i-ом месте в массиве стоит
    # родитель вершины со значением i)

    ans = 0
    store =[None] * len(parents)
    for c, b in enumerate(parents):
        ch = 1
        q = parents[c]
        while q != -1:
            if store[q] is not None:
                ch += store[q]
                break
            else:
                ch += 1
                q = parents[q]
        store[c] = ch
        ans = max(ans, ch)
    print(store)
    return ans


if __name__ == '__main__':
    n = int(input())
    tree_ = list(map(int, input().split()))
    print(height(tree_))
