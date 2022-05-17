import pytest
from find_repeated_value import find_repeated_value


@pytest.mark.parametrize('vector1, vector2, expected_value', [
    ([1, 2, 3], [9, 3, 1], 1),
    ([1, 3, 5], [1, 2, 1, 6], 1),
    ([100, 30, 15], [5, 15, 30], 30),
    ([100, 30, 15, 40], [40, 15, 30], 30),
    ([], [1, 2, 3], None),
    ([], [], None),
    ([1, 2, 4], [], None),
    ([1], [3], None),
    ([1], [1], 1),
    ([-3, 1, 5], [7, -3, 0], -3),
    ([-100], [100], None),
    ([1+2, 0], [3],3),
    ([0x12AF], [0x12AF], 4783),
    ([0o1267], [0o1267], 695),
    ([0b10], [0b10], 2),
])
def test_get_first_repeated(vector1, vector2, expected_value):
    assert find_repeated_value(vector1, vector2) == expected_value


@pytest.mark.parametrize('value1, value2, expected_error', [
    (["a", 3, 6], [9, 3, 1], "Vector 1 contains not integer values"),
    ([1, 3], [1.0, 2], "Vector 2 contains not integer values"),

])
def test_invalid_data_type(value1, value2, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        assert find_repeated_value(value1, value2)


@pytest.mark.parametrize('value1, value2', [
    (None, [9, 3, 1]),
    ([1,2,3], None),
    (None, None),
    ("invalid vector", [1, 2, 3]),
    ([1, 2, 3], "invalid vector"),
])
def test_no_list_arguments(value1, value2):
    with pytest.raises(TypeError, match="Argument is not a list"):
        assert find_repeated_value(value1, value2)
