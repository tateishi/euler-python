WHEEL30 = [7, 11, 13, 17, 19, 23, 29, 31]


def maybe_prime():
    for n in [2, 3, 5]:
        yield n

    base = 0
    while True:
        for n in WHEEL30:
            yield n + base
        base += 30
