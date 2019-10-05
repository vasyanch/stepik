'''
    На вход подается  число 1≤n≤10^7, программа возвращает последнюю
    цифру n-го числа Фибоначчи.
'''
    
def fun_fib(n):
    lst = [0, 1]
    for i in  range(2, n + 1):
        lst.append((lst[0] + lst[1]) % 10)
        lst.pop(0)
    return lst[1]
def main():
    print(fun_fib(int(input())))

if __name__ == '__main__':
    main()    
