import pytest
import utils_math


@pytest.mark.parametrize("x, y, expected", [(5, 10, 10),
                                            (11, 1, 11)])
def test_compare(x, y, expected):
    assert utils_math.compare(x, y) == expected


@pytest.fixture
def five():
    return 5


def test_exception_compare(five):
    with pytest.raises(Exception):
        utils_math.compare(five, five)


@pytest.mark.parametrize("x, expected", [(9, True),
                                         (2, False)])
def test_three_multiple(x, expected):
    assert utils_math.three_multiple(x) == expected


@pytest.mark.parametrize("a, n, expected", [(2, 3, 8),
                                            (5, 3, 125),
                                            (0, 0, 1)])
def test_power(a, n, expected):
    assert utils_math.power(a, n) == expected
