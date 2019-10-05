'''
    Данный скрипт строит графики зависимости времени работы двух функйий,
    вычисляющих n-ое число Фибонначи по различным аллгоритмам,
    в зависимости от входных данныx(т.е. в зависимости от n)
'''    
from matplotlib import pyplot as plt
import time


def timed(f, *args, i_iter=100):
    acc = float('inf')
    for i in range(i_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1-t0)
    return acc 


def compare(fs, args):
	for f in fs:
		plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
		plt.legend()
		plt.grid(True)
	plt.show()

def fib1(n):
	assert n >= 0
	return n if n <=1 else fib1(n-1) + fib1(n-2)

def fib3(n):
    assert n >=0
    f0, f1 =0, 1
    for i in range(n-1):
        f0, f1 = f1, f1 +f0
    return f1
if __name__ == '__main__':
    compare([fib1,fib3], list(range(20)))


