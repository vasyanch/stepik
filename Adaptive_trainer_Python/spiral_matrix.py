'''
 На вход программы дается  целое число n. Необходимо вывести матрицу
 nXn, такую что цифры в ней расположены по спирали начиная
 с верхнего левого угла. От 1 до n^2. для пяти это выглядит так:
 1  2  3  4  5
16 17 18 19  6
15 24 25 20  7
14 23 22 21  8
13 12 11 10  9
'''


def fun(i, j, n, a, b, ans):
    if j > n:
        return ans
    else:
        while j < n:
            ans[i][j] = a
            j += 1
            a += 1
        i += 1
        j -= 1
        while i < n:
            ans[i][j] = a
            i += 1 
            a += 1
        i -= 1
        j -= 1
    
        while j >= b:
            ans[i][j] = a
            j -= 1
            a += 1
        i -= 1
        j += 1
        while i >= b + 1:
            ans[i][j] = a
            i -= 1
            a += 1
        return fun(i+1, j+1, n-1, a,  b+1, ans)
        
if __name__ == '__main__':
    n = int(input())
    ans = [[0]*n for _ in range(n)]
    for x in fun(0, 0, n, 1, 0, ans):
        for _ in x:
            print(_, end = ' ')
        print()
