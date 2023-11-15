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
    assert password.includes_uppercase("") is False


def test_includes_uppercase__includes_number():
    """Test uppercase."""
    assert password.includes_uppercase("ask212") is False


def test_includes_uppercase__true_but_first_lowercase():
    """Test uppercase."""
    assert password.includes_uppercase("aSk") is True


def test_includes_uppercase__only_all_uppercase():
    """Test uppercase."""
    assert password.includes_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ") is True


def test_includes_lowercase__empty():
    """Test lowercase."""
    assert password.includes_lowercase("") is False


def test_includes_lowercase__includes_number():
    """Test lowercase."""
    assert password.includes_lowercase("ASK212") is False


def test_includes_lowercase__true_but_first_uppercase():
    """Test uppercase."""
    assert password.includes_lowercase("AsK") is True


def test_includes_lowercase__only_all_lowercase():
    """Test uppercase."""
    assert password.includes_lowercase("abcdefghijklmnopqrstuvwxyz") is True


def test_includes_special__empty():
    """Test special."""
    assert password.includes_special("") is False


def test_includes_special__whitespaces():
    """Test special."""
    assert password.includes_special("ab cd !") is True


def test_includes_special__no_special():
    """Test special."""
    assert password.includes_special("abc") is False


def test_includes_special__multiple_specials():
    """Test special."""
    assert password.includes_special("a/!@#$%^&*()_+=-][{}~") is True


def test_includes_number__empty():
    """Test number."""
    assert password.includes_number("") is False


def test_includes_number__every_digit():
    """Test number."""
    assert password.includes_number("0123456789") is True


def test_includes_number__no_digits():
    """Test number."""
    assert password.includes_number("abcabc") is False


def test_includes_number__true_but_number_not_first():
    """Test number."""
    assert password.includes_number("abc123abc") is True


def test_is_different__not_case_sensitive():
    """Test difference funtion."""
    assert password.is_different_from_old_password("abDE12!", "abDE12!") is False


def test_is_different__new_pass_even_length__barely_different():
    """Test difference function."""
    assert password.is_different_from_old_password("abDE2!", "abFG2!") is True


def test_is_different__new_pass_odd_length__barely_different():
    """Test difference function."""
    assert password.is_different_from_old_password("abDFE2!", "abDGF2!") is True


def test_is_different__new_pass_odd_length__barely_different_reverse():
    """Test difference function."""
    assert password.is_different_from_old_password("abDFE2!", "!2EGDba") is True


def test_is_different__new_pass_even_length__barely_different_reverse():
    """Test difference function."""
    assert password.is_different_from_old_password("abDE2!", "!2GFba") is True


def test_is_different__new_pass_even_length__barely_not_different():
    """Test difference function."""
    assert password.is_different_from_old_password("hxm21!", "abD21!") is False


def test_is_different__new_pass_odd_length__barely_not_different():
    """Test difference function."""
    assert password.is_different_from_old_password("abDEF1!", "lmzEF1!") is False


def test_is_different__new_pass_even_length__barely_not_different_reverse():
    """Test difference function."""
    assert password.is_different_from_old_password("abDE1!", "!1Efcd") is False


def test_is_different__new_pass_odd_length__barely_not_different_reverse():
    """Test difference function."""
    assert password.is_different_from_old_password("abDEF1!", "!1FEhdf") is False
