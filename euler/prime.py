WHEEL30 = [7, 11, 13, 17, 19, 23, 29, 31]

def maybe_prime():
    yield 2
    yield 3
    yield 5

    count = 0
    base = 0
    while True:
        yield WHEEL30[count] + base
        count += 1
        if count >= len(WHEEL30):
            count = 0
            base += 30
