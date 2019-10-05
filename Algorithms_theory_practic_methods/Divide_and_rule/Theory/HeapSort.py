'''
    Сортировка кучей. Время работы жестко О(nlogn).
     На вход функции heapSort поддается массив,
     кот. нужно отсортировать. На первом шаге
     из него строится max-куча на основе массива(полное двоичное дерево),
     далее происходит сортировка, путем перестановки 1-го(max)
     и последнего элементов массива, а далее первый элемент
     просеивается вниз.
    
'''
from random import randint


def siftdown(heap, i, size):
    while 2 * i < size:
        j = i                          #j - индекс наибольшего из тройки 
        if heap[2 * i] > heap[i]:
            j = 2 * i
        if 2 * i + 1 < size  and heap[2*i + 1] > heap[j]:
            j = 2 * i + 1
        if i == j:
            break
        else:
            heap[i], heap[j] = heap[j], heap[i]
            i = j

def heapSort(lst):
    lst.insert(0, 'heap')
    for i in range(len(lst) // 2, 0, -1):
        siftdown(lst, i, len(lst))
    size = len(lst)
    while size > 2:
        lst[1], lst[size - 1] = lst[size - 1], lst[1]
        size -= 1
        siftdown(lst, 1, size)
    return lst[1:]

def test(f, n=800, m = 500):
    for i in range(n):
        l = list(randint(0, 10 ** 5) for i in range(m))
        #print(l)
        l1 = l[:]
        fun = f(l)
        l1.sort()
        #print(l1, fun)
        assert l1 == fun
    print('Good!')
    

if __name__ == '__main__':
    test(heapSort)
