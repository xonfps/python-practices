from functions.sum import sum_two_numbers
from functions.sum import sum_three_numbers


def test_sum_two_numbers():
    assert sum_two_numbers(1,2) == 3


def test_sum_three_numbers():
    assert sum_three_numbers(1,1,1) == 3
