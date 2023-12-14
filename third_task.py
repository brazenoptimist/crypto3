from tabulate import tabulate
from typing import List, Tuple, Any


def find_m(m: int, a: int) -> int :
    steps: List[Tuple[int, ...]] = [(None, m, a)]
    while a != 0 :
        r = divmod(m, a)[1]
        m, a = a, r
        steps.append((r, m, a))
    table_headers = ["r", "m", "a"]
    formatted_steps = [list(map(lambda x : "None" if x is None else str(x), step)) for step in steps]
    print(tabulate(formatted_steps, headers=table_headers, tablefmt="pretty"))
    return steps[-1][1]


def extended_gcd_for_1(m: int, a: int) -> tuple[list[tuple[int, ...]], int | Any] :
    y2, y1 = 0, 1
    steps: List[Tuple[int, ...]] = [(None, None, None, m, a, y2, y1)]

    while a != 0 :
        q, r = divmod(m, a)
        y = y2 - q * y1
        m, a, y2, y1 = a, r, y1, y
        steps.append((q, r, y, m, a, y2, y1))

    table_headers = ["q", "r", "y", "m", "a", "y2", "y1"]
    formatted_steps = [list(map(lambda x : "None" if x is None else str(x), step)) for step in steps]

    print(tabulate(formatted_steps, headers=table_headers, tablefmt="pretty"))

    return steps, y2


def main()  -> object:
    instruction_title = f"{'*' * 24} Инструкция для Задания 3: {'*' * 24}"
    equation_example = "324x ≡ 162 (mod 1074)"
    input_prompt = "Ниже мы для этого примера должны ввести 3 числа: 324 162 1074"
    separator = "*" * 75

    print(instruction_title.center(75))
    print(equation_example.center(75))
    print(input_prompt.center(75))
    print(separator)

    a, x, m = map(int, input("Введите три числа через пробел: ").split())
    print(f"Решить уравнение {a}x ≡ {x} (mod {m})")
    devision = find_m(m, a)
    print(f"НОД{a, m} = {devision}")
    new_a, new_x, new_m = a // devision, x // devision, m // devision
    print(f"{new_a}x ≡ {new_x} (mod {new_m})")

    new_equation = extended_gcd_for_1(new_m, new_a)
    print(f"{new_a}^-1 (mod {new_m}) = {new_equation[1]}")

    x = new_equation[1] * new_x % new_m

    print("Множество решений:")
    solutions = [x + i * new_m for i in range(devision)]
    print("\n".join(f"x ≡ {solution} (mod {m})" for solution in solutions))


if __name__ == "__main__" :
    main()
