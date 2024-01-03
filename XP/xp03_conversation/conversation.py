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
        self.biggest_number = biggest_number
        self.possible_answers = set([all_possible_answers for all_possible_answers in range(biggest_number + 1)])

    def decision_branch(self, sentence: str):
        """
        Regex can and should be used here.

        :param sentence: sentence to solve
        call one of the functions bellow (within this class) and return either one of the following strings:
        f"Possible answers are {sorted_list_of_possible_answers_in_growing_sequence)}." if there are multiple possibilities
        f"The number I needed to guess was {final_answer}." if the result is certain
        """
        if sentence:
            return f"Possible answers are {sorted(self.possible_answers)}."
        else:
            return f"The number I needed to guess was {self.biggest_number}."

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
        prime_numbers = set(find_primes_in_range(self.biggest_number))

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
            if decimal_value in str(num):
                possible_answers.add(num)

        self.possible_answers = possible_answers

    def deal_with_hex_value(self, hex_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param hex_value: hex value within the number like e in fe2
        """
        possible_answers = set()

        for num in self.possible_answers:
            if hex_value in str(num):
                possible_answers.add(num)

        self.possible_answers = possible_answers

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
        x1, x2 = quadratic_equation_solver(equation)

        result = x1 if is_bigger else x2

        result = result * multiplicative if to_multiply else result / multiplicative

        self.deal_with_dec_value(result)

    def deal_with_fibonacci_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all fibonacci numbers.

        Call find_fibonacci_numbers to get all fibonacci numbers in range.
        :param is_in: boolean whether the number is in fibonacci sequence or not
        """
        fibonacci_numbers = set(find_fibonacci_numbers(self.biggest_number))
        self.possible_answers = self.possible_answers & fibonacci_numbers if is_in \
            else self.possible_answers - fibonacci_numbers

    def deal_with_catalan_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all catalan numbers.

        Call find_catalan_numbers to get all catalan numbers in range.
        :param is_in: boolean whether the number is in catalan sequence or not
        """
        catalan_numbers = set(find_catalan_numbers(self.biggest_number))
        self.possible_answers = self.possible_answers & catalan_numbers if is_in \
            else self.possible_answers - catalan_numbers

    def deal_with_number_order(self, increasing: bool, to_be: bool):
        """
        Filter possible answers to either keep or remove all numbers with wrong order.

        :param increasing: boolean whether to check is in increasing or decreasing order
        :param to_be: boolean whether the number is indeed in that order
        """
        if increasing:
            if to_be:
                self.possible_answers = [num for num in self.possible_answers if
                                         all(x < y for x, y in zip(num, num[1:]))]
            else:
                self.possible_answers = [num for num in self.possible_answers if
                                         any(x >= y for x, y in zip(num, num[1:]))]
        else:
            if to_be:
                self.possible_answers = [num for num in self.possible_answers if
                                         all(x > y for x, y in zip(num, num[1:]))]
            else:
                self.possible_answers = [num for num in self.possible_answers if
                                         any(x <= y for x, y in zip(num, num[1:]))]


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
    equation = equation.replace(" ", "")

    # Pattern to match coefficients and terms
    pattern = r'([-+]?\d*)x(\d*)'

    # Find all matches for the pattern
    matches = re.findall(pattern, equation)

    # Initialize coefficients for x^2, x, and constant term
    a = 0
    b = 0
    c = 0

    for match in matches:
        coef, power = match
        coef = int(coef) if coef else 1
        power = int(power) if power else 1

        if power == 2:
            a += coef
        elif power == 1:
            b += coef
        else:
            c += coef

    # Construct the normalized equation
    normalized_eq = f"{a}x^2" if a != 0 else ""
    normalized_eq += f" + {b}x" if b != 0 else ""
    normalized_eq += f" + {c}" if c != 0 else ""
    normalized_eq += " = 0" if normalized_eq else "0 = 0"

    return normalized_eq


def extract_coefficients(normalized_eq: str) -> tuple:
    """
    Extract coefficients a, b, and c from the normalized quadratic equation.

    :param normalized_eq: normalized quadratic equation
    :return: coefficients a, b, c as integers
    """
    parts = re.split(r'\s*[+-]\s*', normalized_eq.split('=')[0])
    a = 0
    b = 0
    c = 0

    for part in parts:
        if "x^2" in part:
            a += int(part.replace("x^2", ""))
        elif "x" in part:
            b += int(part.replace("x", ""))
        else:
            c += int(part)

    return a, b, c


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
    a, b, c = extract_coefficients(normalize_quadratic_equation(equation))
    disc = b**2 - 4 * a * c
    if disc < 0:
        return None
    elif disc == 0:
        return -b / (2 * a)
    else:
        solution1 = (-b + math.sqrt(disc)) / (2 * a)
        solution2 = (-b - math.sqrt(disc)) / (2 * a)

    return min(solution1, solution2), max(solution1, solution2)


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

    return fibonacci_numbers


def find_catalan_numbers(biggest_number: int) -> list:
    """
    Find all Catalan numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all catalan numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Catalan_number
    :return: list of catalan numbers
    """
    memo = {}  # Memoization dictionary to store calculated values

    def catalan_number(n):
        if n <= 1:
            return 1

        if n not in memo:
            res = 0
            for i in range(n):
                res += catalan_number(i) * catalan_number(n - 1 - i)
            memo[n] = res

        return memo[n]

    catalan_numbers = []
    for i in range(biggest_number + 1):
        catalan_numbers.append(catalan_number(i))

    return catalan_numbers
