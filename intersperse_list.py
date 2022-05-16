first_call = True


def get_first_invalid_position(coin_flips, starting_with, value_to_find):
    """
    In a list of expected interspersed values, this function finds the index of the first invalid position
    e.g. Given this list: [0, 1, 1, 0] get the first invalid 1. The expected result is 2
    :param coin_flips: list of values to be evaluated
    :param starting_with: expected starting value in the list
    :param value_to_find: value to be evaluated
    :return: index of the first invalid ocurrence of the value_to_find
    """
    index = 0
    last_index = 0
    if coin_flips.count(value_to_find) == 0:
        return None
    expected_value = starting_with
    for value in coin_flips:
        if value != expected_value and value == value_to_find:
            return index
        else:
            if value == value_to_find:
                last_index = index
            expected_value = int(not expected_value)
            index = index + 1
    return last_index


def calc_min_permutations(coin_flips, start_with=None):
    """
    Returns the minimum changes to be done on a sequence of coin flips (0 is tails, 1 is heads) to get an interspersed
    sequence
    :param coin_flips: list of sequence of coin flips
    :param start_with: The expected value to start the sequence, if it does not matter this value is supposed to be None
    :return: the minimum quantity of permutations to be done
    :raises: TypeError if the argument is not a list
             ValueError if the argument is an empty list, the argument is list with invalid values (different than 0
             and 1), or it's not possible to fully intersperse the list.
    """
    global first_call
    if first_call:
        if not isinstance(coin_flips, list):
            raise TypeError("Argument is not a list")
        if not coin_flips:
            raise ValueError("Empty List")
        if not all(i in [0, 1] for i in coin_flips):
            raise ValueError("List contains invalid values")
        if not all(isinstance(i, int) for i in coin_flips):
            raise ValueError("List contains invalid values")
        zeros_qty = coin_flips.count(0)
        ones_qty = coin_flips.count(1)
        if len(coin_flips) == 1 or zeros_qty > ones_qty + 1 or ones_qty > zeros_qty + 1:
            raise ValueError("List cannot be fully interspersed")
        first_call = False
    if start_with is None:
        head = coin_flips[0]
        coin_flips.pop(0)
        if len(coin_flips) > 0:
            return calc_min_permutations(coin_flips, int(not head))
        else:
            first_call = True
            raise ValueError("No value can be used to get the list fully interspersed")
    else:
        if coin_flips[0] == start_with:
            coin_flips.pop(0)
            if len(coin_flips) > 0:
                return calc_min_permutations(coin_flips, int(not start_with))
            else:
                first_call = True
                return 0
        else:
            try:
                head = coin_flips[0]
                coin_flips.pop(0)
                index_pos = get_first_invalid_position(coin_flips, int(not start_with), start_with)
                if index_pos is None:
                    index_pos = coin_flips.index(start_with)
                coin_flips[index_pos] = int(not start_with)
                return 1 + calc_min_permutations(coin_flips, int(not start_with))
            except ValueError as e:
                first_call = True
                raise ValueError("No more value can be used to get the list fully interspersed")

