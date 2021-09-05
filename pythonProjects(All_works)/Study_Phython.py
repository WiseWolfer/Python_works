# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:00:06 2021

@author: dimac
"""

#Посчитаем Периметр и Площадь квадрата

#a = int(input("Введите сторону квадрата: "))
# b = 20
# def count(a):
#     global b
#     ##если хотим получить значение внутрь функции пишем глобал перед переменной
#     b = 40
#     Perimeter = a * 4
#     Square = a * a
#     Perimeter_b = b * 4
#     Square_b = b * b 
#     print("Площадь квадрата:  ", Square)
#     print("Периметр квадрата: ", Perimeter)
#     print("Площадь квадрата:  ", Square_b)
#     print("Периметр квадрата: ", Perimeter_b)
#count(a)
# пример с глобал (в итоге заменится имя в функции и будет Дима)
# name = 'Bulat'
#
# def print_hi():
#     global name
#     name = "Dima"
#     print("hello, " + name)
#
# print_hi()
##Задачи для тренировки:
##1) Найти произведение всех четных чисел от 1 до 100.
##2) Пользователь вводит два числа (a, b). 
##  Найти количество всех нечетных чисел, на диапазоне от a до b (a < b).


    
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i*i)
        
# i = 1
# while(i<=100):
    
#     if i % 2 == 0:  
#         b = i*i
#         print(b) 
#     i += 1

# a = int(input("Введите 1 число: "))
# b = int(input("Введите 2 число: "))
# counter = 0
# for i in range(a, b+1):
#     if i % 2 != 0:
#         counter += 1
        
# print("Количество элементов: ", counter)

# c = int(input("Введите 1 число: "))
# d = int(input("Введите 2 число: "))
# count = 0
# while(c <= d):
#     if c % 2 != 0:
#         count += 1
#     c = c + 1
# print(count)

##Пример со строками
# name = "Диман - любит питон"
# counter = 0
# for a in range(1,21):
#     print(name)
#     counter += 1
    
# print(counter)

##пример с брейком и континью
# for i in range(1,12):
#     if i % 2 != 0:
#         print(i)
#     elif i == 8:
#         break;
#     else:
#         continue

##Дан список чисел. Превратить его в список квадратов этих чисел

# numbers = [5, 25, 16 ,64 ,32, 78, 100]  

# numbers.sort()
# counter = 0;
# print("Отсортированный список чисел: ", numbers)
# for num in numbers:
#     counter += 1;
#     print(counter, ':', num*num)

# #захватываем индекс элемента
# position = numbers.index(16)  

# #записываем что-то в список
# numbers.append("какое-то число")

# #удаляем последний элемент
# numbers.pop(-1)

# ##записываем длину списка
# k = len(numbers);
# #тоже самое только через for по range
# for i in range(0, k):
#     if i == position:
#           print("Позиция найдена\n")
#           numbers.pop(i) 
#     else:
#         continue

##тоже самое только через while
# k = len(numbers);
# print(k)
# i = 0;
# while(i != k):
#     if i == 1:
#           print("Позиция найдена\n")
#           numbers.pop(i) 
#     i+=1
# print("Результат после удаления 16: ", numbers)

##кортежи (tuple) и словари

##кортежи

# tuple = ("first", 2, 25 ,10, 15,) ## в картежах пишем в конце значений ставим ,

# print(tuple)

# print(type(tuple)) ##преобразование в класс tuple

#теперь картеж список
# print(list(("first", 2, 25 ,10, 15,)))

# #теперь список стал картеж
# print(tuple(["first", 2, 25 ,10, 15]))

# ##словари (у него есть два поля ключ и значения)

# dict = {"яблоко": "красное", "банан": "желтый", "лимон": "желтый"}
# print(dict)

# for key in dict.keys():
#     print(key)

# print("\n")    

# for value in dict.values():
#         print(value)

# print("\n")         

# for full_dict in dict.items():
#     print(full_dict)
        
# ## выводим по ключу значение
# print(dict["лимон"])    
# ## меняем значение ключа
# dict["лимон"] = "оранжевый"
# dict["лимон"] = "зеленый"

# print(dict)
# print("\n") 
# ##удаление элемента по ключу
# del(dict["лимон"])

# for i in dict.items():
#     print(i)
    
#работа со строками
##способ вывода текста как нам нужно, одним абзацем, например
# print("""Привет, мир!!!
# Дима учит питон!!
# бла-бла-бла""")
# print("Привет, мир!\nПривет, мир!\nПривет, мир!")
# print("\tПривет, мир!\n\tПривет, мир!\n\tПривет, мир!")

# print('"Текст в кавычках"') 

# print("'Текст в опострофах'")  

# ##оборачиваем какой-то символ в кавычки 
# print("Текст \"в\" кавычках")

