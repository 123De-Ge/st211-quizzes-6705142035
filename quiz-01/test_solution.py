import pytest
from solution import RomanNumerals


# Create an object from the RomanNumerals class
converter = RomanNumerals()


def test_one():
    assert converter.to_roman(1) == "I"


def test_two():
    assert converter.to_roman(2) == "II"


def test_three():
    assert converter.to_roman(3) == "III"


def test_four():
    assert converter.to_roman(4) == "IV"


def test_five():
    assert converter.to_roman(5) == "V"


def test_nine():
    assert converter.to_roman(9) == "IX"


def test_ten():
    assert converter.to_roman(10) == "X"


def test_forty():
    assert converter.to_roman(40) == "XL"


def test_fifty():
    assert converter.to_roman(50) == "L"


def test_ninety():
    assert converter.to_roman(90) == "XC"


def test_one_hundred():
    assert converter.to_roman(100) == "C"


def test_four_hundred():
    assert converter.to_roman(400) == "CD"


def test_five_hundred():
    assert converter.to_roman(500) == "D"


def test_nine_hundred():
    assert converter.to_roman(900) == "CM"


def test_one_thousand():
    assert converter.to_roman(1000) == "M"


def test_forty_nine():
    assert converter.to_roman(49) == "XLIX"


def test_nine_hundred_ninety_nine():
    assert converter.to_roman(999) == "CMXCIX"


def test_two_thousand_twenty_six():
    assert converter.to_roman(2026) == "MMXXVI"


def test_zero():
    with pytest.raises(ValueError):
        converter.to_roman(0)


def test_negative_number():
    with pytest.raises(ValueError):
        converter.to_roman(-10)


def test_string_input():
    with pytest.raises(TypeError):
        converter.to_roman("10")


def test_float_input():
    with pytest.raises(TypeError):
        converter.to_roman(10.5)