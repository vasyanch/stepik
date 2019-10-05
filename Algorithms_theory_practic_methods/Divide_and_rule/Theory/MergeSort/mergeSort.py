'''
    Сортировка слиянием, фун. mergeSort(massif) принимает на
    вход массив, который необходимо отсортировать и
    выводит отсортированный массив в виде строки.   
'''
import heapq
from compare_fib1_fib3__timing import timed
from random import randint
from matplotlib import pyplot as plt


def compare(fs, args):
    for f in fs:
        plt.plot([len(i) for i in args],
                 [timed(f, arg) for arg in args],
                 label=f.__name__)
        plt.legend()
        plt.grid(True)
    plt.show()


def test(fs, n):
    args = []
    for i in range(n):
        args.append([randint(0, 10**3) for _ in range((i+1)*10)])
    compare(fs, args)


def mergeSort(massif):
    end = len(massif)
    if end > 1:
        m = (end - 0) // 2
        return merge(mergeSort(massif[0:m]), mergeSort(massif[m:end]))
    else:
        return massif


def mergeSort_heap(massif):
    '''
    Сортировка слиянием с использованием очереди с приорететами 
    вместо рекурсии. 
    '''
    Q = []
    heapq.heapify(Q)
    for i in massif:
        heapq.heappush(Q, [i])
    while len(Q) > 1:
        heapq.heappush(
            Q, merge(heapq.heappop(Q), heapq.heappop(Q)))
    return heapq.heappop(Q)


def merge(a, b):
    ans = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1
    if i == len(a):
        ans += b[j:]
    else:
        ans += a[i:]
    return ans


def main():
    n = input()
    massif = list(map(int, input().split()))
    print(' '.join(str(i) for i in mergeSort(massif)))

if __name__ == '__main__':
    test([mergeSort, mergeSort_heap], 20)
