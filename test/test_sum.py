from functions.sum import sum_two_numbers, sum_several_numbers


def test_sum_two_numbers():
    assert sum_two_numbers(1,2) == 3


def test_sum_several_numbers():
    assert sum_several_numbers(1,1,1) == 3
