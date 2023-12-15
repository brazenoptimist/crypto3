from tasks.first_task import main as first_task_main
from tasks.second_task import main as second_task_main
from tasks.third_task import main as third_task_main
from tasks.fourth_task import main as fourth_task_main
from tasks.fiveth_task import main as fiveth_task_main
def main():
    while True:
        print("1 – НОД")
        print("2 – РЕШЕНИЕ СИСТЕМ СРАВНЕНИЙ")
        print("3 – РЕШЕНИЕ СРАВНЕНИЙ ПЕРВОЙ СТЕПЕНИ С ОДНИМ НЕИЗВЕСТНЫМ")
        print("4 – РЕШЕНИЕ СРАВНЕНИЙ ВТОРОЙ СТЕПЕНИ")
        print("5 – ВЫЧИСЛЕНИЕ СИМВОЛА ЛЕЖАНДРА\n")

        print("Выберите номер задания (1, 2, 3, 4, 5), или введите 0 для завершения:")
        choice = input("Введите номер задания: ")
        print("\n")
        if choice == "0":
            print("Программа завершена.")
            break
        elif choice == "1":
            first_task_main()
        elif choice == "2":
            second_task_main()
        elif choice == "3":
            third_task_main()
        elif choice == "4":
            fourth_task_main()
        elif choice == "5":
            fiveth_task_main()
        else:
            print("Некорректный выбор задания.")

if __name__ == "__main__":
    main()
