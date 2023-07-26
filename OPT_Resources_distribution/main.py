from pulp import *
import numpy as np
import os
import pandas as pd

if __name__ == '__main__':
    # начальные таблицы значений
    # Продолжительность выполнения работ в ч.
    time_of_work_dict = {
        'Установка эл. розеток, выключателей': 61,
        'Монтаж щитков осветительных и электросчетчиков': 9.2,
        'Установка светильников': 2.8,
        'Монтаж эл. кабелей': 97.9,
        'Монтаж эл. звонков': 4.9
    }
    # Объём СМР в тыс.руб на одном этаже
    Volume_CMR_dict = {
        'Установка эл. розеток, выключателей': 76.0,
        'Монтаж щитков осветительных и электросчетчиков': 14.0,
        'Установка светильников': 4.8,
        'Монтаж эл. кабелей': 124.8,
        'Монтаж эл. звонков': 6.0
    }

    # ввод количества зданий в Микрорайоне
    total_num_of_houses = (int(input('Введите количество зданий в микрорайоне: ')))

    # свойство дома (общая этажность дома с учётом подъездов)
    house_properties = []
    print("Подсчитаем общую этажность дома с учетом этажности здания и кол-во подъездов")
    for i in range(total_num_of_houses):
        floor = int(input('Введите этажность здания: '))
        entrance = int(input('Введите кол-во подъездов: '))
        house_properties.append(floor * entrance)

    # списки для хранения трудозатрат и объёмов СМР в тыс.руб на объект
    time_of_work, Cost_of_volume_CMR = [], []
    for i in time_of_work_dict.values():
        time_of_work.append(i)
    for j in Volume_CMR_dict.values():
        Cost_of_volume_CMR.append(j)

    # Трудозатраты СМР в чел.ч
    time_of_work_dict_total = [[i * j for i in time_of_work] for j in house_properties]

    # Ведомость объёмов работ на объект
    table_of_volume_CMR = [[float("{0:.1f}".format(i * j))
                            for i in Cost_of_volume_CMR] for j in house_properties]

    # Трудозатраты СМР итог
    time_of_work_dict_total = np.sum(time_of_work_dict_total, axis=1)

    # Ведомость объёмов работ на объект итог
    table_of_volume_CMR = np.sum(table_of_volume_CMR, axis=1)

    # варианты распределения работников
    workers_distribution = [10, 20, 30, 40]
    # номера объектов
    numbers_of_obj = [1, 2, 3, 4, 5]
    # таблица рабочих и времени работы на пяти объектах. (Время выполнения электромонтажных работ в ч.)
    time_of_electric_works = np.array([
        [round(time_of_work_dict_total[0] / workers_distribution[0] / 1.03),
         round(time_of_work_dict_total[1] / workers_distribution[0] / 1.03),
         round(time_of_work_dict_total[2] / workers_distribution[0] / 1.03),
         round(time_of_work_dict_total[3] / workers_distribution[0] / 1.03),
         round(time_of_work_dict_total[4] / workers_distribution[0] / 1.03)],
        [round(time_of_work_dict_total[0] / workers_distribution[1] * 1.04),
         round(time_of_work_dict_total[1] / workers_distribution[1] * 1.04),
         round(time_of_work_dict_total[2] / workers_distribution[1] * 1.04),
         round(time_of_work_dict_total[3] / workers_distribution[1] * 1.04),
         round(time_of_work_dict_total[4] / workers_distribution[1] * 1.04)],
        [round(time_of_work_dict_total[0] / workers_distribution[2] * 1.05),
         round(time_of_work_dict_total[1] / workers_distribution[2] * 1.05),
         round(time_of_work_dict_total[2] / workers_distribution[2] * 1.05),
         round(time_of_work_dict_total[3] / workers_distribution[2] * 1.05),
         round(time_of_work_dict_total[4] / workers_distribution[2] * 1.05)],
        [round(time_of_work_dict_total[0] / workers_distribution[3]),
         round(time_of_work_dict_total[1] / workers_distribution[3]),
         round(time_of_work_dict_total[2] / workers_distribution[3]),
         round(time_of_work_dict_total[3] / workers_distribution[3]),
         round(time_of_work_dict_total[4] / workers_distribution[3])]])
    # таблица рабочих и объёмов СМР, распределенных по пяти объектам.
    # (Выработка в тыс.руб./бригаду при различном кол-ве рабочих)
    table_of_volume_CMR_with_brigades = np.array([
        [round(table_of_volume_CMR[0] / workers_distribution[3] * workers_distribution[0] * 1.03),
         round(table_of_volume_CMR[1] / workers_distribution[3] * workers_distribution[0] * 1.03),
         round(table_of_volume_CMR[2] / workers_distribution[3] * workers_distribution[0] * 1.03),
         round(table_of_volume_CMR[3] / workers_distribution[3] * workers_distribution[0] * 1.03),
         round(table_of_volume_CMR[4] / workers_distribution[3] * workers_distribution[0] * 1.03)],
        [round(table_of_volume_CMR[0] / workers_distribution[3] * workers_distribution[1] * 1.04),
         round(table_of_volume_CMR[1] / workers_distribution[3] * workers_distribution[1] * 1.04),
         round(table_of_volume_CMR[2] / workers_distribution[3] * workers_distribution[1] * 1.04),
         round(table_of_volume_CMR[3] / workers_distribution[3] * workers_distribution[1] * 1.04),
         round(table_of_volume_CMR[4] / workers_distribution[3] * workers_distribution[1] * 1.04)],
        [round(table_of_volume_CMR[0] / workers_distribution[3] * workers_distribution[2] * 1.05),
         round(table_of_volume_CMR[1] / workers_distribution[3] * workers_distribution[2] * 1.05),
         round(table_of_volume_CMR[2] / workers_distribution[3] * workers_distribution[2] * 1.05),
         round(table_of_volume_CMR[3] / workers_distribution[3] * workers_distribution[2] * 1.05),
         round(table_of_volume_CMR[4] / workers_distribution[3] * workers_distribution[2] * 1.05)],
        [round(table_of_volume_CMR[0]), round(table_of_volume_CMR[1]), round(table_of_volume_CMR[2]),
         round(table_of_volume_CMR[3]), round(table_of_volume_CMR[4])]])
    print(table_of_volume_CMR_with_brigades)
    # определяем максимальный объём ресурсов
    C = max(workers_distribution)
    time_in_obj = int(input("Введите сколько времени могут работать электромонтажники на объектах: "))
    # Неизвестные
    variables = np.array([
        [pulp.LpVariable("v11", lowBound=0, cat='Binary'), pulp.LpVariable("v12", lowBound=0, cat='Binary'),
         pulp.LpVariable("v13", lowBound=0, cat='Binary'), pulp.LpVariable("v14", lowBound=0, cat='Binary'),
         pulp.LpVariable("v15", lowBound=0, cat='Binary')],
        [pulp.LpVariable("v21", lowBound=0, cat='Binary'), pulp.LpVariable("v22", lowBound=0, cat='Binary'),
         pulp.LpVariable("v23", lowBound=0, cat='Binary'), pulp.LpVariable("v24", lowBound=0, cat='Binary'),
         pulp.LpVariable("v25", lowBound=0, cat='Binary')],
        [pulp.LpVariable("v31", lowBound=0, cat='Binary'), pulp.LpVariable("v32", lowBound=0, cat='Binary'),
         pulp.LpVariable("v33", lowBound=0, cat='Binary'), pulp.LpVariable("v34", lowBound=0, cat='Binary'),
         pulp.LpVariable("v35", lowBound=0, cat='Binary')],
        [pulp.LpVariable("v41", lowBound=0, cat='Binary'), pulp.LpVariable("v42", lowBound=0, cat='Binary'),
         pulp.LpVariable("v43", lowBound=0, cat='Binary'), pulp.LpVariable("v44", lowBound=0, cat='Binary'),
         pulp.LpVariable("v45", lowBound=0, cat='Binary')], ])
    print(variables)
    # формулировка задачи(цели) и ее максимизация
    problem = pulp.LpProblem('Volume_CMR_maximization', LpMaximize)
    # математическая запись целевой функции
    problem += np.sum(variables * table_of_volume_CMR_with_brigades), 'Aim_Function'
    # Constraints(ограничения) по ресурсам
    problem += (np.sum(variables[0]) * workers_distribution[0] +
                np.sum(variables[1]) * workers_distribution[1] +
                np.sum(variables[2]) * workers_distribution[2] +
                np.sum(variables[3]) * workers_distribution[3]) == C
    # Constraints(ограничения) по работникам, на каждом объекте только 1 рабочий
    problem += np.sum(variables[:, 0]) <= 1
    problem += np.sum(variables[:, 1]) <= 1
    problem += np.sum(variables[:, 2]) <= 1
    problem += np.sum(variables[:, 3]) <= 1
    problem += np.sum(variables[:, 4]) <= 1
    # Constraints(ограничения) по времени работы на объектах
    problem += (np.sum(variables[:, 0] * time_of_electric_works[:, 0])) <= time_in_obj
    problem += (np.sum(variables[:, 1] * time_of_electric_works[:, 1])) <= time_in_obj
    problem += (np.sum(variables[:, 2] * time_of_electric_works[:, 2])) <= time_in_obj
    problem += (np.sum(variables[:, 3] * time_of_electric_works[:, 3])) <= time_in_obj
    problem += (np.sum(variables[:, 4] * time_of_electric_works[:, 4])) <= time_in_obj
    # поиск решения
    status = problem.solve()
    # хранится распределение рабочих
    matrix_distribution = []
    # Выводим результат
    print("Результат: ")
    c = 0
    i = 0
    for variable in problem.variables():
        if c == 0:
            print(f'\t', f'Распределение по {workers_distribution[i]} чел.:', end='| ')
        print(variable.varValue, end=' ')
        matrix_distribution.append(int(variable.varValue))
        if c == 4:
            print('|\n', end=' ')
            i += 1
            c = 0
        else:
            c += 1
    print(f"Общий объём CМР на электромонтажные работы: {value(problem.objective)} тыс.руб.")

    m = 5  # делим вектор по 5 элементов в строке и превращаем его в матрицу через генератор
    matrix_distribution = list([matrix_distribution[i:i + m] for i in range(0, len(matrix_distribution), m)])
    result_CMR = []
    # список содержащий численность бригад в соответствии их распределением по объектам
    result_brigades = []
    # записываем численность бригад в соответствии их распределением по объектам
    for i in range(4):
        for j in range(5):
            if matrix_distribution[i][j] == 1 and i == 0:
                result_brigades.append(10)
            elif matrix_distribution[i][j] == 1 and i == 1:
                result_brigades.append(20)
            elif matrix_distribution[i][j] == 1 and i == 2:
                result_brigades.append(30)
            elif matrix_distribution[i][j] == 1 and i == 3:
                result_brigades.append(40)
    # формируем объём СМР, который сделает каждая бригада на объектах в результате распределения,
    # чтобы получился макс.объём СМР
    for i in range(4):
        for j in range(5):
            a = matrix_distribution[i][j] * table_of_volume_CMR_with_brigades[i][j]
            if a != 0:
                result_CMR.append(a)
    # проверяем какие на какие номера объектов пошли рабочие и записываем их
    # Наименование каждого объекта
    first, second, third, forth, fifth = ' ', ' ', ' ', ' ', ' '
    # список для хранения наименований объектов
    obj_finder = []
    for k in range(len(numbers_of_obj)):
        for j in range(len(result_CMR)):
            if k == 0 and j + 1 == numbers_of_obj[k]:
                first = 'Объект № 1 (Жилой дом- 8 этажей, 3 подъезда, 192 кв.)'
                obj_finder.append(first)
            elif k == 1 and j + 1 == numbers_of_obj[k]:
                second = 'Объект № 2 (Жилой дом - 9 этажей, 3 подъезда, 216 кв.)'
                obj_finder.append(second)
            elif k == 2 and j + 1 == numbers_of_obj[k]:
                third = 'Объект № 3 (Жилой дом- 12 этажей, 1 подъезда, 96 кв.)'
                obj_finder.append(third)
            elif k == 3 and j + 1 == numbers_of_obj[k]:
                forth = 'Объект № 4 (Жилой дом- 14 этажей, 1 подъезда, 112 кв.)'
                obj_finder.append(forth)
            elif k == 4 and j + 1 == numbers_of_obj[k]:
                fifth = 'Объект № 5 (Жилой дом- 16 этажей, 1 подъезда, 128 кв.)'
                obj_finder.append(fifth)

    # получаем Затраты труда в чел.ч
    labour_cost = []
    for i in range(len(result_CMR)):
        res = int(result_CMR[i] * time_of_work_dict_total[i] / table_of_volume_CMR[i])
        labour_cost.append(res)

    # список для храниния продолжительность работы в днях на каждом объекте
    time_of_work_workers = []
    # рабочие дни работы на каждом объекте в сентябре 2022
    work_days_in_september = [1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 26, 27, 28, 29, 30]
    for j in range(len(labour_cost)):
        time_of_work_workers.append(round(labour_cost[j] / result_brigades[j] / 8))
    # формируем график работы на каждый рабочих день сентября на каждом объекте
    first_obj_days = []
    second_obj_days = []
    graphic_days = []
    counter1 = 0
    for i in range(len(time_of_work_workers)):
        counter1 += 1
        for k in range(time_of_work_workers[i]):
            if counter1 != len(time_of_work_workers):
                first_obj_days.append(work_days_in_september[k])
            elif counter1 == len(time_of_work_workers):
                second_obj_days.append(work_days_in_september[k])
    graphic_days.append(first_obj_days)
    graphic_days.append(second_obj_days)

    # создаем датафрейм для вывода в excel
    df = pd.DataFrame({'Наименование объекта': obj_finder,
                       'Стоимость СМР в тыс.руб.': result_CMR,
                       'Затраты труда, в чел.ч': labour_cost,
                       'Численность бригады, чел.': result_brigades,
                       'Продолжительность в дн.': time_of_work_workers,
                       'График работы (Сентябрь 2022, рабочие дни)': graphic_days})
    # запись содержимого в файл
    writer = pd.ExcelWriter('kalendarniy_plan.xlsx')
    df.to_excel(writer, sheet_name='kalendarniy_plan', index=False, na_rep='NaN')
    # выравнивание текста в колонках по ширине
    for column in df:
        column_width = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        writer.sheets['kalendarniy_plan'].set_column(col_idx, col_idx, column_width)
    writer.save()
    print('Календарный план записан в файл excel в локальный каталог!')
    os.system("pause")
