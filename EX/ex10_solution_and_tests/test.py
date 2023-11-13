"""Test cases for solution."""
from solution import *


def test_students_study_during_day():
    """
    The one with the coffee at noon.

    During the day, students study when there is coffee.
    This case represents the time period of a day and coffee is present.
    Expected result: True.
    """
    assert students_study(12, True) is True


def test_lottery_jackpot():
    """
    Winning jackpot in the lottery.

    All numbers must be 5.
    Expected result: 10.
    """
    assert lottery(5, 5, 5) == 10


def test_lottery_all_same_numbers():
    """
    Same numbers.

    Expected result: 5.
    """
    for num in range(1,9):
        assert lottery(num, num, num) == 5


def test_correct_fruit_order():
    """
    Fruit order.

    Expected result: True.
    """
    assert fruit_order(4, 1, 9) is True
