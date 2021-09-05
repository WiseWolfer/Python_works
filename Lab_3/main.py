# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # old_list = ['1','2','3','4','5','6']
    # new_list = []
    # for item in old_list:
    #     new_list.append(int(item))
    # print(new_list)

    # если использовать функцию map(),
    # то можно сделать тоже самое короче
    # old_list = ['1', '2', '3', '4', '5', '6']
    # new_list = list(map(int, old_list))
    # print(new_list)

    # еще один пример, только еще с лямбда выражением
    # переводим мили в километры
    # mile_distance = [1.0, 6.5, 17.4, 2.4, 9]
    # пишем функцию map(),обернув ее в list(),
    # внутри lambda выражение (lambda переменная: действие с переменной, аргумент(ы))
    # kilometers_per_hour = list(map(lambda x: x * 1.6, mile_distance))
    # print(kilometers_per_hour)

    # map() действуем с несколькими списками
    # l1 = [1, 2, 3]
    # l2 = [4, 5, 6]
    # new_list = list(map(lambda x, y: x+y, l1, l2))
    # print(new_list)

    # выполнение функции закончится на меньшем списке
    # l1 = [1, 2, 3]
    # l2 = [4, 5]
    # new_list = list(map(lambda x, y: x+y, l1, l2))
    # print(new_list)

    # функция filter
    # помогает отфильтровать последовательность
    # ищем все положительные числа из списка
    # функция filter должна возвращать True или False,
    # чтобы аргументы корректно фильтровались
    # mixed = [1, 2, 3, -2, -3, 20, 5]
    # positive = list(filter(lambda x: x > 0, mixed))
    # print(positive)

    # reduce() принимает два аргумента: фуннкцию и последовательность
    # Функция reduce() последовательно применяется
    # к элементам последовательности, возвращает единичное значение
    # нужно импортировать модуль reduce() из библиотеки functools
    # from functools import reduce
    # items = [1, 2, 3, 4, 5]
    # sum_all = reduce(lambda x, y: x + y, items)
    # print(sum_all)

    # находим максимальное значение из списка с помощью reduce()
    # items = [1, 24, 17, 14, 9, 32, 2]
    # all_max = reduce(lambda a, b: a if (a > b) else b, items)
    # print(all_max)

    # функция zip() -> объединяет в кортежи элементы из
    # последовательностей, переданных в качестве аргументов
    # zip() прекращает работу как достигает конца самого короткого списка
    # a = [1, 2, 3]
    # b = "xyz"
    # c = (None, True)
    # res = list(zip(a, b, c))
    # print(res)

    # nonlocal указывает на то, что эта
    # переменная не является локальной,
    # следовательно, ее значение
    # будет взято из ближайшей области
    # видимости, в которой существует
    # переменная с таким же именем.
    # def counter():
    #     num = 0
    #     def incrementer():
    #         nonlocal num
    #         num += 1
    #         return num
    #     return incrementer
    # c = counter()
    # print(c()) # 1
    # print(c()) # 2
    # print(c()) # 3

    # этим условием обособляем тестируемую функцию
    # от других функций и можем запустить только её
    # if __name__ == "__main__":
    # инструкция (вызов тестируемой функции)



# Задание №4. Напишите функцию, которая принимает на вход два целых числа
# a, b и возвращает кортеж из чисел в промежутке [a:b], имеющих наибольшее
# количество делителей.
# и задание
# Задание №4. Напишите функцию, которая принимает на вход два целых числа
# a, b и возвращает кортеж из чисел в промежутке [a:b], имеющих наибольшее
# количество делителей.
# def main():
#     a = int(input("Введите левую границу кортежа: "))
#     b = int(input("Введите правую границу кортежа: "))
#     sp = list(map(int, range(a, b)))
#     test = []
#     print(sp)
#     # алгоритм поиска простого числа
#     for i in sp:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             test.append(i)
#     # алгоритм поиска составных чисел
#     contenner =[]
#     for i in sp:
#         for j in range(2, i):
#             if i % j == 0:
#                 contenner.append(i)
#                 break
#     res = tuple(test)
#     res_1 = tuple(contenner)
#     print(res)
#     print(res_1)

# Задание №5. Напишите функцию, которая принимает в качестве аргумента
# список и возвращает True, если все значения внутри данного списка уникальны,
# иначе возвращает False

def Unique_items(sp= []):
    counter = 0
    for i in range(len(sp)):
        for j in range(i+1, len(sp)):
            # сравниваем элементы списка пред. и след.
            if sp[i] != sp[j]:
                counter += 1
    if counter > 0:
        return True
    else:
        return False
def main():
    spisok = ["dog", "fox", 8, 5, 15, False]
    spisok_1 = ["fox", "fox", "fox", "fox", "fox", "fox"]
    # all() возвращает True или False если все жлементы в последовательноси
    # соответствуют условиям
    res = Unique_items(spisok)
    res_1 = Unique_items(spisok_1)
    # второй варинат функции выше, только покороче через all()
    #res = all(spisok[i] != spisok[i+1] for i in range(len(spisok)-1))
    #res_1 = all(spisok_1[i] != spisok_1[i + 1] for i in range(len(spisok_1) - 1))
    print(res)
    print(res_1)

# Напишите функцию, которая принимает произвольное число
# аргументов (каждый аргумент – список) и возвращает True если пересечение
# списков пустое, иначе возвращает False
# def search_spaces(sp=[]):
#     print(sp)
#     counter = 0
#     for i in range(len(sp)):
#        # есть ли пустой элемент в списке
#         if " " in sp[i]:
#             counter += 1
#     if counter > 0:
#         return True
#     else:
#         return False
#
# def main():
#     spisok = list(map(list, input("Списки: ")))
#     res = search_spaces(spisok)
#     print(res)
if __name__ == '__main__':
    main()