# text = "Привет, "
# text1 = "мир!"
# text_2 ="Привет, мир! "
# print(text + text1)
# print("\n")
# print(text_2 * 5)
# text = "Привет"
# text1 = "мир"
# print(text[0:7])
# print("\n")

# #метод повышения регистра букв
# print(text.upper())

# #метод понижения регистра букв
# print(text.lower())

# #метод написания текста как в предложении
# print(text1.capitalize())
# text = "привет мир куда идешь"

# ##разбиваем слово, делим пробелом, и все содержимое записывается в список
# split_object = text.split(" ")
# print(split_object)

# ##создаем список и из него делаем строку 
# spisok = ['a','b','c']
# #print(tuple((spisok)))
# #преобразовал в кортеж список и потом его в строку
# print(','.join(tuple(spisok)))
# #преобразовал список  в строку
# print(','.join(spisok))

# #метод убирает пробелы слева и справа от текста
# text = "               привет мир куда идешь               "
# print(text.strip())

# #метод убирает пробелы слева от текста
# #print(text.lstrip())

# #метод убирает пробелы справа текста
# #print(text.rstrip())

# ##метод замены буквы на букву
# text1 ="olololololol"
# print(text1.replace("l", "o")) 

##открытие файла на чтение

#f = open("Spisok.txt", "w")
#f.write("Привет, файл!")

#открытие файла на чтение
#f = open("Spisok.txt", "r")
#print(f.read())
#f.close()

#на добавление и имя переменной, файл автоматически закрывается
# with open("Spisok.txt", "a") as f:
#     f.write("бугага")

#Блок обработки исключений

# try:    
#     a = int(input())
#     b = int(input())
#     print(a/b)
# except ZeroDivisionError:
#     print("На 0 делить нельзя!")

#Создаем класс в питоне

# class House():
#     """описание дома"""
#     def __init__(self, street, number):
#         """свойства дома"""
#         self.street = street
#         self.number = number
#         self.age = 0
        
#     def build(self):
#         """строит дом"""
#         print("Дом на улице " + self.street + " под номером " + 
#               str(self.number) + " построен.") 
        
#     def ageofhouse(self, year):
#         """возраст дома"""
#         self.age += year

# House1 = House("Московская", 20)
# House2 = House("Московская", 21) 
# print(House1.street) ##обращаемся к улице
# print(House2.number) ##обращаемся к номеру
# ##вызываем метод по объекту
# House1.build()
# House1.ageofhouse(5)
# print(House1.age)

## Наследование

# class ProspectHouse(House):
#     """Дома на проспекте"""
#     def __init__(self,  prospect, number):
#         super().__init__(self, number)    ##связываем потомка с родителем
#         self.prospect = prospect
        
# PrHouse = ProspectHouse("проспект Ленина ", 5)
# print(PrHouse.prospect, PrHouse.number)

# Множества
##Пустое множество
#numbers = set()
#оборачиваем список в множество - теперь
#нет дубликатов
#num =set([1, 1, 2, 4, 2, 5, 6, 7, 8, 10])
#print(type(numbers))
##вывод поэлементно множество на экран
#for i in num:
#    print(i)

#print(num)
##Проверяем входит ли элемент в множество
#print(2 in num)
##Добавляем элемент в множество
#.add(58)
# print(num)
##удаление элемента из множества
# num.discard(58)
#его фишка в том, что если эл-та не будет
#в множестве, то ошибки не будет
# если мы используем метод remove()
# то ошибка уже будет в случае, когда
# элемента нет во множестве
#удаление первого жлемента из множества
# num.pop()
# print(num)
num = {1, 1, 2, 4, 2, 5, 6, 7, 8, 10}
##удаление всех элементов множества
# num.clear()
# print(num)
num2 = {1, 2, 3, 4, 5, 6, 7 ,8}
#объединение нескольких множеств в одно
#num3 = num.union(num2)
##или так объединяем
# num3 = num | num2
# print(num3)
#Берем элементы которые есть и в первом
#множестве и во втором
# num3 = num.intersection(num2)
# num3 = num & num2
# print(num3)
#Элемнты которые есть в первом множестве
#но этого/их элементов нет во втором
#num3= num - num2
#print(num3)
##тоже самое только теперь элементы
## берем из второго множества только, которых
# нет во втором
#num3 = num2 - num
#print(num3)
#копируем элементы из какого-либо множества
num3 = num2.copy()
##определяем кол-во элементов во множестве
print(len(num3))
#frozenset - тип множества, который нельзя изменить
#numbers = frozenset({2, 4, 6, 7, 8, 10})
#на этой строке выйдет ошибка при добавлении во множество, которое неизменяемое
#numbers.add(8)
#print(numbers)
