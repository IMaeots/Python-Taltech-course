"""Secret letter."""


def secret_letter(letter: str) -> bool:
    """
    Check if the given secret letter follows all the necessary rules. Return True if it does, else False.

    Rules:
    1. The letter has more uppercase letters than lowercase letters.
    2. The sum of digits in the letter has to be equal to or less than the amount of uppercase letters.
    3. The sum of digits in the letter has to be equal to or more than the amount of lowercase letters.

    :param letter: secret letter
    :return: validation
    """
    uppercase_letters = 0
    lowercase_letters = 0
    sum_of_digits = 0

    for character in letter:
        if character.isupper():
            uppercase_letters += 1
        elif character.islower():
            lowercase_letters += 1
        elif character.isdigit():
            sum_of_digits += int(character)

    return uppercase_letters > lowercase_letters and uppercase_letters >= sum_of_digits >= lowercase_letters


if __name__ == '__main__':
    print(secret_letter("sOMEteSTLETTer8"))  # True
    print(secret_letter("thisisNOTvaliD4"))  # False
    print(secret_letter("TOOMANYnumbers99"))  # False
    print(secret_letter("anotherVALIDLETTER17"))  # True
    print(secret_letter("CANBENOLOWERCASENODIGITS"))  # True
