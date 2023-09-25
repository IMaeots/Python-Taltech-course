"""Whether bees meet."""

'Define helper functions for do_bees_meet.'


def error():
    """Raise value error."""
    raise ValueError("Insufficient data for sequence identification")


def check_input(honeyhopper_data, pollenpaddle_data, honeycomb_width):
    """Check input for errors."""
    if honeyhopper_data is not str or pollenpaddle_data is not str:
        error()

    honeyhopper_numeric_data = honeyhopper_data.split(',')
    pollenpaddle_numeric_data = pollenpaddle_data.split(',')
    if honeycomb_width <= 0 or len(honeyhopper_numeric_data) < 4 or len(pollenpaddle_numeric_data) < 4:
        error()


def honeyhopper_new_position(overall_position: int, TOTAL_HEXES) -> int:
    """Generate honeyhopper position."""
    current_hex = overall_position % TOTAL_HEXES
    if current_hex == 0:
        current_hex = TOTAL_HEXES
    return current_hex


def pollenpaddle_new_position(overall_position: int, TOTAL_HEXES) -> int:
    """Generate pollenpaddle position."""
    current_hex = int(TOTAL_HEXES + 1 - (overall_position % TOTAL_HEXES))
    if current_hex == TOTAL_HEXES + 1:
        return 1
    else:
        return current_hex


def constant_increase(differences, data_list):
    """Make constantly increasing data list."""
    new_data_list = data_list[:4]
    i = 3
    while i < 100000:
        new_data_list.append(new_data_list[i] + differences[0])
        i += 1

    return new_data_list


def arithmetic_increase(differences, data_list):
    """Make arithmetically increasing data list."""
    increment = differences[1] - differences[0]
    new_data_list = data_list[:4]
    i = 3
    while i < 100000:
        last_step = new_data_list[i] - new_data_list[i - 1]
        new_data_list.append(new_data_list[i] + last_step + increment)
        i += 1

    return new_data_list


def geometric_increase(multiplier, data_list):
    """Make geometrically increasing data list."""
    multiplier = int(multiplier)
    new_data_list = data_list
    i = 3
    while i < 35000:
        new_value = new_data_list[i] * multiplier
        new_data_list.append(new_value)
        i += 1

    return new_data_list


def geometric_step(differences, data_list):
    """Make geometrically increasing step data list."""
    multiplier = differences[1] // differences[0]
    new_data_list = data_list[:4]
    i = 3
    while i < 10000:
        last_step = new_data_list[i] - new_data_list[i - 1]
        new_value = new_data_list[i] + last_step * multiplier
        new_data_list.append(int(new_value))
        i += 1

    return new_data_list


def calculate_complete_bee_data(bee_data: str) -> list[int]:
    """Evaluate list type and return a larger list."""
    # Recycle out the numbers.
    data_list = [abs(int(num)) for num in bee_data.split(',')]

    # Find the differences.
    differences = [abs(int(data_list[i + 1] - data_list[i])) for i in range(3)]

    # Check for constant:
    if all(diff == differences[0] for diff in differences):
        return constant_increase(differences, data_list[:4])

    # Check for arithmetic increase:
    if differences[2] - differences[1] == differences[1] - differences[0]:
        return arithmetic_increase(differences, data_list)

    # Find the ratios.
    ratios = [data_list[i + 1] // data_list[i] if data_list[i] != 0 else error() for i in range(3)]

    # Check for geometrical increase:
    if all(ratio == ratios[0] for ratio in ratios):
        return geometric_increase(ratios[1], data_list[:4])

    # Check for geometric step:
    try:
        if ((data_list[3] - data_list[2]) // (data_list[1] - data_list[0])) == differences[1]:
            return geometric_step(differences, data_list[:4])
    except ZeroDivisionError:
        error()
    error()


def simulation(honeyhopper, pollenpaddle, TOTAL_HEXES) -> bool:
    """Simulate the process and return the answer."""
    for pos1, pos2 in zip(honeyhopper, pollenpaddle):
        honey_new_pos = honeyhopper_new_position(pos1, TOTAL_HEXES)
        pollen_new_pos = pollenpaddle_new_position(pos2, TOTAL_HEXES)
        if honey_new_pos == pollen_new_pos:
            return True
        else:
            continue

    return False


def do_bees_meet(honeycomb_width: int, honeyhopper_data: str, pollenpaddle_data: str) -> bool:
    """Given honeycomb structure and bees' datas, return True if the two bees land on the same hex, otherwise False.

    :param honeycomb_width: length of the honeycomb cell side (number of cells at the side)
    :param honeyhopper_data: honeyhopper bee positions as words, separated by a comma (no spaces)
    :param pollenpaddle_data: pollenpaddle bee positions as words, separated by a comma (no spaces)
    :return: validation
    """
    # Number of hexes.
    TOTAL_HEXES: int = 1 + 3 * (honeycomb_width - 1) * honeycomb_width

    # Check for errors.
    check_input(honeyhopper_data, pollenpaddle_data, honeycomb_width)

    # Calling the simulation function.
    return simulation(calculate_complete_bee_data(honeyhopper_data), calculate_complete_bee_data(pollenpaddle_data),
                      TOTAL_HEXES)


if __name__ == '__main__':
    print(do_bees_meet(61, "2,4,2,1", "0,1,2,3"))
    print(do_bees_meet(61, "1,1,2,4", "1,2,4,8"))  # Growing arithmetic and random.
    print(do_bees_meet(61, "2,6,12,20", "1,2,4,8"))  # Negative and random.
    print(do_bees_meet(1212, "5,12,21,32", "1,2,4,8"))  # large width i guess.
    print(do_bees_meet(5, "1,3,7,15", "1,1,1,1"))  # True
    print(do_bees_meet(50, "1,2,3,4,5", "1,2,4,8,16"))
    sequence_1 = ",".join(str(x) for x in range(50000, 200001, 10000))  # Arithmetic sequence with a large difference.
    sequence_2 = ",".join(str(2 ** x) for x in range(30, 45))  # Geometric sequence with a ratio of 2, but starting
    # from a larger power.
    print(do_bees_meet(30, sequence_1, sequence_2))  # TRUE
    print(do_bees_meet(61, "1,2,3,4", "1,2,3,4"))  # True.
    print(do_bees_meet(1029, "1,3,5,7", "1,3,9,27"))
    assert do_bees_meet(5, "1,3,7,15", "1,1,1,1") is True
