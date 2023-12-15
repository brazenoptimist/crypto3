# TODO сделать вычисление символа лежандра разными способами

def solution() :
    pass


def main() :
    instruction_title = f"{'*' * 24} Инструкция для Задания 5: {'*' * 24}"
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


if __name__ == "__main__" :
    main()
