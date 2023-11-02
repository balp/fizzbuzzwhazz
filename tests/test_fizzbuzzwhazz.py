import pytest

from fizbuzz import fizz_buzz_whazz, numbers


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "One"),
        (2, "Two"),
        (3, "Fizz"),
        (4, "Four"),
        (5, "Buzz"),
        (6, "Fizz"),
        (7, "Whazz"),
        (8, "Eight"),
        (9, "Fizz"),
        (15, "FizzBuzz"),
        (21, "FizzWhazz"),
        (35, "BuzzWhazz"),
        (105, "FizzBuzzWhazz"),
    ],
)
def test_fizzbuzzwhazz(number, expected):
    assert fizz_buzz_whazz(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "One"),
        (2, "Two"),
        (3, "Three"),
        (4, "Four"),
        (5, "Five"),
        (6, "Six"),
        (7, "Seven"),
        (8, "Eight"),
        (9, "Nine"),
        (10, "Ten"),
        (11, "Eleven"),
        (12, "Twelve"),
        (13, "Thirteen"),
        (14, "Fourteen"),
        (15, "Fifteen"),
        (16, "Sixteen"),
        (17, "Seventeen"),
        (18, "Eighteen"),
        (19, "Nineteen"),
        (20, "Twenty"),
        (21, "Twenty One"),
        (22, "Twenty Two"),
        (29, "Twenty Nine"),
        (30, "Thirty"),
        (42, "Forty Two"),
        (55, "Fifty Five"),
        (69, "Sixty Nine"),
        (72, "Seventy Two"),
        (84, "Eighty Four"),
        (99, "Ninety Nine"),
        (100, "One Hundred"),
        (105, "One Hundred Five"),
        (119, "One Hundred Nineteen"),
        (142, "One Hundred Forty Two"),
    ],
)
def test_numbers(number, expected):
    assert numbers(number) == expected
