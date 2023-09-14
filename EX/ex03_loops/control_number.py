"""Control number."""


def control_number(encrypted_string: str) -> bool:
    """
    Given encrypted string that has a control number in the end of it, return True if correct, else False.

    Calculating the correct control number:
    1. Start the calculation from 0.
    2. Add 1 for every lowercase occurrence.
    3. Add 2 for every uppercase occurrence.
    4. Add 5 for any of the following symbol occurrences: "?!@#".
    Other symbols/letters/digits don't affect the result.

    NB! If for example the number you come up with is 25, you only have to check the last two digits of the string.
    e.g. control_number("?!?!#4525") -> True, because it ends with 25.

    :param encrypted_string: encrypted string
    :return: validation
    """
    encryption_number = 0

    for i in encrypted_string:
        if i.islower():
            encryption_number += 1
        elif i.isupper():
            encryption_number += 2
        elif i in ['!', '?', '@', '#']:
            encryption_number += 5

    return encrypted_string.endswith(str(encryption_number))


if __name__ == '__main__':
    print(control_number("mE0W5"))  # True
    print(control_number("SomeControlNR?20"))  # False
    print(control_number("False?Nr9"))  # False
    print(control_number("#Hello?!?26"))  # True
    print(control_number("3423982340000000.....///....0"))  # True
    print(control_number("#Shift6"))  # False
