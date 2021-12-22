WHEEL30 = [7, 11, 13, 17, 19, 23, 29, 31]


def maybe_prime():
    for n in [2, 3, 5]:
        yield n

    base = 0
    while True:
        for n in WHEEL30:
            yield n + base
        base += 30


def prime():
    maybe = maybe_prime()

    for mp in maybe:
        for n in maybe_prime():
            if n * n > mp:
                yield mp
                break
            if mp % n == 0:
                break
