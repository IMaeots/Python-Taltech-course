"""Solution to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if time in range(18, 25):
        return True

    if time in range(5, 18):
        return coffee_needed

    if time in range(1, 5):
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c == 5:
        return 10

    if a == b == c:
        return 5

    if a != b and a != c:
        return 1

    return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if (small_baskets + big_baskets * 5) < ordered_amount:
        return -1
    elif big_baskets == 0:
        return ordered_amount
    elif big_baskets <= ordered_amount // 5:
        return ordered_amount - (5 * big_baskets)
    elif (ordered_amount % 5) <= small_baskets:
        return ordered_amount % 5
    else:
        return -1
