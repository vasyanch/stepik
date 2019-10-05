'''
    Двоичный поиск в упорядоченом массиве.
     В первой строке нв вход дается целое число 1 ≤ n ≤ 10*5 и
     массив A[1…n] из n различных натуральных чисел, не превышающих 10*9,
     в порядке возрастания, во второй — целое число 1 ≤ k ≤ 10*5 и
     k натуральных чисел b1,…,bk, не превышающих 10*9.
     Для каждого i от 1 до k необходимо вывести индекс 1 ≤ j ≤ n,
     для которого A[j]=bi, или −1, если такого j нет.
'''


def bin_sear(sort_list, b):
    ans = -2
    n = len(sort_list)
    m = 0
    i = (n - m) // 2
    while n > m:
        if sort_list[i] > b:
            n = i 
            i -= (n - m) // 2 or 1 
        elif sort_list[i] < b:
            m = i + 1 
            i += (n - m) // 2 or 1
        else:
            ans = i
            break
    return ans + 1  


def main():
    sort_list = list(map(int, input().split()))
    k_list = list(map(int, input().split()))  
    n, k = sort_list.pop(0), k_list.pop(0)
    ans = []
    for i in k_list:
        ans.append(bin_sear(sort_list, i))
    return ' '.join(str(i) for i in ans)


if __name__ == '__main__':
    print(main())

