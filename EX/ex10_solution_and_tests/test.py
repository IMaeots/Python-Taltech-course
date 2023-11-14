"""Test cases for solution."""
from solution import *


def test_students_study_during_day():
    """The one with the coffee at noon."""
    assert students_study(12, True) is True


def test_lottery_jackpot():
    """Winning jackpot in the lottery."""
    assert lottery(5, 5, 5) == 10


def test_lottery_all_same_numbers():
    """Same numbers."""
    for num in range(1, 9):
        assert lottery(num, num, num) == 5


def test_correct_fruit_order():
    """Correct fruit order"""
    assert fruit_order(4, 1, 9) is True
