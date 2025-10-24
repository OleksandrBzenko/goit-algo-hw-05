import re
from typing import Callable, Generator


def generator_numbers(text: str)-> Generator[float, None, None]:
    numbers = re.findall(r"\d+\.\d+|\d+", text)# Знаходимо всі дійсні числа у тексті
    for number in numbers:
        yield float(number)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]):
    return sum(func(text))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 "
        "і 324.00 доларів."
    )
    total_profit = sum_profit(text, generator_numbers)
    print(f"Total income: {total_profit}")
