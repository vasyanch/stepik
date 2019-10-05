def buildHeap(mas, n):
    changes = []

    def siftDown(mas, i, n):
        ind_min = i
        while 2 * i + 1 < n:
            if mas[2 * i + 1] < mas[ind_min]:
                ind_min = 2 * i + 1
            if 2 * i + 2 < n and mas[2 * i + 2] < mas[ind_min]:
                ind_min = 2 * i + 2
            if ind_min != i:
                mas[i], mas[ind_min] = mas[ind_min], mas[i]
                changes.append((i, ind_min))
                i = ind_min
            else:
                break

    for j in range(len(mas) // 2, -1, -1):
        siftDown(mas, j, n)
    return changes 

if __name__ == '__main__':
    n_ = int(input())
    mas_ = list(map(int, input().split()))
    m = buildHeap(mas_, n_)
    print(len(m))
    for w in m:
        print(w[0], w[1])