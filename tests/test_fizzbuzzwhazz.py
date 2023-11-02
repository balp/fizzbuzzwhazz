import pytest

from fizbuzz import fizz_buzz_whazz


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
