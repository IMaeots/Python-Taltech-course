"""KT2."""


def switch_lasts_and_firsts(s: str) -> str:
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    if len(s) < 4:
        return s[::-1]

    beginning = s[:2]
    end = s[-2:]
    middle = s[2:-2]

    return end + middle + beginning


def min_diff(nums: list) -> int:
    """
    Find the smallest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1
    min_diff([1, 9, 17]) => 8
    min_diff([100, 90]) => 10
    min_diff([1, 100, 1000, 1]) => 0

    :param nums: list of ints, at least 2 elements.
    :return: min diff between 2 numbers.
    """
    differences = []
    for i in range(len(nums)):
        for index in range(len(nums)):
            if i == index:
                continue
            else:
                differences.append(abs(nums[i] - nums[index]))

    return min(differences)


def get_symbols_by_occurrences(text: str) -> dict:
    """
    Return dict where key is the occurrence count and value is a list of corresponding symbols.

    The order of the counts and the symbols is not important.

    get_symbols_by_occurrences("hello") => {1: ['e', 'o', 'h'], 2: ['l']}
    get_symbols_by_occurrences("abcaba") => {2: ['b'], 1: ['c'], 3: ['a']}
    """
    if not text:
        return {}

    letter_dict = {}
    for letter in text:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1

    repetition_dict = {}
    for letter, amount in letter_dict.items():
        if amount not in repetition_dict:
            repetition_dict[amount] = [letter]
        else:
            repetition_dict[amount].append(letter)

    return repetition_dict


def sum_of_digits_recursion(s: str) -> int:
    """
    Return sum of all the digits.

    The input string contains different symbols.
    Sum all the digits.

    The function has to be recursive (no loops allowed).

    sum_of_digits_recursion("123") => 6
    sum_of_digits_recursion("a") => 0
    sum_of_digits_recursion("") => 0
    sum_of_digits_recursion("1-2-3-99") => 24
    """
    if len(s) < 1:
        return 0

    num = int(s[0]) if s[0].isdigit() else 0

    return num + sum_of_digits_recursion(s[1:])


if __name__ == '__main__':
    print(switch_lasts_and_firsts("ambulance"))  # => "cebulanam"
    print(switch_lasts_and_firsts("firetruck"))  # => "ckretrufi"
    print(switch_lasts_and_firsts("car"))  # => "rac"

    print(min_diff([1, 2, 3]))  # => 1
    print(min_diff([1, 9, 17]))  # => 8
    print(min_diff([100, 90]))  # => 10
    print(min_diff([1, 100, 1000, 1]))  # => 0

    print(get_symbols_by_occurrences("hello"))  # => {1: ['e', 'o', 'h'], 2: ['l']}
    print(get_symbols_by_occurrences("abcaba"))  # => {2: ['b'], 1: ['c'], 3: ['a']}

    print(sum_of_digits_recursion("123"))  # 6
    print(sum_of_digits_recursion(""))  # 0
