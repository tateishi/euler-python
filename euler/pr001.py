def is_multiples_of_3_or_5(n: int) -> bool:
    if n % 3 == 0:
        return True
    if n % 5 == 0:
        return True
    return False


def answer(n: int) -> int:
    return sum(m for m in range(1, n) if is_multiples_of_3_or_5(m))
