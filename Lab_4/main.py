# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.

# подключаем классы к проекту


# from classes import Person, Auto

# def main():
#     tom = Person("Tom")
#     tom.display_info()
#     del tom
#     bmw = Auto("BMW")
#     bmw.move(120)

# если нужно задать атрибут с инкапсуляцией делаем так:
# пример: self.__age = age - тогда извне это поле не изменим
# также делаем метод get() и set() для считывания и установки значения этого поля

# @property - ставится над геттером (явно показываем, что это геттер-свойство)
# @имя_свойства_сеттера.setter - ставится над сеттером
# сначала определяется свойства геттера, потом свойства сеттера
# сеттер и геттер называются одинаково
# Пример инкапсуляции с наследованием

# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # устанавливаем имя
#         self.__age = age  # устанавливаем возраст
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print("Имя:", self.__name, "\tВозраст:", self.__age)
#
# class Employees(Person):
#     def details(self, company):
#         print(self.name, "работает в компании:", company)
# def main():
#     tom = Person("Tom")
#     tom.display_info()
#     tom.age = -3486
#     print(tom.age)  # Недопустимый возраст
#     tom
#     tom.age = 36
#     tom.display_info()
# def main():
#     tom = Employees("Tom",23)
#     tom.details("Google")
#     tom.age = 33
#     tom.display_info()

# пример Полиморфизма
# class Person:
#     def __init__(self, name, age):
#         self.__name = name # устанавливаем имя
#         self.__age = age # устанавливаем возраст
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
#     def display_info(self):
#         print("Имя:", self.__name, "\tВозраст:", self.__age)
#     # получаем строковое представление объекта класса
#     # (получаем объект в виде строки)
#     def __str__(self):
#         return "Имя: {} \t Возраст: {}".format(self.__name, self.__age)
#
# class Employee(Person):
#     # определение конструктора
#     def __init__(self, name, age, company):
#         Person.__init__(self, name, age)
#         self.company = company
#     # переопределение метода display_info
#     def display_info(self):
#         Person.display_info(self)
#         print("Компания:", self.company)
# class Student(Person):
#     # определение конструктора
#     def __init__(self, name, age, university):
#         Person.__init__(self, name, age)
#         self.university = university
#     # переопределение метода display_info
#     def display_info(self):
#         print("Студент", self.name, ",возрастом ",self.age," лет, ","учится в университете",
#         self.university)
#
# def main():
#     people = [Person("Tom", 23), Student("Bob", 19, "Harvard"),
#     Employee("Sam", 35, "Google")]
#     for items in people:
#         items.display_info()
#         print()
#
#     # isinstance() - проверяет принадлежность объекта к классу (его типу)
#     # если объект представляет указанный тип, то функция возвращает true, иначе false
#     # Пример:
#     for person in people:
#         if isinstance(person, Student):
#             print(person.university)
#         elif isinstance(person, Employee):
#             print(person.company)
#         else:
#             print(person.name)
#         print()
#
#     tom = Person("Tom", 23)
#     print(tom)
from Task_Class import Book
from Class1 import Author
from Class2 import Find_illustrations
from Class3 import BookType
import shelve


def readfile():
    filename = input("Введите название файла для открытия: ")
    while True:
        try:
            if filename == "Result_of_displaying":
                with shelve.open(filename) as file:
                    for items in file:
                        print(items + " " + file[items])
                    break
            else:
                raise IOError("Вы открываете несуществующий файл!")
        except IOError as err:
            print(err)
            filename = input("Введите название файла для открытия: ")
    print()


def main():
    test_book = Book()
    print(test_book)
    print()
    try:
        book_types = [Book(input("Введите произведение: "),
                           int(input("Введите кол-во страниц: ")),
                           int(input("Введите стоимость произведение: "))),
                      Author(input("\nВведите произведение: "),
                             int(input("Введите кол-во страниц: ")),
                             int(input("Введите стоимость произведения: ")),
                             input("Введите имя автора: ")),
                      Find_illustrations(input("\nВведите произведение: "),
                                         int(input("Введите кол-во страниц: ")),
                                         int(input("Введите стоимость произведения: ")),
                                         input("Введите имя автора: ")),
                      BookType(input("\nВведите произведение: "),
                               int(input("Введите кол-во страниц: ")),
                               int(input("Введите стоимость произведения: ")),
                               input("Введите имя автора: "),
                               input("Введите тип книги: "))]
        for items in book_types:
            if isinstance(items, BookType):
                amount_of_illustration = int(input(f"Введите кол-во иллюстраций в книге {items.get_name}: "))
                # заводим число иллюстраций и пишем его в класс
                items.get_book_thickness = amount_of_illustration
                print()
                items.thickness_control()
                items.show()
                print()
            elif isinstance(items, Find_illustrations):
                print()
                amount_of_illustration = int(input(f"Введите кол-во иллюстраций в книге {items.get_name}: "))
                # заводим число иллюстраций и пишем его в класс
                items.get_book_thickness = amount_of_illustration
                print()
                items.thickness_control()
                items.show()
            elif isinstance(items, Book):
                print()
                items.count_age(input(f"Введите год создания книги (только год) {items.get_name}: "))
                items.day_calculations(input(f"Введите дату издания книги (число месяц год) {items.get_name}: ").split(" "))
                print(items)
                print()
                items.display_Book_information()
            elif isinstance(items, Author):
                items.display_Book_information()
                print()
    except ValueError:
        print()
        print("Видимо, вы ошиблись в значении!!")
        raise AssertionError('Not passed')
    except AssertionError as e:
        print(e)
        return 0
    readfile()


if __name__ == '__main__':
    main()
