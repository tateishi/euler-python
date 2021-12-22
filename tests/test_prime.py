from euler.prime import maybe_prime

def test_maybe_prime():
    maybe_prime_iter = maybe_prime()
    assert  next(maybe_prime_iter) == 2
    assert  next(maybe_prime_iter) == 3
    assert  next(maybe_prime_iter) == 5
    assert  next(maybe_prime_iter) == 7
    assert  next(maybe_prime_iter) == 11
    assert  next(maybe_prime_iter) == 13
    assert  next(maybe_prime_iter) == 17
    assert  next(maybe_prime_iter) == 19
    assert  next(maybe_prime_iter) == 23
    assert  next(maybe_prime_iter) == 29
    assert  next(maybe_prime_iter) == 31
    assert  next(maybe_prime_iter) == 37
    assert  next(maybe_prime_iter) == 41
    assert  next(maybe_prime_iter) == 43
    assert  next(maybe_prime_iter) == 47
    assert  next(maybe_prime_iter) == 49
    assert  next(maybe_prime_iter) == 53
    assert  next(maybe_prime_iter) == 59
    assert  next(maybe_prime_iter) == 61
    assert  next(maybe_prime_iter) == 67
    assert  next(maybe_prime_iter) == 71
    assert  next(maybe_prime_iter) == 73
    assert  next(maybe_prime_iter) == 77
    assert  next(maybe_prime_iter) == 79
    assert  next(maybe_prime_iter) == 83
    assert  next(maybe_prime_iter) == 89
    assert  next(maybe_prime_iter) == 91
    assert  next(maybe_prime_iter) == 97
