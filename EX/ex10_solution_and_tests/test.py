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


def test_lottery__a_has_one_same():
    """Lottery function test."""
    for num1 in range(10):
        for num2 in range(10):
            if num1 != num2:
                assert lottery(num1, num1, num2) == 0
                assert lottery(num1, num2, num1) == 0
                assert lottery(num1, num2, num2) == 1


def test_lottery__all_diff():
    """Lottery function test."""
    for num1 in range(10):
        for num2 in range(10):
            for num3 in range(10):
                if num1 != num2 and num1 != num3 and num2 != num3:
                    assert lottery(num1, num2, num3) == 1


"""Fruit order function tests."""


def test_fruit_order__all_zero():
    """Fruit order function test."""
    assert fruit_order(0, 0, 0) == 0


def test_fruit_order__one_input_non_zero():
    """Fruit order function test."""
    for num in range(1, 10):
        assert fruit_order(num, 0, 0) == 0
        assert fruit_order(0, num, 0) == 0
        assert fruit_order(0, 0, num) == -1


def test_fruit_order__zero_amount_others_not_zero():
    """Fruit order function test."""
    for num1 in range(1, 10):
        for num2 in range(1, 10):
            assert fruit_order(num1, num2, 0) == 0


def test_fruit_order__only_big_exact_match():
    """Fruit order function test."""
    for num1 in range(1, 10):
        assert fruit_order(0, num1, (num1 * 5)) == 0


def test_fruit_order__only_big_not_enough():
    """Fruit order function test."""
    assert fruit_order(0, 5, 30) == -1


def test_fruit_order__only_big_more_than_required_match():
    """Fruit order function test."""
    assert fruit_order(0, 6, 20) == 0


def test_fruit_order__only_big_more_than_required_no_match():
    """Fruit order function test."""
    assert fruit_order(0, 5, 12) == -1


def test_fruit_order__only_small_match_more_than_5_smalls():
    """Fruit order function test."""
    assert fruit_order(20, 0, 10) == 10


def test_fruit_order__only_small_not_enough():
    """Fruit order function test."""
    assert fruit_order(10, 0, 12) == -1


def test_fruit_order__only_small_exact_match():
    """Fruit order function test."""
    assert fruit_order(20, 0, 20) == 20


def test_fruit_order__all_positive_exact_match():
    """Fruit order function test."""
    assert fruit_order(6, 1, 11) == 6


def test_fruit_order__use_all_smalls_some_bigs():
    """Fruit order test."""
    assert fruit_order(4, 2, 9) == 4


def test_fruit_order__use_some_smalls_all_bigs():
    """Fruit order function test."""
    assert fruit_order(6, 3, 20) == 5


def test_fruit_order__not_enough():
    """Fruit order function test."""
    assert fruit_order(12, 5, 38) == -1


def test_fruit_order__not_enough_with_more_than_5_smalls():
    """Fruit order function test."""
    assert fruit_order(6, 1, 12) == -1


def test_fruit_order__use_some_smalls_some_bigs():
    """Fruit order function test."""
    assert fruit_order(4, 2, 8) == 3


def test_fruit_order__enough_bigs_not_enough_smalls():
    """Fruit order function test."""
    assert fruit_order(2, 4, 19) == -1


def testfruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Fruit order function test."""
    assert fruit_order(3, 120, 204) == -1
