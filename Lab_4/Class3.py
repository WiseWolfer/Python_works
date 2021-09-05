from Task_Class import Book
from Class1 import Author
from Class2 import Find_illustrations


class BookType(Find_illustrations):
    def __init__(self, name, amount_of_pages, price, author_name, type_of_book=None):
        Book.__init__(self, name, amount_of_pages, price)
        Author.__init__(self, name, amount_of_pages, price, author_name)
        Find_illustrations.__init__(self, name, amount_of_pages, price, author_name)
        self.__type_of_book = type_of_book
        self.__res3 = {}
        self.__counter = 0

    @property
    def type_of_book(self):
        return self.__type_of_book

    def show(self, counter=0):
        counter += 1
        Find_illustrations.show(self, counter)
        print("\nТип книги: ", self.__type_of_book)
        self.__res3 = {"Тип книги": self.__type_of_book}
