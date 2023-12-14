from first_task import main as first_task_main
from second_task import main as second_task_main
from third_task import main as third_task_main

def main():
    while True:
        print("Выберите задание (1, 2, 3), или введите 'exit' для завершения:")
        choice = input("Введите номер задания: ")
        if choice == "exit":
            print("Программа завершена.")
            break
        elif choice == "1":
            first_task_main()
        elif choice == "2":
            second_task_main()
        elif choice == "3":
            third_task_main()
        else:
            print("Некорректный выбор задания.")

if __name__ == "__main__":
    main()
