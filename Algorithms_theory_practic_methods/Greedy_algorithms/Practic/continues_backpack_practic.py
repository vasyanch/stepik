import heapq


def backpack(volume, val_and_weights):
    order = [(-v/w, w) for v, w in val_and_weights]
    heapq.heapify(order)
    
    acc = 0 
    while order and volume:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, volume)
        acc -= v_per_w * can_take
        volume -= can_take
    return acc


def main():
    n, volume = map(int, input().split())
    val_and_weights = list(tuple(map(int, input().split())) for line in range(n))
    assert len(val_and_weights) == n 
    opt_value  = backpack(volume, val_and_weights)
    print('{:.3f}'.format(opt_value))


def test_():
    assert backpack(0, [(60, 20)]) == 0.0
    assert backpack(25, [(60, 20)]) == 60
    assert backpack(25, [(60, 20), (50, 50)]) == 60 + 5.0
    assert backpack(25, [(60, 20), (0, 100)]) == 60
    assert backpack(50, [(60, 20), (100, 50), (120, 30)]) == 180.0

    from random import randint
    import compare_fib1_fib3_timing
    for attempt in range(100):
        n = randint(0, 100)
        volume = randint(0, 2 * 10 ** 6)
        val_and_weights = []
        for i in range(n):
           val_and_weights.append(
               (randint(0, 2 * 10 ** 6), randint(0, 2 * 10 ** 6)))
        t = timed(backpack, volume, val_and_weights)
        assert t < 5
    
    
if __name__ == '__main__':
    test_()
