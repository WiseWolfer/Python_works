import shelve
from Task_Class import Book


class Author(Book):
    def __init__(self, name, amount_of_pages, price, author_name):
        Book.__init__(self, name, amount_of_pages, price)
        self.__author_name = author_name

    @property
    def get_author_name(self):
        return self.__author_name

    def display_Book_information(self, counter=0):
        counter = counter + 1
        Book.display_Book_information(self, counter)
        filename = "Result_of_displaying"
        print("Автор книги:", self.__author_name)
        with shelve.open(filename) as file:
            file["Автор книги_" + str(counter) + ":"] = self.__author_name
