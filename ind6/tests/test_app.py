import pytest

from ind6.app import add, is_even


def test_add_simple():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -5) == -6


def test_add_mixed():
    assert add(-3, 7) == 4


@pytest.mark.parametrize("value, expected", [
    (2, True),
    (3, False),
    (10, True),
    (15, False),
])
def test_is_even(value, expected):
    assert is_even(value) == expected


@pytest.fixture
def sample_numbers():
    return [2, 4, 6]


def test_all_even(sample_numbers):
    for n in sample_numbers:
        assert is_even(n)
