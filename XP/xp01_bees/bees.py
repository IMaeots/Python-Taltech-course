"""Whether bees meet."""


def do_bees_meet(honeycomb_width: int, honeyhopper_data: str, pollenpaddle_data: str) -> bool:
    """
    Given honeycomb structure and bees' datas, return True if the two bees land on the same hex at some point, \\
     otherwise False.

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

    """Defining helper functions."""
    def honeyhopper_new_position(overall_position: int) -> int:
        current_hex = overall_position % TOTAL_HEXES
        if current_hex == 0:
            current_hex = TOTAL_HEXES
        return current_hex

    def pollenpaddle_new_position(overall_position: int) -> int:
        current_hex: int = TOTAL_HEXES + 1 - (overall_position % TOTAL_HEXES)
        if current_hex == TOTAL_HEXES + 1:
            return 1
        else:
            return current_hex

    def calculate_complete_bee_data(bee_data: str) -> list[int]:
        # Recycle out the numbers
        data_list = [int(num) for num in bee_data.split(',')]

        # Find the differences
        differences = [data_list[i + 1] - data_list[i] for i in range(3)]

        # Check for constant:
        if all(diff == differences[0] for diff in differences):
            # Constant: (hüpete vahel on konstantne vahe).
            new_data_list = data_list[:4]
            i = 3
            while i < 100000:
                new_data_list.append(new_data_list[i] + differences[0])
                i += 1

            return new_data_list

        # Check for arithmetic:
        # Arithmetic increase: (hüpete vahel on ühtlaselt suurenev vahe.) (1,2,4,7) - kordaja suureneb mingi arv võrra
        # TODO

        # Check for geometrical increase and geometrical step distance:
        # Geometric progression (positsioonid moodustavad gemoeetrilise jada.) (1,2,4,8) - sama kordaja
        #ratios = [data_list[i + 1] / data_list[i] for i in range(3)]
        #if all(ratio == ratios[0] for ratio in ratios):
        #    step = int(data_list[1] / data_list[2])
        #    return

        # Check for geometric step:
        # (hüpete vahe suureneb geomeetrilise jada võrra.) (1,3,7,15) - kordaja suureneb mingi arv korda
        # TODO

        return data_list

    """Function that simulates bees movement."""
    def simulation(honeyhopper, pollenpaddle) -> bool:
        for pos1, pos2 in zip(honeyhopper, pollenpaddle):
            if honeyhopper_new_position(pos1) == pollenpaddle_new_position(pos2):
                return True
            else:
                continue

        return False

    # Calling the simulation function
    return simulation(calculate_complete_bee_data(honeyhopper_data), calculate_complete_bee_data(pollenpaddle_data))


if __name__ == '__main__':
    print(do_bees_meet(50, "1,2,3,4,5", "1,2,4,8,16"))
