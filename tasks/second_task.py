from tabulate import tabulate
from functools import reduce
from typing import List, Tuple


def extended_gcd(a: int, b: int) -> List[Tuple[int, ...]]:
    x2, x1, y2, y1 = 1, 0, 0, 1
    steps: List[Tuple[int, ...]] = [(None, None, None, None, a, b, x2, x1, y2, y1)]

    while b != 0:
        q, r = divmod(a, b)
        x, y = x2 - q * x1, y2 - q * y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y
        steps.append((q, r, x, y, a, b, x2, x1, y2, y1))

    return steps


def main():
    instruction_title = f"{'*' * 37} Инструкция для Задания 2: {'*' * 37}"
    equation_example = "x = 2 (mod 17)"
    equation_example1 = "x = 3 (mod 19)"
    equation_example2 = "x = 4 (mod 23)"
    input_prompt = "Ниже мы для этого примера должны ввести количество строк в системе, а затем x и mod для каждой строки"
    separator = "*" * 101

    print(instruction_title.center(101))
    print(equation_example.center(101))
    print(equation_example1.center(101))
    print(equation_example2.center(101))
    print(input_prompt.center(101))
    print(separator)

    n = int(input('Введите количество строк в системе(через пробел): '))
    x, modd = zip(*(map(int, input('Введите x и mod (через пробел): ').split()) for _ in range(n)))
    N = reduce(lambda x, y : x * y, modd, 1)
    print("\n")
    print(f"Считаем N (произведение всех модулей) = {N}\n" + "\n".join(
        f"Считаем N_{i} = {N} / {modd[i]} = {N // modd[i]}" for i in range(n)))

    a = 0
    equation_str = ""

    for i in range(n):
        steps = extended_gcd(N // modd[i], modd[i])
        last_step = steps[-1]
        x_val = last_step[6]

        table_headers = ["q", "r", "x", "y", "a", "b", "x2", "x1", "y2", "y1"]
        formatted_steps = [list(map(lambda x: "None" if x is None else str(x), step)) for step in steps]

        print(tabulate(formatted_steps, headers=table_headers, tablefmt="pretty"))
        print("\n")

        equation_str += f"{x[i]}*{N // modd[i]}*{x_val} + "
        a += x[i] * N // modd[i] * x_val

    print(f'a  = {equation_str[:-3]} = {a} = {a % reduce(lambda x, y: x * y, modd)} mod(M = {" * ".join(map(str, modd))})')
    print("*" * 60)

if __name__ == "__main__":
    main()
