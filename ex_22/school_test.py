import pytest
import school


@pytest.mark.average
def test_average_calculate():
    assert school.average_calculate(70, 85, 90, 95) == 85


@pytest.fixture
def five():
    return 5


@pytest.mark.bonus
def test_bonus_add(five):
    assert school.bonus_add(70, 85, 90, 95) == [70+five, 85+five, 90+five, 95+five]


@pytest.mark.parametrize("grade, expected", [(100, "Excellent"),
                                             (99, "Very Good"),
                                             (80, "Very Good"),
                                             (79, "Good"),
                                             (70, "Good"),
                                             (69, "Pass"),
                                             (60, "Pass"),
                                             (59, "Fail")])
def test_result_get(grade, expected):
    assert school.result_get(grade) == expected

