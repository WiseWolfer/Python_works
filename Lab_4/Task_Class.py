import datetime
import shelve


class IncorrectYear(Exception):
    pass


class Book:
    # конструктор со значениями поумолчанию
    def __init__(self, name="Somebook", amount_of_pages=0, price=0):
        self.__name = name
        self.__amount_of_pages = amount_of_pages
        self.__price = price
        self.__book_age = 0
        self.__days_from_realese = 0
        self.__data = 0
        self.__counter = 0
        self.__prev_data = 0

    @property
    def amount_of_page(self):
        return self.__amount_of_pages

    @property
    def get_name(self):
        return self.__name

    @property
    def price_list(self):
        return self.__price


    def display_Book_information(self, counter=0):
        print("Название книги:", str(self.__name),
              "\nЦена книги:", str(self.__price),
              "\nКол-во страниц:", str(self.__amount_of_pages))
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
                        answers["Название произведения_" + str(self.__counter) + ":"] = str(self.__name)
                        answers["Цена книги_" + str(self.__counter) + ":"] = str(self.__price)
                        answers["Возраст книги_" + str(self.__counter) + ":"] = str(self.__book_age)
                        answers["Кол-во страниц книги_" + str(self.__counter) + ":"] = str(self.__amount_of_pages)
                        answers["Дней со дня издания_" + str(self.__counter) + ":"] = str(self.__days_from_realese)
                    break
                else:
                    raise Exception("Ответ должен быть да или нет!!!")
            except Exception as e:
                print(e)

    def __del__(self):
        print(self.__name, "- Объект класса уничтожен!")

    # вычисляет сколько лет книге
    def count_age(self, age_of_book):
        now = datetime.datetime.today()
        self.__data = str(now.date()).split("-")
        num_year = 0
        for i in self.__data:
            if i == self.__data[0]:
                num_year = int(i)
        while True:
            try:
                if type(age_of_book) != int:
                    raise IncorrectYear("Вы ввели дату не по формату!")
                else:
                    break
            except IncorrectYear as err:
                print(err)
                try:
                    age_of_book = int(input("Введите год создания произведения: "))
                except ValueError:
                    print("Введите уже наконец числами год создания произведения!!!")
                    try:
                        age_of_book = int(input("Введите год создания произведения: "))
                        if age_of_book > num_year:
                            raise ValueError("Введенный код больше текущего, такого не может быть!")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        age_of_book = int(input("Введите год создания произведения: "))
                break
        # Возраст книги
        self.__book_age = num_year - int(age_of_book)

    # считаем сколько дней прошло с момента издательства книги
    def day_calculations(self, day_of_finished_writing):
        try:
            now = datetime.datetime.today()
            self.__data = str(now.date()).split("-")
            # фиксируем дни текущего года
            curr_num_year, curr_num_date, curr_num_month = int(self.__data[0]), int(self.__data[2]), int(self.__data[1])
            # перебираем элементы списка и переводим их в числа
            self.__prev_data = [int(item) for item in day_of_finished_writing]
            # записываем элементы в нужную переменную с датой, месяцем и годом
            day, month, year = self.__prev_data[0], self.__prev_data[1], self.__prev_data[2]
            if curr_num_year < year or (month > 12 or month <= 0) or (day > 31 or day <= 0):
                print("Вы ввели не корректные данные! \nВаши данные: {} , {}, {}".format(day, month, year))
                raise IOError
            else:
                # записываем текущую дату в now
                now = datetime.datetime(curr_num_year, curr_num_month, curr_num_date).strftime("%Y-%m-%d")
                # дата окончания написания произведения
                timefinished = datetime.datetime(year, month, day).strftime("%Y-%m-%d")
                now = datetime.datetime.fromisoformat(now)
                timefinished = datetime.datetime.fromisoformat(timefinished)
                # получаем объект класса timedelta, который нам и нужен
                # Со дня издательства книги прошло дней
                self.__days_from_realese = now - timefinished
                self.__days_from_realese = self.__days_from_realese.days
        except IOError as err:
            print(err)

    def __str__(self):
        return f"\nНазвание книги: {self.__name} \nВозраст книги: {self.__book_age } \nКол-во страниц: {self.__amount_of_pages} \nСтоимость: {self.__price} \nДней со дня издания: {self.__days_from_realese}"
