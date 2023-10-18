"""Conversation."""
import re
import math
from typing import Union


class Student:
    """Student class which interacts with the server."""

    def __init__(self, biggest_number: int):
        """
        Initialize Student object.

        Save the biggest number into a variable that is attainable later on.
        Create a collection of all possible results [possible_answers] <- dont rename that (can be a list or a set)
        :param biggest_number: biggest possible number(inclusive) to guess
        NB: calculating using sets is much faster compared to lists
        """
        self.possible_answers = set([all_possible_answers for all_possible_answers in range(biggest_number + 1)])

    def decision_branch(self, sentence: str):
        """
        Regex can and should be used here.

        :param sentence: sentence to solve
        call one of the functions bellow (within this class) and return either one of the following strings:
        f"Possible answers are {sorted_list_of_possible_answers_in_growing_sequence)}." if there are multiple possibilities
        f"The number I needed to guess was {final_answer}." if the result is certain
        """
        """
        if (completed):
            return f"Possible answers are {sorted_list_of_possible_answers_in_growing_sequence}."
        else: 
            return f"The number I needed to guess was {final_answer}."
        """

    def intersect_possible_answers(self, update: list):
        """
        Logical AND between two sets.

        :param update: new list to be put into conjunction with self.possible_answers
        conjunction between self.possible_answers and update
        https://en.wikipedia.org/wiki/Logical_conjunction
        """
        self.possible_answers = set(update).intersection(self.possible_answers)

    def exclude_possible_answers(self, update: list):
        """
        Logical SUBTRACTION between two sets.

        :param update: new list to be excluded from self.possible_answers
        update excluded from self.possible_answers
        """
        self.possible_answers = self.possible_answers - set(update)

    def deal_with_number_of_zeroes(self, amount_of_zeroes: int):
        """
        Filter possible_answers to match the amount of zeroes in its binary form.

        :param amount_of_zeroes: number of zeroes in the correct number's binary form
        """
        possible_answers = set()
        for num in self.possible_answers:
            binary_representation = bin(num)[2:]
            zero_count = binary_representation.count('0')
            if zero_count == amount_of_zeroes:
                possible_answers.add(num)

        self.possible_answers = possible_answers

    def deal_with_number_of_ones(self, amount_of_ones: int):
        """
        Filter possible answers to match the amount of ones in its binary form.

        :param amount_of_ones: number of zeroes in the correct number's binary form
        """
        possible_answers = set()
        for num in self.possible_answers:
            binary_representation = bin(num)[2:]
            one_count = binary_representation.count('1')
            if one_count == amount_of_ones:
                possible_answers.add(num)

        self.possible_answers = possible_answers

    def deal_with_primes(self, is_prime: bool):
        """
        Filter possible answers to either keep or remove all primes.

        Call find_primes_in_range to get all composite numbers in range.
        :param is_prime: boolean whether the number is prime or not
        """
        biggest_num = max(self.possible_answers)
        prime_numbers = set(find_primes_in_range(biggest_num))

        self.possible_answers = self.possible_answers & prime_numbers if is_prime \
            else self.possible_answers - prime_numbers

    def deal_with_composites(self, is_composite: bool):
        """
        Filter possible answers to either keep or remove all composites.

        Call find_composites_in_range to get all composite numbers in range.
        :param is_composite: boolean whether the number is composite or not
        """
        biggest_num = max(self.possible_answers)
        composite_numbers = set(find_composites_in_range(biggest_num))

        self.possible_answers = self.possible_answers & composite_numbers if is_composite \
            else self.possible_answers - composite_numbers

    def deal_with_dec_value(self, decimal_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param decimal_value: decimal value within the number like 9 in 192
        """
        possible_answers = set()
        for num in self.possible_answers:
            if len(str(num)) < 2:
                continue
            elif str(num)[1] != decimal_value:
                continue
            else:
                possible_answers.add(num)

        self.possible_answers = possible_answers  # I currently assume that the numbers are not with commas and weird.

    def deal_with_hex_value(self, hex_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param hex_value: hex value within the number like e in fe2
        """
        possible_answers = set()
        for num in self.possible_answers:
            if len(str(num)) < 2:
                continue
            elif str(num)[1] != hex_value:
                continue
            else:
                possible_answers.add(num)

        self.possible_answers = possible_answers  # I currently assume that the numbers are not with commas and weird.

    def deal_with_quadratic_equation(self, equation: str, to_multiply: bool, multiplicative: float, is_bigger: bool):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        Regex can be used here.
        Call quadratic_equation_solver with variables a, b, c.
        deal_with_dec_value should be called.
        :param equation: the quadratic equation
        :param to_multiply: whether it is necessary to multiply or divide with a given multiplicative
        :param multiplicative: the multiplicative to multiply or divide with
        :param is_bigger: to use the bigger or smaller result of the quadratic equation(min or max from [x1, x2])
        """
        pass

    def deal_with_fibonacci_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all fibonacci numbers.

        Call find_fibonacci_numbers to get all fibonacci numbers in range.
        :param is_in: boolean whether the number is in fibonacci sequence or not
        """
        biggest_number = max(self.possible_answers)
        fibonacci_numbers = set(find_fibonacci_numbers(biggest_number + 1))
        self.possible_answers = self.possible_answers & fibonacci_numbers if is_in \
            else self.possible_answers - fibonacci_numbers

    def deal_with_catalan_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all catalan numbers.

        Call find_catalan_numbers to get all catalan numbers in range.
        :param is_in: boolean whether the number is in catalan sequence or not
        """
        biggest_number = max(self.possible_answers)
        catalan_numbers = set(find_catalan_numbers(biggest_number + 1))
        self.possible_answers = self.possible_answers & catalan_numbers if is_in \
            else self.possible_answers - catalan_numbers

    def deal_with_number_order(self, increasing: bool, to_be: bool):
        """
        Filter possible answers to either keep or remove all numbers with wrong order.

        :param increasing: boolean whether to check is in increasing or decreasing order
        :param to_be: boolean whether the number is indeed in that order
        """
        pass


def normalize_quadratic_equation(equation: str) -> str:
    """
    Normalize the quadratic equation.

    normalize_quadratic_equation("x2 + 2x = 3") => "x2 + 2x - 3 = 0"
    normalize_quadratic_equation("0 = 3 + 1x2") => "x2 + 3 = 0"
    normalize_quadratic_equation("2x + 2 = 2x2") => "2x2 - 2x - 2 = 0"
    normalize_quadratic_equation("0x2 - 2x = 1") => "2x + 1 = 0"
    normalize_quadratic_equation("0x2 - 2x = 1") => "2x + 1 = 0"
    normalize_quadratic_equation("2x2 + 3x - 4 + 0x2 - x1 + 0x1 + 12 - 12x2 = 4x2 + x1 - 2") => "14x2 - x - 10 = 0"

    :param equation: quadratic equation to be normalized
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return: normalized equation
    """
    pass


def quadratic_equation_solver(equation: str) -> Union[None, float, tuple]:
    """
    Solve the normalized quadratic equation.

    :param str: quadratic equation
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return:
    if there are no solutions, return None.
    if there is exactly 1 solution, return it.
    if there are 2 solutions, return them in a tuple, where smaller is first
    all numbers are returned as floats.
    """
    pass


def find_primes_in_range(biggest_number: int) -> list:
    """
    Find all primes in range(end inclusive).

    :param biggest_number: all primes in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    :return: list of primes
    """
    if biggest_number < 2:
        return []

    primes = []

    for num in range(2, biggest_number + 1):
        is_prime = True  # Assume num is prime until proven otherwise.
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break  # If a divisor is found, num is not prime.

        if is_prime:
            primes.append(num)  # If no divisors were found, num is prime.

    return primes


def find_composites_in_range(biggest_number: int) -> list:
    """
    Find all composites in range(end inclusive).

    Call find_primes_in_range from this method to get all composites
    :return: list of composites
    :param biggest_number: all composites in range of biggest_number(included)
    """
    if biggest_number < 2:
        return []

    primes = find_primes_in_range(biggest_number)
    composites = [num for num in range(2, biggest_number + 1) if num not in primes]

    return composites


def find_fibonacci_numbers(biggest_number: int) -> list:
    """
    Find all Fibonacci numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all fibonacci numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Fibonacci_number
    :return: list of fibonacci numbers
    """
    fibonacci_numbers = []

    a, b = 0, 1
    while a <= biggest_number:
        fibonacci_numbers.append(a)
        a, b = b, a + b


def find_catalan_numbers(biggest_number: int) -> list:
    """
    Find all Catalan numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all catalan numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Catalan_number
    :return: list of catalan numbers
    """

    def catalan_number(n):
        if n <= 1:
            return 1
        res = 0
        for i in range(n):
            res += catalan_number(i) * catalan_number(n - 1 - i)
        return res

    catalan_numbers = []
    for i in range(biggest_number + 1):
        catalan_numbers.append(catalan_number(i))

    return catalan_numbers
