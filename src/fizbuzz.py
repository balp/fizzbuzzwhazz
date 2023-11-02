def fizz_buzz_whazz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return "FizzBuzzWhazz"
    if number % 5 == 0 and number % 7 == 0:
        return "BuzzWhazz"
    if number % 3 == 0 and number % 7 == 0:
        return "FizzWhazz"
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 7 == 0:
        return "Whazz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return numbers(number)


def numbers(number: int) -> str:
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
