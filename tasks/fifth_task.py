from typing import List


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_factors(n: int) -> List[int]:
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def legendre_symbol(q: int, p: int) -> int:
    l = 0

    if p <= 1:
        print('LEGENDRE_SYMBOL - Fatal error!')
        print('P must be greater than 1.')
        l = -2
        exit('LEGENDRE_SYMBOL - Fatal error!')

    if not is_prime(p):
        print('LEGENDRE_SYMBOL - Fatal error!')
        print('P is not prime.')
        l = -3
        exit('LEGENDRE_SYMBOL - Fatal error!')

    if q % p == 0:
        l = 0
        return l

    if p == 2:
        l = 1
        return l

    qq = q
    while qq < 0:
        qq = qq + p

    nstack = 0
    pstack = [0] * 100
    qstack = [0] * 100
    pp = p
    l = 1

    while True:
        if pp == 0:
            break

        qq = qq % pp

        factors = prime_factors(qq)

        if not factors:
            print('LEGENDRE_SYMBOL - Fatal error!')
            print('Not enough factorization space.')
            l = -5
            exit('LEGENDRE_SYMBOL - Fatal error!')

        nmore = 0

        for factor in factors:
            if factor % 2 == 1:
                nmore += 1
                pstack[nstack] = pp
                qstack[nstack] = factor
                nstack += 1

        hop = False

        if nmore != 0:
            nstack -= 1
            qq = qstack[nstack]

            if qq == 1:
                l = 1 * l
            elif qq == 2 and (pp % 8 == 1 or pp % 8 == 7):
                l = 1 * l
            elif qq == 2 and (pp % 8 == 3 or pp % 8 == 5):
                l = -1 * l
            else:
                if pp % 4 == 3 and qq % 4 == 3:
                    l = -1 * l

                rr = pp
                pp = qq
                qq = rr

                hop = True

        if not hop and nstack == 0:
            break

        nstack -= 1
        pp = pstack[nstack]
        qq = qstack[nstack]

    return l


def solution(q: int, p: int, criteria: int) -> int:
    if criteria == 1:
        # Euler's criterion
        return legendre_symbol(q, p)
    elif criteria == 2:
        # Gauss's criterion
        # Implement Gauss's criterion here if needed
        pass
    else:
        # Other criteria or default behavior
        pass


def main():
    instruction_title = f"{'*' * 17} Инструкция для Задания 5: {'*' * 17}"
    equation_example = "Вычислить символ лежандра (170/311) c помощью критерия Эйлера"
    help1 = "Третьим числом надо выбрать какой критерий нужен:"
    help2 = "1 - Эйлера, 2 - Гаусса, 3 - не указан"
    input_prompt = "Ниже мы для этого примера должны ввести 2 числа: 170 31 1"
    separator = "*" * 61

    print(instruction_title.center(61))
    print(equation_example.center(61))
    print(help1.center(61))
    print(help2.center(61))
    print(input_prompt.center(61))
    print(separator)

    q, p, criteria = map(int, input("Введите три числа через пробел: ").split())
    symbol = solution(q, p, criteria)
    print(f"Legendre Symbol ({q}/{p}): {symbol}")


if __name__ == "__main__":
    main()
