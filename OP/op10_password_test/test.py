"""Password validation tests."""
from EX.ex04_validation import password


def test_is_correct_length__empty():
    assert password.is_correct_length("") is False


def test__is_correct_length__too_short():
    """Test whether password of length 7 is not correct."""
    assert password.is_correct_length("passwor") is False


def test__is_correct_length__too_long():
    """Test whether password of length > 64 is incorrect."""
    assert password.is_correct_length("pass" * 18) is False
