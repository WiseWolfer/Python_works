import numpy as np
import random
maxres = 9999999999
maxmatrx = []
A = np.array([[30, 40, 50, 60],
              [33, 43, 53, 58],
              [23, 44, 49, 53],
              [35, 33, 43, 63]])#Распределяем по объектам

obj_inter1 = [0,0.25,0.5,0.75,1] # интервалы по объектам для первой бригады
obj_inter2 = [0,0.33,0.66,1] # интервалы по объектам для второй бригады
obj_inter3 = [0,0.5,1] # интервалы по объектам для третьей бригады

brig_inter1 = [0,0.25,0.5,0.75,1] # интервалы по бригадам для первого объекта
brig_inter2 = [0,0.33,0.66,1] # интервалы по бригадам для второго объекта
brig_inter3 = [0,0.5,1] # интервалы по бригадам для третьего объекта
n= 1000
for z in range(n):
    object = [1, 2, 3, 4]
    brig = [1, 2, 3, 4]
    vibor_brig = []
    vibor_obj = []
    print(f'-----Испытание № {z + 1}----- ')
    # для первой бригады
    rand_obj = random.random()
    print(f'Случайное число для 1 объекта = {rand_obj}')
    for i in range(len(obj_inter1)):
        if obj_inter1[i] < rand_obj <= obj_inter1[i + 1]:
            vibor_obj.append(object[i])
            object.pop(i)
    # для второй бригады
    rand_obj = random.random()
    print(f'Случайное число для 2 объекта = {rand_obj}')
    for i in range(len(obj_inter2)):
        if obj_inter2[i] < rand_obj <= obj_inter2[i + 1]:
            vibor_obj.append(object[i])
            object.pop(i)
    #для треьей бригады
    rand_obj = random.random()
    print(f'Случайное число для 3 объекта = {rand_obj}')
    for i in range(len(obj_inter3)):
        if obj_inter3[i] < rand_obj <= obj_inter3[i + 1]:
            vibor_obj.append(object[i])
            object.pop(i)
    # остаток идет для 4 бригады
    for j in range(1):
        if object[j] not in vibor_obj:
            vibor_obj.append(object[j])
    print(f'Рандомные номера объектов: {vibor_obj}')

    # для первого объекта
    rand_brig = random.random()
    print(f'Случайное число для 1 бригады = {rand_brig}')
    for i in range(len(brig_inter1)):
        if brig_inter1[i] < rand_brig <= brig_inter1[i + 1]:
            vibor_brig.append(brig[i])
            brig.pop(i)
    # для второго объекта
    rand_brig = random.random()
    print(f'Случайное число для 2 бригады = {rand_brig}')
    for i in range(len(brig_inter2)):
        if brig_inter2[i] < rand_brig <= brig_inter2[i + 1]:
            vibor_brig.append(brig[i])
            brig.pop(i)
    #для треьего объекта
    rand_brig = random.random()
    print(f'Случайное число для 3 бригады = {rand_brig}')
    for i in range(len(brig_inter3)):
        if brig_inter3[i] < rand_brig <= brig_inter3[i + 1]:
            vibor_brig.append(brig[i])
            brig.pop(i)
    # остаток идет для 4 объекта
    for j in range(1):
        if brig[j] not in vibor_brig:
            vibor_brig.append(brig[j])
    print(f'Рандомные номера бригад: {vibor_brig}')
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        a = vibor_brig[i]
        b = vibor_obj[i]
        matrix[a - 1][b - 1] = 1
    print(f'Матрица распределения: {matrix}')
    result = 0
    matrix2 = matrix
    for i in range(4):
        for j in range(4):
            matrix2[i][j] = matrix2[i][j] * A[i][j]
    for i in range(4):
        for j in range(4):
            result += matrix2[i][j]
    print(f'Суммарный срок выполнения всех работ = {result}')
    if result <= maxres:
        maxres = result
        maxmatrx = matrix
print('_________________________')
print('Минимальный срок выполнения работ', maxres)
print('Матрица распределения бригад по объектам:')
print(maxmatrx[0])
print(maxmatrx[1])
print(maxmatrx[2])
print(maxmatrx[3])
print('_________________________')


