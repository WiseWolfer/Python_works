import numpy as np
import random


maxres = 0
maxmatrx = []
A = np.array([[10, 3, 12, 13],
              [16, 18, 20, 22],
              [37, 25, 33, 28],
              [70, 33, 45, 36]]) #Объем СМР

n = 1000

matrixfinal = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]] # наилучший вариант распределения бригад по объектам

matrixfinal_CMR = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
for z in range(n):
    # список из рандомных чисел
    lister = []
    random_kolvo = 0
    random_kolvo2 = 0
    random_kolvo3 = 0
    kol = 4
    # кол-во людей на объекты
    list = 0
    list2 = 0
    list3 = 0
    list4 = 0
    print('Испытание', z + 1, '_____________________________________________')
    random_kolvo = random.random()   # рандом количества бригад на 1 объект
    list = int(0+(kol-0+1)*random_kolvo)
    if list < kol:
        random_kolvo2 = random.random()
        list2 = int(0+(kol-list + 1 - 0)*random_kolvo2)
        if list2 < kol-list:
            random_kolvo3 = random.random()
            list3 = int(0 + (kol - list - list2 + 1 - 0) * random_kolvo3)
            if list3 < kol-list-list2:
                list4 = kol-list-list2-list3
            else:
                list4 = 0
        else:
            list3 = 0
            list4 = 0
    else:
        list2 = 0
        list3 = 0
        list4 = 0
    print(f'Случайное значение для 1 объекта = {random_kolvo}, Распределение на 1 объект = {list * 10}')
    if random_kolvo2 > 0:
        print(f'Случайное значение для 2 объекта = {random_kolvo2}, Распределение на 2 объект = {list2 * 10}')
    else:
        print(f'Распределение на 2 объект = {list2 * 10}')
    if random_kolvo3 > 0:
        print(f'Случайное значение для 3 объекта = {random_kolvo3}, Распределение на 3 объект = {list3 * 10}')
    else:
        print(f'Распределение на 3 объект = {list3 * 10}')
    print(f'Распределение на 4 объект = {list4*10}')
    # распределение бригад на объекты(печать матрицы)
    lest = []  # записываем бригады для печати
    lest2 =[1, 2, 3, 4] # записываем объекты для печати
    lest.append(list)
    lest.append(list2)
    lest.append(list3)
    lest.append(list4)

    matrix2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # матрица СМР для испытания
    result = 0 # объём СМР
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # матрица распределения рабочих
                                                                        # для каждого испытания
    for i in range(4):
        if lest[i] !=0:
            matrix[lest[i]-1][lest2[i]-1] = 1
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print(matrix[3])
    for i in range(4):
        for j in range(4):
            matrix2[i][j] = matrix[i][j] * A[i][j]
    for i in range(4):
        for j in range(4):
            result += matrix2[i][j]
    print('СМР:', result)

    if result >= maxres:
        maxres=result
        matrixfinal = matrix
        matrixfinal_CMR = matrix2
print('_________________________')
print(matrixfinal[0])
print(matrixfinal[1])
print(matrixfinal[2])
print(matrixfinal[3])
print('максимальное СМР=', maxres)
print(matrixfinal_CMR[0])
print(matrixfinal_CMR[1])
print(matrixfinal_CMR[2])
print(matrixfinal_CMR[3])
