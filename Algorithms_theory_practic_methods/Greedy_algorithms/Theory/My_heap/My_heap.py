def siftdown(heap, i):
    while 2 * i < len(heap) :
        j = i                          #j - индекс наибольшего из тройки 
        if heap[2 * i] > heap[i]:
            j = 2 * i
        if 2 * i + 1 < len(heap) and heap[2*i + 1] > heap[j]:
            j = 2 * i + 1
        if i == j:
            break
        else:
            heap[i], heap[j] = heap[j], heap[i]
            i = j
            
def siftup(heap, i):
    while i > 1 and  heap[i] > heap[i // 2]:
        heap[i // 2], heap[i] = heap[i], heap[i // 2]
        i //= 2 
        
def insert(heap, a):
    heap.append(a)
    siftup(heap, len(heap)-1)
    

def extract_max(heap):
    if len(heap) > 2:
        ans = heap[1]
        heap[1] = heap.pop(-1)
        siftdown(heap, 1)
    else:
        ans = heap.pop(1)
    return ans
        

def main():                                     
    heap = ['heap']
    for i in range(int(input(''))):
        s = input('').strip()
        if s == 'ExtractMax':
            print(extract_max(heap))
        else: 
            s = s.split()
            insert(heap, int(s[1]))

if __name__ == '__main__':
    main()
