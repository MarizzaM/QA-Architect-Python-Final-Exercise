import pytest
import utils_string


@pytest.mark.parametrize("s, expected", [("Hello", "HELLO"),
                                         ("HELLO", "HELLO")])
def test_make_upper(s, expected):
    assert utils_string.make_upper(s) == expected


@pytest.mark.parametrize("s, expected", [("Hello", "hello"),
                                         ("hello", "hello")])
def test_three_make_lower(s, expected):
    assert utils_string.make_lower(s) == expected


@pytest.mark.parametrize("s, e, expected", [("Hello", "l", True),
                                            ("Hello", "a", False)])
def test_e_check(s, e, expected):
    assert utils_string.e_check(s, e) == expected
