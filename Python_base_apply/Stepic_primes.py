def primes():
    yield 2
    i = 3
    yield i
    while True:
        i +=1; it = i // 2
        for k in range(2, it + 1):
            if i % k == 0:
               break
            else:
                if k == it:
                    yield i 
