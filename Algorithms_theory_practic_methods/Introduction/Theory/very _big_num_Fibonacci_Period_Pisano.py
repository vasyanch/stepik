'''
   Программа получает на вход два числа n и m,
   и выводит в консоль остаток от деления n-того
   числа Фибоначчи на m. Ограничения 1<= n <=10^18, 2<= m <=10^5. 
   В программе использовано свойсто последовательности Фибоначчи
   называемое: период Пизано =) 
'''
def fib_mod(n, m):
    x, y = 0, 1
    i = 0
    for i in range(6*m):
        x, y = y, (x + y) % m
        i += 1
        if (x, y) == (0, 1):
            p = i
            break
    if (n % p) == 0:
        y = 0
    else:
        for i in range(2, (n % p) +1):
            x, y = y, (x + y) % m
    return y

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))

if __name__ == "__main__":
       main()
    
 
