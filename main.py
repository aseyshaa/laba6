class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, student_id, major):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.major = major

    def get_info(self):
        super().get_info()
        print(f"Студенческий ID: {self.student_id}, Специальность: {self.major}")



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
