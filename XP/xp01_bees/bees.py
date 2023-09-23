"""Whether bees meet."""


def do_bees_meet(honeycomb_width: int, honeyhopper_data: str, pollenpaddle_data: str) -> bool:
    """Given honeycomb structure and bees' datas, return True if the two bees land on the same hex, otherwise False.

    :param honeycomb_width: length of the honeycomb cell side (number of cells at the side)
    :param honeyhopper_data: honeyhopper bee positions as words, separated by a comma (no spaces)
    :param pollenpaddle_data: pollenpaddle bee positions as words, separated by a comma (no spaces)
    :return: validation
    """
    # Number of hexes
    TOTAL_HEXES: int = 1 + 3 * (honeycomb_width - 1) * honeycomb_width

    # Check for errors in input.
    if honeycomb_width <= 0 or len(honeyhopper_data.split(',')) < 4 or len(pollenpaddle_data.split(',')) < 4:
        raise ValueError("Insufficient data for sequence identification")

    'Defining helper functions.'

    def honeyhopper_new_position(overall_position: int) -> int:
        """Generates honeyhopper position."""
        current_hex = overall_position % TOTAL_HEXES
        if current_hex == 0:
            current_hex = TOTAL_HEXES
        return current_hex

    def pollenpaddle_new_position(overall_position: int) -> int:
        """Generates pollenpaddle position."""
        current_hex = int(TOTAL_HEXES + 1 - (overall_position % TOTAL_HEXES))
        if current_hex == TOTAL_HEXES + 1:
            return 1
        else:
            return current_hex

    def constant_increase(differences, data_list):
        """Makes constantly increasing data list."""
        new_data_list = data_list[:4]
        i = 3
        while i < 100000:
            new_data_list.append(new_data_list[i] + differences[0])
            i += 1

        return new_data_list

    def arithmetic_increase(differences, data_list):
        """Makes arithmetically increasing data list."""
        increment = differences[1] - differences[0]
        new_data_list = data_list[:4]
        i = 3
        while i < 100000:
            last_step = new_data_list[i] - new_data_list[i - 1]
            new_data_list.append(new_data_list[i] + last_step + increment)
            i += 1

        return new_data_list

    def geometric_increase(multiplier, data_list):
        """Makes geometrically increasing data list."""
        multiplier = int(multiplier)
        new_data_list = data_list
        i = 3
        while i < 100:
            new_value = new_data_list[i] * multiplier
            new_data_list.append(int(new_value))
            i += 1

        return new_data_list

    def geometric_step(differences, data_list):
        """Makes geometrically increasing step data list."""
        multiplier = differences[1] // differences[0]
        new_data_list = data_list[:4]
        i = 3
        while i < 100:
            last_step = new_data_list[i] - new_data_list[i - 1]
            new_value = new_data_list[i] + last_step * multiplier
            new_data_list.append(int(new_value))
            i += 1

        return new_data_list

    def calculate_complete_bee_data(bee_data: str) -> list[int]:
        """Evaluates list type and returns a larger list."""
        # Recycle out the numbers.
        data_list = [int(num) for num in bee_data.split(',')]

        # Find the differences.
        differences = [data_list[i + 1] - data_list[i] for i in range(3)]

        # Check for constant:
        if all(diff == differences[0] for diff in differences):
            return constant_increase(differences, data_list[:4])

        # Check for arithmetic increase:
        if differences[2] - differences[1] == differences[0]:
            return arithmetic_increase(differences, data_list)

        # Find the ratios.
        ratios = [data_list[i + 1] / data_list[i] for i in range(3)]

        # Check for geometrical increase:
        if all(ratio == ratios[0] for ratio in ratios):
            return geometric_increase(ratios[0], data_list[:4])

        # Check for geometric step:
        for diff in differences:
            if diff == 0:
                raise ValueError("Insufficient data for sequence identification")

        if differences[2] / (differences[1] / differences[0]) == data_list[2]:
            return geometric_step(differences, data_list[:4])

        raise ValueError("Insufficient data for sequence identification")

    'Function that simulates bees movement.'

    def simulation(honeyhopper, pollenpaddle) -> bool:
        """Simulates the process and returns the answer."""
        for pos1, pos2 in zip(honeyhopper, pollenpaddle):
            if honeyhopper_new_position(pos1) == pollenpaddle_new_position(pos2):
                return True
            else:
                continue

        return False

    # Calling the simulation function.
    return simulation(calculate_complete_bee_data(honeyhopper_data), calculate_complete_bee_data(pollenpaddle_data))


if __name__ == '__main__':
    print(do_bees_meet(50, "1,2,3,4,5", "1,2,4,8,16"))
    sequence_1 = ",".join(str(x) for x in range(50000, 200001, 10000))  # Arithmetic sequence with a large difference.
    sequence_2 = ",".join(str(2 ** x) for x in range(30, 45))  # Geometric sequence with a ratio of 2, but starting
    # from a larger power.
    print(do_bees_meet(300, sequence_1, sequence_2))  # TRUE
    print(do_bees_meet(61, "1,2,3,4", "1,2,3,4"))  # True.
