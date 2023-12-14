from tabulate import tabulate
from typing import List, Tuple

def extended_gcd_for_1(m: int, a: int) -> Tuple[List[Tuple[int, ...]], int | int]:
    y2, y1 = 0, 1
    steps: List[Tuple[int, ...]] = [(None, None, None, m, a, y2, y1)]

    while a != 0:
        q, r = divmod(m, a)
        y = y2 - q * y1
        m, a, y2, y1 = a, r, y1, y
        steps.append((q, r, y, m, a, y2, y1))

    table_headers = ["q", "r", "y", "m", "a", "y2", "y1"]
    formatted_steps = [list(map(lambda x: "None" if x is None else str(x), step)) for step in steps]

    print(tabulate(formatted_steps, headers=table_headers, tablefmt="pretty"))

    return steps, y2


def main():
    instruction_title = f"{'*' * 24} Инструкция для Задания 1: {'*' * 24}"
    equation_example = "Вычислить 877^-1 (mod 2467)"
    input_prompt = "Ниже мы для этого примера должны ввести 2 числа: 877 2467"
    separator = "*" * 75

    print(instruction_title.center(75))
    print(equation_example.center(75))
    print(input_prompt.center(75))
    print(separator)

    a, m = map(int, input("Введите два числа через пробел: ").split())
    result = extended_gcd_for_1(m, a)

    print(f"Ответ a^-1 = {result[1]}")
    print("*" * 49)
    print("ПРОВЕРКА".center(49))
    print(f"{a} * {result[1]} = {a * result[1]} = {a * result[1] % m} mod {m}".center(49))
    print("*" * 49)



if __name__ == "__main__":
    main()
