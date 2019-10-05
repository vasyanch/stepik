'''
    Несколько реализаций алгоритма нахождения наибольшего общего  делителя (НОД).
    Фун test() проверяет алгоритм на адекватность в первом приближении.
'''

from compare_fib1_fib3__timing import timed 
import random
def test(gcd, n_iter=100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b 
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0

        
def gcd1(a, b):
    assert a >= 0, b >= 0
    for d in reversed(range(max(a, b) +1)):
        if d == 0 or a % d == b % d == 0:
            return d

def gcd2(a, b):
    assert a >= 0, b >= 0
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)

def gcd3(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b  == 0:
        return max(a, b)
    elif a >= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)

def gcd4(a, b):
    assert a >= 0 and  b >= 0
    if a == 0 or b  == 0:
        return max(a, b)
    return gcd4(b % a, a)
if __name__ == '__main__':
    for i in [gcd1, gcd2, gcd3, gcd4]:
        print(timed(i, 1000, 990))


    
