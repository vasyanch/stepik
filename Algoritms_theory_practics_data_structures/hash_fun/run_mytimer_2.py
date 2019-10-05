#Скрин для запуска mytimer_2 или mytimer_2_Python_3_X


import sys, math, mytimer_2_Python_3_X
import eight_ex_prime

reps = 10000
repslist = range(reps)

#Для того чтобы оценить время выполнения каких либо функций
#их необходимо импортировать в этот модуль

'''
def forLoop():
	res = []
	for i in repslist:
		res.append(i + 10)
	return res

def listComp():
    return [i + 10 for i in repslist]

def mapCall():
    return list(map(lambda i: i + 10, repslist))

def genExpr():
    return list(i + 10 for i in repslist)

def genFunc():
    def gen():
        for i in repslist:
            yield i +10
    return list(gen())
'''


'''
print(sys.version)
for tester in (mytimer_2_Python_3_X.timer, mytimer_2_Python_3_X.best):
    print('<%s>' % tester.__name__)
    for test in (forLoop, listComp, mapCall, genExpr, genFunc):
                 elapsed, result = tester(test)
                 print('-' * 35)
                 print('%-9s: %.5f => [%s...%s]' %
                       (test.__name__, elapsed, result[0], result[-1]))
'''

'''
for tester in (mytimer_2_Python_3_X.timer, mytimer_2_Python_3_X.best):
    print('<%s>' % tester.__name__)
    for test in ((eight_ex_prime.prime), (eight_ex_prime.prime_2)):
                 elapsed, result = tester(test, 17)
                 print('-' * 35)
                 print('%-9s: %.5f => %s' %
                       (test.__name__, elapsed, result))
'''

def root_math():
    for i in repslist:
        res = math.sqrt(i)
    return res

def root_pow():
    for i in repslist:
        res = pow(i, .5)
    return res

def root_():
    for i in repslist:
        res =  i ** .5
    return res

seq_root = (root_pow, root_math, root_)



for tester in (mytimer_2_Python_3_X.timer, mytimer_2_Python_3_X.best):
    print('<%s>' % tester.__name__)
    for test in seq_root:
                 elapsed, result = tester(test)
                 print('-' * 35)
                 print('%-9s: %.5f => %s' %
                       (test.__name__, elapsed, result))




 
               
