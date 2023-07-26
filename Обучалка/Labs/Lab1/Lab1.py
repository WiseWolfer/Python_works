# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # 1) По введенному году выводит сообщение является ли год високусным
    # в соответствии с григорианским календарем, год является високосным,
    # если его номер кратен 4, но не кратен 100, а также если он кратен 400.
    year = int(input("Введите какой-то год: "))
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Год - високосный!")
    else:
        print("Год - невисокосный!")

    # найти все трехзначные и четрырехзначные числа Армстронга
    # number = int(input("Введите трехзначное или четырехзначное число:"))
    # counter = 0
    # summa = 0
    # while True:
    #     a = number // 1000 #- самое первое число слева
    #     b = number // 100 % 10 #- перед первым числом
    #     c = number // 10 % 10 #- перед числом за первым
    #     d = number % 10 #- последнее число
    #     counter += 1
    #     if counter == 3 and a == 0:
    #         summa = pow(a, counter) + pow(b, counter) + pow(c, counter) + pow(d, counter)
    #         break
    #     if counter == 4 and a != 0:
    #         summa = pow(a, counter) + pow(b, counter) + pow(c, counter) + pow(d, counter)
    #         break
    # print(counter)
    # print(summa)

# задача фибоначчи
# arr = list(map(int, input("Введите числа: ").split()))
#
# print(len(arr))
# for i in range(2, len(arr)):
#     if arr[i] == arr[i - 1] + arr[i - 2]:
#         print("Последовательность Фибоначчи!")
#         break
#     else:
#         print("Не последовательность Фибоначчи!")
#         break
# sp = list([1, 1, 2, 3, 5, 8])
sp = list(map(int, input("Numbers: ").split()))
print(sp)
print(len(sp))
for i in range(2, len(sp)):
    print(sp[2])
    if sp[i] == sp[i-1] + sp[i-2]:
        print("Последовательность Фибоначчи!")
        break
    else:
        print("Не последовательность Фибоначчи!")
        break
#Задание №2. Последовательно вводятся ненулевые числа.
#Определить сумму положительных и сумму отрицательных чисел.
#Закончить ввод чисел при вводе 0.
# neg = 0
# pos = 0
# n = int(input("Введите числа: \n"))
# while n != 0:
#     if n < neg:
#         neg += n
#     else:
#         pos += n
#     n = int(input())
#
# print("neg =", neg)
# print("pos =", pos)

# Напишите скрипт, который запрашивает натуральное число N и
# выводит на экран все автоморфные числа, не превосходящие N.
# Автоморфным называется натуральное число, если оно равно последним
# цифрам своего квадрата. Например, 25^2 = 625.
# N = int(input("Введите число: "))
# mod = 10
# for i in range(1, N + 1):
#     if i == mod:
#         mod *= 10
#     if (i * i) % mod == i:
#         print(i)


# Задание №3. Распечатывать дни недели с их порядковыми номерами. Кроме
# того, рядом выводить, выходной это день или рабочий. Использовать кортеж
# week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# for i in range(0, len(week)):
#     if week[i] == "Saturday" or week[i] == "Sunday":
#         print("Порядковый номер " + str(i+1) + ":", str(week[i]) + " - выходной")
#     else:
#         print("Порядковый номер " + str(i+1) + ":", str(week[i]) + " - рабочий")

# Дополнительное задание
# Будем называть положительное целое число «магическим», если сумма его цифр
# равна 10. Вам дано целое число k, найдите k-е по величине прекрасное «магическое»
# целое число.

# Входные данные
# Пользователь вводит целое число k (1 ≤ k ≤ 10000).
#
# Выходные данные
# # Выведите k-е по величине «магическое» число.
# k_number = int(input("Введите целое число k,(1 ≤ k ≤ 10000): "))
# if k_number < 1:
#     print("Вы ввели число в неправильном диапазоне!")
# summa = 0
# for i in range(k_number, 10000 + 1):
#     a = i // 1000 #- самое первое число слева
#     b = i // 100 % 10 #- перед первым числом
#     c = i // 10 % 10 #- перед числом за первым
#     d = i % 10 #- последнее число
#     summa = a + b + c + d
#     if summa == 10:
#         print("k-ое по величине прекрасное «магическое» целое число: ", i)
#         break

