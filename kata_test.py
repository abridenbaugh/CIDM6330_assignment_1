import pytest
# Dr. Babb's code

from kata import number_conversion


def test_number_conversion():
    assert number_conversion(123) == "CXXIII"
    assert number_conversion(2023) == "MMXXIII"
