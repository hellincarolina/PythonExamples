import pytest
from intersperse_list import calc_min_permutations


@pytest.mark.parametrize('coins_flips, expected_error', [
    (["a", 1], "List contains invalid values"),
    ([1.0, 0], "List contains invalid values"),
    ([1, 0, 1, 0, 0, 0], "List cannot be fully interspersed"),
    ([0, 0, 0], "List cannot be fully interspersed"),
    ([1, 1, 1], "List cannot be fully interspersed"),
    ([1], "List cannot be fully interspersed"),
    ([0, 1, 0, 9], "List contains invalid values"),
    ([], "Empty List"),
    ([0, 1, 0, 1, 1], "No more value can be used to get the list fully interspersed"),
])
def test_invalid_values(coins_flips, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        assert calc_min_permutations(coins_flips)


def test_no_list_argument():
    with pytest.raises(TypeError):
        assert calc_min_permutations("11")


def test_none_list():
    with pytest.raises(TypeError):
        assert calc_min_permutations(None)


def test_already_ordered_list():
    assert calc_min_permutations([1, 0, 1, 0, 1]) == 0


@pytest.mark.parametrize('coins_flips, expected_value', [
    ([1, 1, 0, 1, 0, 1, 0], 3),
    ([0, 1, 0, 1], 0),
    ([1, 1, 0, 0], 1),
    ([1, 1, 1, 0, 0, 0], 1),
    ([1, 0, 0, 1, 1, 1, 0], 2)
])
def test_interspersed_list(coins_flips, expected_value):
    assert calc_min_permutations(coins_flips) == expected_value
