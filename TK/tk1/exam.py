"""TK1."""
import math


def format_time(minutes: int) -> str:
    """
    Given minutes as an int, return correctly formatted time in hours and minutes.

    Correct format would be '{hours}h {minutes}min'.
    However, if there is not enough minutes to form an hour, show only minutes.
    In that case the format would be '{minutes}min'.
    But when there are no remaining minutes, show only hours.
    In that case the format would be '{hours}h'.
    One hour contains of 60 minutes.

    Examples:
    1) format_time(112) => '1h 52min'.
    2) format_time(23) => '23min'.
    3) format_time(180) => '3h'.

    :param minutes: given minutes
    :return: formatted time in hours and minutes
    """
    hours_float = minutes / 60
    hours_int = math.floor(hours_float)
    minutes_left = minutes - (hours_int * 60)
    if hours_int == 0:
        return f"{minutes_left}min"
    elif (hours_float % 1) == 0:
        return f"{hours_int}h"
    else:
        return f"{hours_int}h {minutes_left}min"


def caught_speeding(speed: int, is_birthday: bool) -> int:
    """
    Return which category speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    caught_speeding(60, False) => 0
    caught_speeding(65, False) => 1
    caught_speeding(65, True) => 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category speeding ticket you would get (0, 1, 2).
    """
    if is_birthday:
        travelling_speed = speed - 5
    else:
        travelling_speed = speed

    if travelling_speed <= 60:
        return 0
    elif travelling_speed <= 80:
        return 1
    elif travelling_speed > 80:
        return 2


def first_half(text: str) -> str:
    """
    Return the first half of an string.

    The length of the string is even.

    first_half('HaaHoo') => 'Haa'
    first_half('HelloThere') => 'Hello'
    first_half('abcdef') => 'abc'
    """
    half = len(text) // 2

    return text[:half]


def num_as_index(nums: list) -> int:
    """
    Return element which index is the value of the smaller of the first and the last element.

    If there is no such element (index is too high), return the smaller of the first and the last element.

    num_as_index([1, 2, 3]) => 2 (1 is smaller, use it as index)
    num_as_index([4, 5, 6]) => 4 (4 is smaller, but cannot be used as index)
    num_as_index([0, 1, 0]) => 0
    num_as_index([3, 5, 6, 1, 1]) => 5

    :param nums: list of non-negative integers.
    :return: element value in the specific index.
    """
    if nums[0] == nums[-1]:
        index = nums[0]
    elif nums[0] < nums[-1]:
        index = nums[0]
    else:
        index = nums[-1]

    try:
        return nums[index]
    except IndexError:
        return index


def remove_in_middle(text: str, to_remove: str) -> str:
    """
    Remove substring from the text, except for the first and the last occurrence.

    remove_in_middle("abc", "def") => "abc"
    remove_in_middle("abcabcabc", "abc") => "abcabc"
    remove_in_middle("abcdabceabcabc", "abc") => "abcdeabc"
    remove_in_middle("abcd", "abc") => "abcd"
    remove_in_middle("abcdabc", "abc") => "abcdabc"
    remove_in_middle("ABCAaaaAA", "a") => "ABCAaaAA

    :param text: string from where the remove takes place.
    :param to_remove: substring to be removed.
    :return: string with middle substrings removed.
    """
    if to_remove not in text:
        return text

    parts = text.split(to_remove)

    if len(parts) >= 4:
        return str(parts[0]) + to_remove + "".join(parts[1:-1]) + to_remove + str(parts[-1])
    else:
        return text
