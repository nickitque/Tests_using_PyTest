import pytest

from calc.calculator import calculator


def test_plus():
    assert calculator('2+2') == 4


def test_minus():
    assert calculator('55-32') == 23


def test_multiplication():
    assert calculator('2*8') == 16


def test_division():
    assert calculator('16/2') == 8


def test_plus_negative():
    assert calculator('2+2') != 5


def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('abracadabra')
    assert 'Выражение должно содержать хотя бы один знак (+-/*)' == error.value.args[0]


def test_3_numbers():
    with pytest.raises(ValueError) as error:
        calculator('2+2+2')
    assert 'Выражение должно содержать 2 целых числа и 1 знак' == error.value.args[0]


if __name__ == "__main__":
    pytest.main()
