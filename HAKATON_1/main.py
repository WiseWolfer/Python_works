import numpy as np
import matplotlib.pyplot as plt
import math
from pulp import *


massive_bool = np.array([])


def checkZero():
    count = 0
    for k in range(len(massive_bool)):
        if int(massive_bool[k].value() or 0) > 0:
            count += 1
    print(str(count) + " Привет Максим!!!")
    return count


if __name__ == '__main__':
    max_weight = 200
    max_volume = 100
    with open("map.json", 'r') as file:
        information = json.load(file)
        massive_x = []
        massive_y = []
        massive_circle = []
        for item in information['children']:
            massive_x.append(item['x'])
            massive_y.append(item['y'])
        for snow_ar in information['snowAreas']:
            massive_circle.append(plt.Circle((snow_ar['x'], snow_ar['y']), snow_ar['r']))
        for circle in massive_circle:
            plt.gca().add_patch(circle)

        plt.plot(massive_x, massive_y, 'ro', markersize=2)
        plt.plot(0, 0, 'go')

        problem = LpProblem('Ценность_рюкзака_с_подарками', LpMinimize)

        # profit
        massive_gifts = np.array([])
        for item in information['gifts']:
            itm = np.array([item['id'], item['weight'], item['volume']])
            if item['id'] == 1:
                massive_gifts = np.array([itm])
            else:
                massive_gifts = np.concatenate(
                    (massive_gifts,
                     [itm]),
                    axis=0
                )

            # massive_gifts = np.concatenate([massive_gifts,
            #                                np.append([item['id'], item['weight']], [item['volume']], axis=0)])
        # unknown = ['var' + str(i) + " " + str(j) for i in range
        # (len(massive_gifts)) for j in range(len(massive_gifts))]
        matrix_unknown_values = np.array([])
        for i in range(len(massive_gifts)):
            row = np.array([])
            for j in range(len(massive_gifts)):
                row = np.append(row, pulp.LpVariable(str(i) + " " + str(j), cat="Binary"))
            if i == 0:
                matrix_unknown_values = np.array([row])
            else:
                matrix_unknown_values = np.concatenate(
                    (matrix_unknown_values,
                     [row]),
                    axis=0
                )
            # matrix_unknown_values = np.append(matrix_unknown_values, row)
        massive_volume = np.array([])
        massive_weights = np.array([])
        for i in range(len(matrix_unknown_values[0])):
            massive_volume = np.append(massive_volume, lpSum(matrix_unknown_values[:, i] * massive_gifts[:, 2]))
        for i in range(len(matrix_unknown_values[0])):
            massive_weights = np.append(massive_weights, lpSum(matrix_unknown_values[:, i] * massive_gifts[:, 1]))
        for i in range(len(matrix_unknown_values[0])):
            # количество подарков в мешке
            massive_bool = np.append(massive_bool, 1 if
            lpSum(matrix_unknown_values[:, i]) >= 1 else 0)
        print(massive_bool)
        # Ограничения
        for i in massive_volume:
            problem += i <= max_volume
        for i in massive_weights:
            problem += i <= max_weight
        for row in matrix_unknown_values:
            problem += lpSum(row) == 1

        problem += lpSum(massive_bool), "Function"
        problem.solve()

        print("Результат:")
        c = 0
        for variable in problem.variables():
            if c == 0:
                print('\t', end='\t')

            print(variable.varValue, end='\t')

            if c == len(matrix_unknown_values):
                print('\n', end=' ')
                c = 0
            else:
                c += 1
        print("Количество пакетов с подарками:", value(problem.objective), "\n\n")
        for i in range(len(massive_weights)):
            print(str(massive_weights[i].value()), end=" ")
        # plt.show()
