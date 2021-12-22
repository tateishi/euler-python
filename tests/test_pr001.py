from euler.pr001 import is_multiples_of_3_or_5, answer

def test_is_multiples_of_3_or_5():
    assert not is_multiples_of_3_or_5(1)
    assert not is_multiples_of_3_or_5(2)
    assert     is_multiples_of_3_or_5(3)
    assert not is_multiples_of_3_or_5(4)
    assert     is_multiples_of_3_or_5(5)


def test_answer():
    assert answer(10) == 23
