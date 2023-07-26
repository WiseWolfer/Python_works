# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # пытаемся открыть файл
    # try:
    #     myfile = open("hello.txt", "r")
    #     try:
    #        myfile.write("hello world!")
    #     except Exception as ex:
    #         print(ex)
    #     # если возникает исключение файл будет все ровно закрыт
    #     # (обязательное закрытие файла) после проверок
    #     finally:
    #          myfile.close()
    # # возникает исключение типа файл не найден, если такого
    # # файла не существует при открытии на чтение
    # except Exception as e:
    #     print(e)

    # второй вариант (более короткий и удобный вариант)
    # with open("hello.txt", "w") as myfile:
    #     myfile.write("Hello, world!")
    # with open("hello.txt", "a") as myfile:
    #     myfile.write("\nGood bye, world!")
    # with open("hello.txt", "a") as myfile:
    #     print("\nHello world", file=myfile)

    # считываем построчно строки файла без применения метода readline()
    # with open("hello.txt", 'r') as myfile:
    #     for i in myfile:
    #         print(i, end="")

    # метод readline() нужен чтобы построчно считать содержимое файла
    # единственный минус кода: считываем
    # в каждую отдельную строчку в строчку - это неудобно
    # with open("hello.txt", 'r') as myfile:
    #     str1 = myfile.readline()
    #     print(str1, end="")
    #     str2 = myfile.readline()
    #     print(str2)
    # with open("hello.txt", "r") as myfile:
    #     line = myfile.readline()
    #     # пока line не пустой, будет все считывать из файла (через цикл while)
    #     while line:
    #         print(line, end="")
    #         line = myfile.readline()
    # если файл не большой то можно считать через read()
    # with open("hello.txt", "r") as myfile:
    #     content = myfile.read()
    #     print(content)

    # считываем весь файл в список строк
    # with open("hello.txt", 'r') as myfile:
    #     content = myfile.readlines()
    #     str1 = content[0]
    #     str2 = content[1]
    #     str3 = content[2]
    #     print(str1, end="")
    #     print(str2, end="")
    #     print(str3)

    # можем явно указать кодировку при открытии файла
    # filename = "hello.txt"
    # with open(filename, encoding="utf8") as myfile:
    #     text = myfile.read()
    #     print(text)

    # имя файла
    # FILENAME = "messages.txt"
    # # определяем пустой список
    # messages = list()
    #
    # for i in range(4):
    #     message = input("Введите строку " + str(i+1) + ": ")
    #     messages.append(message + "\n")
    #
    # # запись элементов списка в файл
    # print("Пошла запись в файл.")
    # with open(FILENAME, "a") as myfile:
    #     for i in messages:
    #         myfile.write(i)
    # print("Данные записались в файл.")

    # считывание записей из файла
    # print("Данные считываются из файла.")
    # with open(FILENAME, "r") as myfile:
    #     for i in myfile:
    #         print(i, end="")
    # print("Данные считались из файла.")

    # Файлы scv
    import csv
    FILENAME = "users.csv"

    # users = [
    #     ["Tom", 28],
    #     ["Alice", 23],
    #     ["Bob", 34]
    # ]
    # # newline="" - позволяет корректно считывать строки из файла
    # # независимо от операционной системы
    # with open(FILENAME, 'w', newline="") as myfile:
    #     # получаем объект writer в который пишем ссылку на файл
    #     writer = csv.writer(myfile)
    #     # осуществляем запись с помощью writerows() - принимает набор строк(двумерный список)
    #     writer.writerows(users)
    #
    # with open(FILENAME, 'a', newline="") as myfile:
    #     user = ["Sam", 31] # одномерный список
    #     writer = csv.writer(myfile)
    #     # если нужно добавить одну запись(одномерный список),
    #     # то нужно использовать метод writerows()
    #     writer.writerow(user)
    #
    # # считываем из файла наш двумерный список(таблицу с разширением csv)
    # with open(FILENAME, 'r', newline="") as myfile:
    #     # создаем объект reader на чтение и считываем по строчно
    #     # первый и второй аргументы
    #     reader = csv.reader(myfile)
    #     for row in reader:
    #         print(row[0] + " - " + row[1])

    # вспомнил список
    # sp = []
    # numbers = int(input("Введите кол-во элементов в списке: "))
    # for number in range(numbers):
    #     nums = int(input("Число под номером " + str(number+1) + " : "))
    #     sp.append(nums)
    # print(sp)
    # sp.append([2, 3])
    # sp.extend([20, 10])
    # print(sp)
    # users =[
    #     {"name": "Tom", "age": 28},
    #     {"name": "Alice", "age": 23},
    #     {"name": "Bob", "age": 34}
    # ]
    # with open(FILENAME, "w", newline="") as myfile:
    #     columns = ["name", "age"]
    #     # в качестве второго аргумента передается набор столбцов
    #     # возвращает объект writer для записи файла
    #     writer = csv.DictWriter(myfile, fieldnames=columns)
    #     # запись заголовков столбцов
    #     writer.writeheader()
    #
    #     # запись нескольких строк
    #     writer.writerows(users)
    #
    #     user = {"name": "Sam", "age": 41}
    #     # запись одной строки
    #     writer.writerow(user)
    #
    # with open(FILENAME, 'r', newline="") as myfile:
    #     # возвращает объект reader для чтения файла
    #     reader = csv.DictReader(myfile)
    #     for row in reader:
    #         print(row["name"], " - ", row["age"])

    # Работа с бинарными файлами
    import pickle
    FILENAME = "user.dat"

    # name = "Tom"
    # age = 19
    #
    # with open(FILENAME, 'wb') as myfile:
    #     # записываем объект obj в бинарный файл
    #     pickle.dump(name, myfile)
    #     pickle.dump(age, myfile)
    #
    # with open(FILENAME, 'rb') as myfile:
    #     name = pickle.load(myfile)
    #     age = pickle.load(myfile)
    #     print("Имя:", name, "\tВозраст:", age)
    # users = [
    #     ["Tom", 28, True],
    #     ["Alice", 23, False],
    #     ["Bob", 34, False]
    # ]
    # with open(FILENAME, "wb") as myfile:
    #     # запист в файл
    #     pickle.dump(users, myfile)
    #
    # with open(FILENAME, "rb") as myfile:
    #     # чтение из файла в объект
    #     users_from_file = pickle.load(myfile)
    #     for user in users_from_file:
    #         print("Имя:", user[0],
    #               "\t\tВозраст:", user[1],
    #               "\t\tЖенат(замужем):", user[2])

    # Модуль shelve (еще один модуль по работе с бинарными)

    import shelve

    # как можно открывать файл и закрытия файла
    # filename = "proba"
    # d = shelve.open(filename)
    # d.close()

    FILENAME = "states2"
    # with shelve.open(FILENAME) as states:
    #     # запись - это присваивание значения определенному ключу
    #     states["London"] = "Great Britain"
    #     states["Paris"] = "France"
    #     states["Berlin"] = "Germany"
    #     states["Madrid"] = "Spain"

    # with shelve.open(FILENAME) as states:
    #     # считывание - это вывод на экран значений по ключу
    #     print(states["London"])
    #     print(states["Paris"])
    #     print(states["Berlin"])
    #     print(states["Madrid"])
    # проверка на существование ключей
    # with shelve.open(FILENAME) as states:
    #      key = "Brussels"
    #      if key in states:
    #          print(states[key])
    # методом get() можно проверить есть ли ключ
    # если он есть выйдет первое значени,  а если нет то второе
    # значение аргумента
    # with shelve.open(FILENAME) as states:
    #      state = states.get("Brussels", "Undefined")
    #      print(state)

    # как можно перебрать все значения через цикл
    # with shelve.open(FILENAME) as states:
    #     for key in states:
    #         print(key, " - ", states[key])

    # отдельно перебираем по ключам и по знаачениям
    # with shelve.open(FILENAME) as states:
    #     for key in states.keys():
    #         print("City: ", key)
    #     print()
    #     for value in states.values():
    #         print("Country: ", value)
    #     print()
    #     for city_country in states.items():
    #         print("City + Country: ", city_country)
    # with shelve.open(FILENAME) as states:
    #     states["London"] = "Great Britain"
    #     states["Tokyo"] = "Japan"
    #     states["Berlin"] = "Germany"
    #     states["Madrid"] = "Spain"
    #
    # # добавляем и изменяем значения в словаре
    # with shelve.open(FILENAME) as states:
    #     states["London"] = "United Kingdom"
    #     states["Tokyo"] = "Country of the rising sun"
    #     states["Moscow"] = "Russia"
    #     for key in states:
    #         print(key, " - ", states[key])
    #     print()
    # # удаляем из словаря данные
    # with shelve.open(FILENAME) as states:
    #     del states["Moscow"]    # удаляем значение с ключом Madrid
    #     for key in states:
    #         print(key, " - ", states[key])
    #     # передаем удаляемое значение ключа в state
    #     # если ключа нет, то запишет в переменную второй аргумент
    #     state = states.pop("London", "Not Found!")
    #     print(state)
    #     for key in states:
    #         print(key, " - ", states[key])
    #     print()
    #     # удаление всех элементов в словаре
    #     states.clear()
    #     for key in states:
    #         print(key, " - ", states[key])
    import os

    # создание и удаление текущего скрипта

    # Создание каталога
    # путь относительно текущего скрипта
    # (создает в каталоге проекта папку "hello")
    #os.mkdir("hello")

    # абсолютный путь
    # создает по этому пути католог hello(папку)
    # os.mkdir("C://Users/Dmitriy")
    # os.mkdir("C://Users/Dmitriy/hello")

    # Удаление каталога
    # 1 - удаление каталога сначала в каталоге скрипта
    # 2 - удаление каталога по заданному пути
    # os.rmdir("hello")
    # os.rmdir("C://Users/Dmitriy/hello")

    # Переминование каталога
    # метод rename("Путь со старым названием","Путь с новым названием")
    #os.rename("C://Users/Dmitriy/hello.txt", "C://Users/Dmitriy/hello")

    # удаление файла c абсолютного пути
    # os.remove("C://Users/Dmitriy/Dima.txt")

    # создаем файл
    # with open("C://Users/Dmitriy/Myfile.txt", 'w') as myfile:
    #     file = myfile.write(myfile)
    # os.remove("C://Users/Dmitriy/Myfile.txt") # удаляем файл
    #
    # # Существование файла
    # # проверяем существует ли файл по такому пути
    # filename = input("Введите путь к файлу: ")
    # if os.path.exists(filename):
    #     print("Указанный файл существует!")
    # else:
    #     print("Указанный файл не существует!")

    #   Задание 1: В файле записаны целые числа. Найти максимальное и
    #   минимальное число и записать в другой файл

    # FILENAME = "hello.txt"
    # a, b = 0, 0
    # sp = []
    # with open(FILENAME, 'r') as myfile:
    #     numbers = myfile.read().split("\n")
    #     for i in numbers:
    #         sp.append(i)
    # print(sp)
    # a = max(sp)
    # b = min(sp)
    #
    # with open("hell.txt", 'w') as myfile:
    #     myfile.write(a + "\n")
    #     myfile.write(b)

    # Необходимо записать в текстовый файл артикул
    # самого дорогого и самого дешевого товара
    # (если их несколько, вывести тот артикул, который находится ниже)

    # FILENAME = "Shop.txt"
    # comodities = [
    #     ["420250; SSD накопитель Kingston; 1700"],
    #     ["820540; Ноутбук Msi Gl 63; 80000"],
    #     ["425850; SSD накопитель Samsung; 12000"],
    #     ["1154016; Ноутбук Acer Aspire; 22140"]
    #     ]
    # with open(FILENAME, 'w', encoding="utf8", newline="") as myfile:
    #     headers = ["Артикул;Наименование;Цена"]
    #     writer = csv.DictWriter(myfile, fieldnames=headers)
    #     writer.writeheader()
    #     writer2 = csv.writer(myfile)
    #     writer2.writerows(comodities)
    #     reader = csv.reader(myfile)
    # with open(FILENAME, 'r', encoding="utf8", newline="") as myfile:
    #     reader = csv.reader(myfile)
    #     for row in reader:
    #         print(row[0])

