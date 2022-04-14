from pulp import *
import numpy as np

if __name__ == '__main__':
    # начальные таблицы значений
    time_of_work_dict = {
        'Установка эл. розеток, выключателей': 61,
        'Монтаж щитков осветительных и электросчетчиков': 9.2,
        'Установка светильников': 2.8,
        'Монтаж эл. кабелей': 97.9,
        'Монтаж эл. звонков': 4.9
    }
    Volume_CMR_dict = {
        'Установка эл. розеток, выключателей': 76,
        'Монтаж щитков осветительных и электросчетчиков': 14,
        'Установка светильников': 4.8,
        'Монтаж эл. кабелей': 124.8,
        'Монтаж эл. звонков': 6
    }
    # ввод количества зданий в Микрорайоне
    total_num_of_houses = (int(input('Введите количество зданий в микрорайоне: ')))
    # свойство дома
    house_properties = []
    print("Подсчитаем общую этажность дома с учетом этажности здания и кол-во подъездов")
    for i in range(total_num_of_houses):
        floor = int(input('Введите этажность здания: '))
        entrance = int(input('Введите кол-во подъездов: '))
        house_properties.append(floor * entrance)
    # составим таблицу времени выполнения работ в чел.ч
    time_of_work = []
    Cost_of_volume_CMR = []
    for i in time_of_work_dict.values():
        time_of_work.append(i)
    for j in Volume_CMR_dict.values():
        Cost_of_volume_CMR.append(j)
    time_of_work_dict_total = [[i*j for i in time_of_work] for j in house_properties]
    table_of_volume_CMR = [[i*j for i in Cost_of_volume_CMR] for j in house_properties]
    time_of_work_dict_total = np.sum(time_of_work_dict_total, axis=1)
    table_of_volume_CMR = np.sum(table_of_volume_CMR, axis=1)
    # варианты распределения работников
    workers_distribution = [10, 18, 20]
    # таблица рабочих и времени работы на пяти объектах.
    time_of_electric_works = np.array([[round(i / j) for i in time_of_work_dict_total]
                                       for j in workers_distribution])
    # таблица рабочих и объёмов СМР, распределенных по пяти объектам.
    table_of_volume_CMR_with_brigades = [[round(i / j) for i in table_of_volume_CMR]
                                         for j in workers_distribution]
    # определяем максимальный объём ресурсов
    C = max(workers_distribution)
    time_in_obj = int(input("Введите сколько времени могут работать электромонтажники на объектах: "))
    # Неизвестные
    variables = np.array([
        [pulp.LpVariable("v11", lowBound=0, cat='Binary'),
         pulp.LpVariable("v12", lowBound=0, cat='Binary'),
         pulp.LpVariable("v13", lowBound=0, cat='Binary'),
         pulp.LpVariable("v14", lowBound=0, cat='Binary'),
         pulp.LpVariable("v15", lowBound=0, cat='Binary')],
        [pulp.LpVariable("v21", lowBound=0, cat='Binary'),
         pulp.LpVariable("v22", lowBound=0, cat='Binary'),
         pulp.LpVariable("v23", lowBound=0, cat='Binary'),
         pulp.LpVariable("v24", lowBound=0, cat='Binary'),
         pulp.LpVariable("v25", lowBound=0, cat='Binary')],
        [pulp.LpVariable("v31", lowBound=0, cat='Binary'),
         pulp.LpVariable("v32", lowBound=0, cat='Binary'),
         pulp.LpVariable("v33", lowBound=0, cat='Binary'),
         pulp.LpVariable("v34", lowBound=0, cat='Binary'),
         pulp.LpVariable("v35", lowBound=0, cat='Binary')]
        ])
    # формулировка задачи(цели) и ее максимизация
    problem = pulp.LpProblem('Volume_CMR_maximization', LpMaximize)
    # математическая запись целевой функции
    problem += np.sum(variables * table_of_volume_CMR_with_brigades), 'Aim_Function'
    # Constraints(ограничения) по ресурсам
    problem += (np.sum(variables[0]) * workers_distribution[0] +
                np.sum(variables[1]) * workers_distribution[1] +
                np.sum(variables[2]) * workers_distribution[2]) == C
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
    # Выводим результат
    print("Результат: ")
    c = 0
    for variable in problem.variables():
        if c == 0:
            print('\t', end='| ')
        print(variable.varValue, end=' ')
        if c == 4:
            print('|\n', end=' ')
            c = 0
        else:
            c += 1
    print(f"Общий объём CМР на электромонтажные работы: {value(problem.objective)} тыс.руб.")
