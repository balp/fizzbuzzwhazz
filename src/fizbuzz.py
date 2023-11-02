import math

def fizz_buzz_whazz(number: int) -> str:
    """Return the Fizz Buzz Whazz string for any number between 1 and 199"""
    if is_dividable_by(3 * 5 * 7, number):
        return "FizzBuzzWhazz"
    if is_dividable_by(5 * 7, number):
        return "BuzzWhazz"
    if is_dividable_by(3 * 7, number):
        return "FizzWhazz"
    if is_dividable_by(3 * 5, number):
        return "FizzBuzz"
    if is_dividable_by(7, number):
        return "Whazz"
    if is_dividable_by(5, number):
        return "Buzz"
    if is_dividable_by(3, number):
        return "Fizz"
    return _as_letters(number)


def is_dividable_by(divisor, number):
    """True if number is dividable by divisor."""
    return number % divisor == 0


def numbers(number: int) -> str:
    """Return the string from of any number between 1 and 199"""
    return _as_letters(number)


def _is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def _as_letters(number: int) -> str:
    _single_number = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
        "Twenty",
    ]
    _teen_number = [
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
        "Twenty",
        "Twenty-One",
    ]
    _ten_number = [
        "",
        "",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]
    result = ""
    if number > 99:
        result = "One Hundred "
        number -= 100
    if number > 19:
        ten = number // 10
        result += _ten_number[ten]
        ones = number % 10
        if ones:
            result += " " + _single_number[ones]
        return result.strip()
    if number > 9:
        return (result + _teen_number[number - 10]).strip()
    return (result + _single_number[number]).strip()