# 3 Вывести все файлы (полный путь до файла) размером менее 1МБ,
# внутри текущего проекта (включая вложенные директории).

    # loc = os.listdir(".")
    # for files in loc:
    #     if os.path.getsize(files) < 1:
    #         print(files)

# 3. Вывести все файлы (полный путь до файла) с расширением .py
# внутри текущего проекта (включая вложенные директории)

    # path = 'C://Users/Dmitriy/PycharmProjects/Lab2'
    # # проходимся рекурсивно все папки
    # for dirs, folders, files in os.walk(path):
    #     # проходимся по всем файлам
    #     for file in files:
    #         # ищем по названиям файлов с расширением .py
    #         if file.endswith(".py"):
    #             print('Выбранный каталог: ', dirs)
    #             print('Вложенные директории:', folders)
    #             print('Файлы в папке: ', files)

    #Задание №4. Даны два текстовых файла (input_1.txt, input_2.txt), необходимо
    # записать в файл output.txt все слова, которые встречаются в файле input_2.txt, но
    # не встречаются в файле input_1.txt

    # FILENAME1 = "input_1.txt"
    # FILENAME2 = "input_2.txt"
    # with open(FILENAME1, 'r', encoding="utf8") as myfile:
    #     A = set()
    #     for word in myfile:
    #         w = word.split(",")
    #         A = set(w)
    # print(A)
    # with open(FILENAME2, 'r') as myfile:
    #     B = set()
    #     for item in myfile:
    #         word = item.split(",")
    #         B = set(word)
    # print(B)
    # B.difference_update(A)
    # itog = ",".join(list(B))
    # print(itog)
    # with open("output.txt",'w') as myfile:
    #     myfile.write(itog)

    #Задание №5. Дан текстовый файл input.txt. Определить частоту повторяемости
    #каждой кириллической буквы в тексте, отсортировать в порядке убывания
    #частоты, результат записать в файл output.txt. Продемонстрировать работу
    #алгоритма на файлах различной длины.

    FILENAME = "input.txt"
    FILENAME1 = "output2.txt"
    with open(FILENAME, 'r', encoding="utf8") as myfile:
        sp = []
        letters = []
        for i in myfile:
            stroka = "".join(myfile.readlines())
            A = stroka.count("А")
            sp.append(A)
            letters.append("А")
            B = stroka.count("Б")
            sp.append(B)
            letters.append("Б")
            C = stroka.count("В")
            sp.append(C)
            letters.append("В")
            D = stroka.count("Г")
            sp.append(D)
            letters.append("Г")
            E = stroka.count("Д")
            sp.append(E)
            letters.append("Д")
            F = stroka.count("Е")
            sp.append(F)
            letters.append("Е")
            G = stroka.count("Ё")
            sp.append(G)
            letters.append("Ё")
            H = stroka.count("Ж")
            sp.append(H)
            letters.append("Ж")
            I = stroka.count("З")
            sp.append(I)
            letters.append("З")
            J = stroka.count("И")
            sp.append(J)
            letters.append("И")
            K = stroka.count("Й")
            sp.append(K)
            letters.append("Й")
            L = stroka.count("К")
            sp.append(L)
            letters.append("К")
            M = stroka.count("Л")
            sp.append(M)
            letters.append("Л")
            N = stroka.count("М")
            sp.append(N)
            letters.append("М")
            O = stroka.count("Н")
            sp.append(O)
            letters.append("Н")
            P = stroka.count("О")
            sp.append(P)
            letters.append("О")
            Q = stroka.count("П")
            sp.append(Q)
            letters.append("П")
            R = stroka.count("Р")
            sp.append(R)
            letters.append("Р")
            S = stroka.count("С")
            sp.append(S)
            letters.append("С")
            T = stroka.count("Т")
            sp.append(T)
            letters.append("Т")
            U = stroka.count("У")
            sp.append(U)
            letters.append("У")
            V = stroka.count("Ф")
            sp.append(V)
            letters.append("Ф")
            W = stroka.count("Х")
            sp.append(W)
            letters.append("Х")
            X = stroka.count("Ц")
            sp.append(X)
            letters.append("Ц")
            Y = stroka.count("Ч")
            sp.append(Y)
            letters.append("Ч")
            Z = stroka.count("Ш")
            sp.append(Z)
            letters.append("Ш")
            op = stroka.count("Щ")
            sp.append(op)
            letters.append("Щ")
            op_1 = stroka.count("Ы")
            sp.append(op_1)
            letters.append("Ы")
            op_2 = stroka.count("Ъ")
            sp.append(op_2)
            letters.append("Ъ")
            op_3 = stroka.count("Э")
            sp.append(op_3)
            letters.append("Э")
            op_4 = stroka.count("Ь")
            sp.append(op_4)
            letters.append("Ь")
            op_5 = stroka.count("Ю")
            sp.append(op_5)
            letters.append("Ю")
            op_6 = stroka.count("Я")
            sp.append(op_6)
            letters.append("Я")
            a = stroka.count("а")
            sp.append(a)
            letters.append("а")
            b = stroka.count("б")
            sp.append(b)
            letters.append("б")
            c = stroka.count("в")
            sp.append(c)
            letters.append("в")
            d = stroka.count("г")
            sp.append(d)
            letters.append("г")
            e = stroka.count("д")
            sp.append(e)
            letters.append("д")
            f = stroka.count("е")
            sp.append(f)
            letters.append("е")
            g = stroka.count("ё")
            sp.append(g)
            letters.append("ё")
            h = stroka.count("ж")
            sp.append(h)
            letters.append("ж")
            i = stroka.count("з")
            sp.append(i)
            letters.append("з")
            j = stroka.count("и")
            sp.append(j)
            letters.append("и")
            k = stroka.count("й")
            sp.append(k)
            letters.append("й")
            l = stroka.count("к")
            sp.append(l)
            letters.append("к")
            m = stroka.count("л")
            sp.append(m)
            letters.append("л")
            n = stroka.count("м")
            sp.append(n)
            letters.append("м")
            o = stroka.count("н")
            sp.append(o)
            letters.append("н")
            p = stroka.count("о")
            sp.append(p)
            letters.append("о")
            q = stroka.count("п")
            sp.append(q)
            letters.append("п")
            r = stroka.count("р")
            sp.append(r)
            letters.append("р")
            s = stroka.count("с")
            sp.append(s)
            letters.append("с")
            t = stroka.count("т")
            sp.append(t)
            letters.append("т")
            u = stroka.count("у")
            sp.append(u)
            letters.append("у")
            v = stroka.count("ф")
            sp.append(v)
            letters.append("ф")
            w = stroka.count("x")
            sp.append(w)
            letters.append("x")
            x = stroka.count("ц")
            sp.append(x)
            letters.append("ц")
            y = stroka.count("ч")
            sp.append(y)
            letters.append("ч")
            z = stroka.count("ш")
            sp.append(z)
            letters.append("ш")
            po_1 = stroka.count("щ")
            sp.append(po_1)
            letters.append("щ")
            po_2 = stroka.count("ы")
            sp.append(po_2)
            letters.append("ы")
            po_3 = stroka.count("ъ")
            sp.append(po_3)
            letters.append("ъ")
            po_4 = stroka.count("э")
            letters.append("э")
            sp.append(po_4)
            po_5 = stroka.count("ь")
            sp.append(po_5)
            letters.append("ь")
            po_6 = stroka.count("ю")
            sp.append(po_6)
            letters.append("ю")
            po_7 = stroka.count("я")
            sp.append(po_7)
            letters.append("я")
    print(sp)
    print(letters)
    # создаем из двух список с помощью генератора словарь
    Dictionary = {letters[i]: sp[i] for i in range(len(letters))}
    # сортируем словарь по значению в обратном порядке
    sorted_num_frequency = sorted(Dictionary.items(), key=lambda element: element[1], reverse=True)
    total = ("\n".join(map(str, list(sorted_num_frequency))))
    with open(FILENAME1, 'w') as myfile:
            myfile.write(total)

