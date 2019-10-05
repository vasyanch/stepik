from random import randint
'''
    Алгоритм быстрой сортировки. Время работы O(nlogn)
    для массивов в которых не значителное кол-во
    равных между собой элементов отн-во всех элементов.
    Если равных эл-ов много то нужно в partition  прописать
    3-й регион с элементами равными опорному
    (т.е. поддерживать три региона <x, =x, >x).
'''



def test(f, n=800, m = 500):
    for i in range(n):
        l = list(randint(0, 10 ** 5) for i in range(m))
        #print(l)
        l1 = l[:]
        fun = f(l, r=len(l))
        l1.sort()
        #print(l1, fun)
        assert l1 == fun
    print('Good!')
    
    
def quickSort(lst, l=0, r=0):
    while l < r:
        _ = randint(l, r-1)
        lst[l], lst[_] = lst[_], lst[l]
        m = partition(lst, l, r)
        if m - l > r - m:
            quickSort(lst, m+1, r)
            r = m
        else:
            quickSort(lst, l, m)
            l = m + 1
    return lst
 

def partition(lst, l, r):
    x = lst[l]
    j = l  
    for i in range(l+1, r):
        if lst[i] < x:
            j += 1
            lst[j], lst[i] = lst[i], lst[j]
    lst[j], lst[l] = lst[l], lst[j]
    return j
            

def main():
    lst = list(map(int, input().split()))    
    print(quickSort(lst, r=len(lst))) 


if __name__ == '__main__':
    test(quickSort)
