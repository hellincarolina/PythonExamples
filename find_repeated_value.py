def find_repeated_value(vector1, vector2):
    """
    Given two vectors this function returns the first value in vector1 that is contained in vector2 as well

    :param vector1: list of integers
    :param vector2: list of integers to find the value that is contained in the first list
    :return: first value contained in both
    :raises: TypeError if one (or both) of the arguments is not a list
             ValueError if one of the list contains not integer values
    """
    if not isinstance(vector1, list) or not isinstance(vector2, list):
        raise TypeError("Argument is not a list")
    if not all(isinstance(i, int) for i in vector1):
        raise ValueError("Vector 1 contains not integer values")
    if not all(isinstance(i, int) for i in vector2):
        raise ValueError("Vector 2 contains not integer values")
    for value1 in vector1:
        try:
            return value1
        except ValueError as e:
            continue
    return None
