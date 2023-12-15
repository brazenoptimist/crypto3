from tabulate import tabulate
from typing import List, Tuple

def extract_sqrt_by_complex_mod(a, q, p):
    n = q * p
    r1, r2 = extract_sqrt_by_prime_mod(a, p)
    s1, s2 = extract_sqrt_by_prime_mod(a, q)

    c, d = extended_gcd(p, q)

    x = (r1*d*q + s1*c*p) % n
    y = (r1*d*q - s1*c*p) % n

    print(f"Ответ: {x} {-x} {y} {-y}")

    return (x, -x, y, -y)

def extract_sqrt_by_prime_mod(a, p):
    ls = legendre_symbol(a, p)

    print("Шаг 1.")
    if ls == -1:
        print(f"Символ Лежандра ({a}/{p}) = -1, поэтому нет решений\n")
        return None

    print(f"Символ Лежандра ({a}/{p}) = {ls}\n")
    b = 0
    for i in range(2, p - 1):
        if legendre_symbol(i, p) == p-1:
            b = i
            break

    print(f"Шаг 2.\nb = {b}\n")

    print(f"Шаг 3.\n{p} - 1 = {p - 1}")
    s = 1
    t = (p - 1) // 2
    print(t)
    while t % 2 == 0:
        t //= 2
        print(t)
        s += 1

    print(f"t = {t}")
    print(f"s = {s}\n")

    print("Шаг 4.")
    _, y2 = extended_gcd(p, a)
    print(f"{a}^-1 mod {p} = {y2}\n")

    c0 = pow_by_mod(b, t, p)
    r = pow_by_mod(a, (t + 1) // 2, p)

    print(f"Шаг 5.\nc0 = {b}^{t} mod {p} = {c0}\nr = {a}^{(t + 1) // 2} mod {p} = {r}\n")

    print("Шаг 6.")
    for i in range(1, s):
        print(f"Шаг 6.{i}")
        d = pow_by_mod(r**2 * y2, 2**(s - i - 1), p)
        print(f"d = ({r}^2 * {y2})^2^{s - i - 1} mod {p} = {d}")
        if d == -1 or d == p - 1:
            r = (r * c0) % p
            print(f"r = {c0} * {r} mod {p} = {r}")

        c0 = pow_by_mod(c0, 2, p)
        print(f"c0 = {c0}^2 mod {p} = {c0}\n")

    print(f"Ответ: r={r}, -r={-r}")

    return (r, -r)


def legendre_symbol(a, p):
    return pow_by_mod(a, (p - 1) // 2, p)

def pow_by_mod(num, pow, mod):
    a = 1
    while pow != 1:
        if pow % 2 == 0:
            num = num**2 % mod
            pow //= 2
        else:
            a = (a * num) % mod
            pow -= 1

    return (num * a) % mod

def extended_gcd(a: int, b: int) -> List[Tuple[int, ...]]:
    x2, x1, y2, y1 = 1, 0, 0, 1
    steps: List[Tuple[int, ...]] = [(None, None, None, None, a, b, x2, x1, y2, y1)]

    while b != 0:
        q, r = divmod(a, b)
        x, y = x2 - q * x1, y2 - q * y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y
        steps.append((q, r, x, y, a, b, x2, x1, y2, y1))

    return x2, y2

def main():
    print("Выберите подтип задания (1 для простого делителя, 2 для составного):")
    choice = input("Введите номер подтипа: ")
    print("\n")
    if choice == "1":
        instruction_title = f"{'*' * 15} Инструкция для Задания 4: {'*' * 15}"
        equation_example = "x^2 ≡ 805 (mod 857)"
        input_prompt = "Ниже мы для этого примера должны ввести 2 числа: 805 857"
        separator = "*" * 56

        print(instruction_title.center(56))
        print(equation_example.center(56))
        print(input_prompt.center(56))
        print(separator)
        a, p = map(int, input("Введите два числа через пробел: ").split())
        extract_sqrt_by_prime_mod(a, p)
        print("*"*60)

    elif choice == "2":
        instruction_title = f"{'*' * 15} Инструкция для Задания 4: {'*' * 15}"
        equation_example = "x^2 ≡ 421 (mod 3503), если извечтно, что 3503 = 31 * 113"
        input_prompt = "Ниже мы для этого примера должны ввести 3 числа: 421 31 113"
        separator = "*" * 56

        print(instruction_title.center(56))
        print(equation_example.center(56))
        print(input_prompt.center(56))
        print(separator)
        a, p, q = map(int, input("Введите три числа через пробел: ").split())
        extract_sqrt_by_complex_mod(a, p, q)
        print("*"*60)


