# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from pulp import *


if __name__ == '__main__':
        a11 = 16
        a12 = 32
        a13 = 32
        a21 = 9
        a22 = 4
        a23 = 6
        a31 = 40
        a32 = 60
        a33 = 44
        b1 = 290
        b2 = 80
        b3 = 530
        c1 = 10
        c2 = 12
        c3 = 11
        # variables
        vol1 = pulp.LpVariable('vol1', 0)
        vol2 = pulp.LpVariable('vol2', 0)
        vol3 = pulp.LpVariable('vol3', 0)
        # function
        problem = pulp.LpProblem('0', LpMaximize)
        profit = vol1 * c1 + vol2 * c2 + vol3 * c3
        problem += profit, "Function"
        # constraints
        # ограничение на кол-во балласта
        problem += vol2 <= 8
        problem += vol3 <= 5
        # ограничение ресурсов экскаватора
        exccost = 0
        exccost += vol1 * a11
        exccost += vol2 * a12
        exccost += vol3 * a13
        problem += exccost <= b1
        # ограничение ресурсов бульдозера
        buldcost = 0
        buldcost += vol1 * a21
        buldcost += vol2 * a22
        buldcost += vol3 * a23
        problem += buldcost <= b2
        # ограничение трудовых ресурсов
        buldcost = 0
        buldcost += vol1 * a31
        buldcost += vol2 * a32
        buldcost += vol3 * a33
        problem += buldcost <= b3
        # solving problem
        status = problem.solve()
        print(status)
        print("Результат:")
        for variable in problem.variables():
            print(variable.name, "=", variable.varValue)
        print("Прибыль:")
        print(value(problem.objective))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
