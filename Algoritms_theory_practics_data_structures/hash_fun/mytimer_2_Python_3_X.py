'''
Вместо формы ** и метода pop словарей используются аргументы,
которые могут передаваться только по именам,
появившиеся в версии 3.0. В версии 3.0 нет необходимости
выносить вызов range() за пределы цикла, так как эта
функция возвращает генератор, а не список
'''


import time, sys

trace = lambda *args: None # or print

timefunc = time.clock if sys.platform == 'win32' else time.time

def timer(func, *pargs, _reps=1000, **kargs):
    trace(func, pargs, kargs, _reps)
    start = timefunc()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)

def best(func, *pargs, _reps=50, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        (time,ret)=timer(func,*pargs,_reps=1,**kargs)
        if time < best: best = time
    return (best, ret)
