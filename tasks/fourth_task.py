from tabulate import tabulate

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
    steps, y2 = extended_gcd_for_1(p, a)
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

def extended_gcd_for_1(m: int, a: int) -> tuple[list[tuple[int, ...]], int | int] :
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

def main():
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

