"""Entry."""
import re


def parse(row: str) -> tuple:
    """
    Parse string row into a tuple.

    The row has a first name, last name, ID code, phone number, date of birth and address.
    Only ID code is mandatory, other values may not be included.

    They can be found by the following rules:
    - Both the first name and last name begin with a capital letter and are followed by a lowercase letter
    - ID code is an 11-digit number
    - Phone number has the same rules applied as in the previous task
    - Date of birth is in the form of dd-MM-YYYY
    - Address is everything else that's left

    :param row: given string to find values from
    :return: tuple of values found in given string
    """
    pattern = r'([A-Z][a-z]+)?([A-Z][a-z]+)?(\d{11})(\+\d{3}\s\d{7,8})?(\d{2}\-\d{2}\-\d{4})?(.+)?'
    match = re.search(pattern, row)

    return match[1], match[2], match[3], match[4], match[5], match[6]


if __name__ == '__main__':
    print(parse('PriitPann39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', '+372 56887364', '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # (None, None, '39712047623', '+372 56887364', '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('PriitPann3971204762302-12-1998Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', None, '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('PriitPann39712047623+372 56887364Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', '+372 56887364', None, 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('39712047623'))
    # (None, None, '39712047623', None, None, None)
