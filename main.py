class Person:
    def __init__(self):
        pass

    def get_info(self):
        pass


class Student():
    def __init__(self):
        pass

    def get_info(self):
        pass


class Teacher():
    def __init__(self):
        pass

    def get_info(self):
        pass


class DepartmentHead(Teacher):
    def __init__(self):
        pass

    def get_info(self):
        pass


def add_person():
    pass


def view_students():
    pass


def view_teachers():
    pass


def view_department_heads():
    pass


def main():
    while True:
        print("1. Добавить человека")
        print("2. Посмотреть список студентов")
        print("3. Посмотреть список преподавателей")
        print("4. Посмотреть список заведующих кафедрой")
        print("5. Выйти")
        choice = input("Введите ваш выбор: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            break
        else:
            pass


if __name__ == "__main__":
    main()
