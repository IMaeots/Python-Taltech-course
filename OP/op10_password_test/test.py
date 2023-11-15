"""Password validation tests."""
import password
# For testing
# from EX.ex04_validation import password


def test_is_correct_length__empty():
    """Test is correct length function."""
    assert password.is_correct_length("") is False


def test_is_correct_length__too_short():
    """Test whether password of length up to 7 is not correct."""
    assert password.is_correct_length("p") is False
    assert password.is_correct_length("pa") is False
    assert password.is_correct_length("pas") is False
    assert password.is_correct_length("pass") is False
    assert password.is_correct_length("passw") is False
    assert password.is_correct_length("passwo") is False
    assert password.is_correct_length("passwor") is False


def test_is_correct_length__too_long():
    """Test whether password of length > 64 is incorrect."""
    assert password.is_correct_length("password" * 8 + 'a') is False
    assert password.is_correct_length("pass" * 18) is False


def test_is_correct_length__edge_cases():
    """Test edge cases."""
    assert password.is_correct_length("password" * 8) is True
    assert password.is_correct_length("password") is True


def test_includes_uppercase__empty():
    """Test uppercase."""
    assert password.includes_password("") is False
