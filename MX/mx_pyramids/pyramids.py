"""Some cool pyramids."""


def create_simple_pyramid_left(height: int) -> str:
    """
    Create simple pyramid on the left side.

    Use recursion!

    create_simple_pyramid_left(4) => *
                                     **
                                     ***
                                     ****

    :param height: Pyramid height.
    :return: Pyramid.
    """
    if height <= 0:
        return ''

    return create_simple_pyramid_left(height - 1) + '*' * height + '\n'


def create_simple_pyramid_right(height: int, current=1) -> str:
    """
    Create simple pyramid on the right side.

    Use recursion!

    create_simple_pyramid_right(4) =>   *
                                       **
                                      ***
                                     ****

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ''

    room = ' ' * (height - current)
    stars = '*' * current
    row = room + stars + '\n'

    return row + create_simple_pyramid_right(height, current + 1)


def create_number_pyramid_left(height: int, current=1) -> str:
    """
    Create left-aligned number pyramid.

    Use recursion!

    create_number_pyramid_left(4) => 1
                                     12
                                     123
                                     1234

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ''

    row = ''
    for num in range(1, height + 2 - current):
        row += str(num)
    return create_number_pyramid_left(height, current + 1) + row + '\n'


def create_number_pyramid_right(height: int, current=1) -> str:
    """
    Create right-aligned number pyramid.

    Use recursion!

    create_number_pyramid_right(4) =>    1
                                        21
                                       321
                                      4321

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ''

    spaces = ' ' * (height - current)
    row = ''.join(str(i) for i in range(current, 0, -1))
    return spaces + row + '\n' + create_number_pyramid_right(height, current + 1)


def create_number_pyramid_left_down(height: int, current=1) -> str:
    """
    Create left-aligned number pyramid upside-down.

    Use recursion!

    create_number_pyramid_left(4) => 4321
                                     321
                                     21
                                     1

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ''

    row = ''.join(str(i) for i in range(current, 0, -1))
    return create_number_pyramid_left_down(height, current + 1) + row + '\n'


def create_number_pyramid_right_down(height: int, current=1) -> str:
    """
    Create right-aligned number pyramid upside-down.

    Use recursion!

    create_number_pyramid_right(4) => 1234
                                       123
                                        12
                                         1

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ''

    spaces = ' ' * (height - current)
    row = ''.join(str(i) for i in range(1, current + 1))
    return create_number_pyramid_right_down(height, current + 1) + spaces + row + '\n'


def create_regular_pyramid(height: int, current=1) -> str:
    """
    Create regular pyramid.

    Use recursion!

    create_regular_pyramid(4) =>    *
                                   ***
                                  *****
                                 *******

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ''

    spaces = ' ' * (height - current)
    row = '*' * (2 * current - 1)
    return spaces + row + '\n' + create_regular_pyramid(height, current + 1)


def create_regular_pyramid_upside_down(height: int, current=1) -> str:
    """
    Create regular pyramid upside down.

    Use recursion!

    create_regular_pyramid_upside_down(4) => *******
                                              *****
                                               ***
                                                *

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ''

    spaces = ' ' * (height - current)
    row = '*' * (2 * current - 1)
    return create_regular_pyramid_upside_down(height, current + 1) + spaces + row + '\n'


def create_diamond(height: int, current=1) -> str:
    """
    Create diamond.

    Use recursion!

    create_diamond(4) =>    *
                           ***
                          *****
                         *******
                         *******
                          *****
                           ***
                            *

    :param height: Height of half of the diamond.
    :param current: Keeping track of current layer.
    :return: Diamond.
    """
    if current > height * 2:
        return ''

    spaces = ' ' * abs(height - current)

    if current < height:
        row = '*' * (2 * current - 1)
    elif current == height:
        row = '*' * (height * 2 - 1) + '\n' + '*' * (height * 2 - 1)
    else:
        row = '*' * (2 * (height * 2 - current) - 1)

    if current == height * 2:
        return row  # No newline for the last row

    return create_diamond(height, current + 1) + spaces + row + '\n'


def create_empty_pyramid(height: int, current=1) -> str:
    """
    Create empty pyramid.

    Use recursion!

    create_empty_pyramid(4) =>    *
                                 * *
                                *   *
                               *******

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ''

    spaces = ' ' * (height - current)

    if current == 1 or current == height:
        row = '*' * (2 * current - 1)
    else:
        row = '*' + ' ' * (2 * current - 3) + '*'

    return spaces + row + '\n' + create_empty_pyramid(height, current + 1)


if __name__ == '__main__':
    print(create_simple_pyramid_left(4))
    print(create_simple_pyramid_right(4))
    print(create_number_pyramid_left(4))
    print(create_number_pyramid_right(4))
    print(create_number_pyramid_left_down(4))
    print(create_number_pyramid_right_down(4))
    print(create_regular_pyramid(4))
    print(create_regular_pyramid_upside_down(4))
    print(create_diamond(4))
    print(create_empty_pyramid(4))
