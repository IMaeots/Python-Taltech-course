"""Test cases for solution."""
from solution import students_study
from solution import lottery
from solution import fruit_order


"""Students study function tests."""


def test_student_study__night_coffee_true():
    """Student study test."""
    for num in range(1, 5):
        assert students_study(num, True) is False


def test_student_study__night_coffee_false():
    """Student study test."""
    for num in range(1, 5):
        assert students_study(num, False) is False


def test_student_study__day_coffee_true():
    """Student study test."""
    for num in range(5, 18):
        assert students_study(num, True) is True


def test_student_study__day_coffee_false():
    """Student study test."""
    for num in range(5, 18):
        assert students_study(num, False) is False


def test_student_study__evening_coffee_true():
    """Student study test."""
    for num in range(18, 25):
        assert students_study(num, True) is True


def test_student_study__evening_coffee_false():
    """Student study test."""
    for num in range(18, 25):
        assert students_study(num, False) is True


"""Lottery function tests."""


def test_lottery__all_fives():
    """Lottery function test."""
    assert lottery(5, 5, 5) == 10


def test_lottery__all_same_positive():
    """Lottery function test."""
    for num in range(10):
        if num != 5:
            assert lottery(num, num, num) == 5


def test_lottery__all_same_negative():
    """Lottery function test."""
    for num in range(-10, 0):
        if num != 5:
            assert lottery(num, num, num) == 5


def test_lottery__all_same_zero():
    """Lottery function test."""
    assert lottery(0, 0, 0) == 5


def test_lottery__a_b_same_c_diff():
    """Lottery function test."""
    pass


def test_lottery__a_c_same_b_diff():
    """Lottery function test."""
    pass


def test_lottery__b_c_same_a_diff():
    """Lottery function test."""
    pass


def test_lottery__all_diff():
    """Lottery function test."""
    pass


"""Fruit order function tests."""


def test_fruit_order__all_zero():
    """Fruit order function test."""
    pass

def test_fruit_order__zero_amount_zero_small():
    """Fruit order function test."""
    pass


def test_fruit_order__zero_amount_zero_big():
    """Fruit order function test."""
    pass


def test_fruit_order__zero_amount_others_not_zero():
    """Fruit order function test."""
    pass


def test_fruit_order__only_big_exact_match():
    """Fruit order function test."""
    pass


def test_fruit_order__only_big_not_enough_but_multiple_of_5():
    """Fruit order function test."""
    pass


def test_fruit_order__only_big_not_enough():
    """Fruit order function test."""
    pass


def test_fruit_order__only_big_more_than_required_match():
    """Fruit order function test."""
    pass


def test_fruit_order__only_big_more_than_required_no_match():
    """Fruit order function test."""
    pass


def test_fruit_order__only_small_match_more_than_5_smalls():
    """Fruit order function test."""
    pass


def test_fruit_order__only_small_not_enough_more_than_5_smalls():
    """Fruit order function test."""
    pass


def test_fruit_order__only_small_exact_match():
    """Fruit order function test."""
    pass


def test_fruit_order__only_small_not_enough():
    """Fruit order function test."""
    pass


def test_fruit_order__only_small_more_than_required():
    """Fruit order function test."""
    pass


def test_fruit_order__match_with_more_than_5_smalls():
    """Fruit order function test."""
    pass


def test_fruit_order__all_positive_exact_match():
    """Fruit order function test."""
    pass


def test_fruit_order__use_all_smalls_some_bigs():
    """Fruit order function test."""
    pass


def test_fruit_order__use_some_smalls_all_bigs():
    """Fruit order function test."""
    pass


def test_fruit_order__use_some_smalls_some_bigs():
    """Fruit order function test."""
    pass


def test_fruit_order__not_enough():
    """Fruit order function test."""
    pass


def test_fruit_order__enough_bigs_not_enough_smalls():
    """Fruit order function test."""
    pass


def test_fruit_order__not_enough_with_more_than_5_smalls():
    """Fruit order function test."""
    pass


def test_fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Fruit order function test."""
    pass


def test_fruit_order__match_large_numbers():
    """Fruit order function test."""
    pass
