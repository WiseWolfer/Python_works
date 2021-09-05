from Task_Class import Book
from Class1 import Author
import shelve


class Find_illustrations(Author):
    def __init__(self, name, amount_of_pages, price, author_name):
        Book.__init__(self, name, amount_of_pages, price)
        Author.__init__(self, name, amount_of_pages, price, author_name)
        self.__illustations_including = 0
        self.__counter = 2

    @property
    def get_book_thickness(self):
        return self.__illustations_including

    @get_book_thickness.setter
    def get_book_thickness(self, illustations_including):
        if int(illustations_including) > self.amount_of_page:
            print("Такого не может быть!\nВведите еще раз число иллюстраций!")
            self.__illustations_including = int(input("Число иллюстраций: "))
        else:
            self.__illustations_including = illustations_including

    def thickness_control(self):
        result_of_counting = int(round(self.__illustations_including / self.amount_of_page * 100))
        if (result_of_counting >= 60) and (result_of_counting <= 100):
            print("Книжка состоит из иллюстраций: {} % - скорей всего перед нами комикс!".format(result_of_counting))
        elif (result_of_counting >= 30) and (result_of_counting < 60):
            print("Книжка состоит из иллюстраций: {} % - скорей всего перед нами легкая новелла!".format(result_of_counting))
        else:
            print("Книжка состоит из иллюстраций: {} % - скорей всего эта повесть или роман!".format(result_of_counting))

    def show(self, counter=0):
        print("Название книжки: {} "
              "\nАвтор книги: {} "
              "\nСтоимость книги: {}"
              "\nВсего страниц в книге: {} "
              "\nКол-во цветных иллюстраций в книге: {}"
              "".format(self.get_name,
                        self.get_author_name,
                        self.price_list,
                        self.amount_of_page,
                        self.__illustations_including))
        filename = "Result_of_displaying"
        self.__counter += counter + 1
        print("Хотите сохранить вывод?")
        while True:
            try:
                answer = input("Ваш ответ(да/нет): ")
                if answer == "нет":
                    print("Данные не записались в файл!")
                    break
                elif answer == "да":
                    with shelve.open(filename) as answers:
                        answers["Название книжки_" + str(self.__counter) + ":"] = str(self.get_name)
                        answers["Автор книги_" + str(self.__counter) + ":"] = str(self.get_author_name)
                        answers["Стоимость книги_" + str(self.__counter) + ":"] = str(self.price_list)
                        answers["Всего страниц в книге_" + str(self.__counter) + ":"] = str(self.amount_of_page)
                        answers["Кол-во цветных иллюстраций в книге_" + str(self.__counter) + ":"] = str(self.__illustations_including)
                    break
                else:
                    raise Exception("Ответ должен быть да или нет!!!")
            except Exception as e:
                print(e)

