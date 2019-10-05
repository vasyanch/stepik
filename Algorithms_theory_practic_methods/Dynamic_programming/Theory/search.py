def bin_search(massif, b):
    n = len(massif)
    m = 0
    while n - m > 1:
        i = (n + m) // 2
        if b < massif[i]:
            n = i 
        else:
            m = i 
    return m
