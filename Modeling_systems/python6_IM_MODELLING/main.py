#Задача 6
from pulp import *
import numpy as np

# Объем бетонных работ
A = np.array([[30, 40, 50, 60],
              [33, 43, 53, 58],
              [23, 44, 49, 53],
              [70, 33, 43, 63]])
# неизвестные
xi = []
for i in range(16):
    xi.append(i)

x = pulp.LpVariable.dict('x', xi, lowBound=0, cat='Binary')
problem = LpProblem('0', LpMinimize) #целевая функция
problem += A[0][0] * x[0] + A[0][1] * x[1] + A[0][2] * x[2] + A[0][3] * x[3] \
         + A[1][0] * x[4] + A[1][1] * x[5] + A[1][2] * x[6] + A[1][3] * x[7] \
         + A[2][0] * x[8] + A[2][1] * x[9] + A[2][2] * x[10] + A[2][3] * x[11] \
         + A[3][0] * x[12] + A[3][1] * x[13] + A[3][2] * x[14] + A[3][3] * x[15], "Целевая" #уравнение целевой функции

problem += x[0] + x[4] + x[8] + x[12] == 1, "1" #сумма по столбцу = 1
problem += x[1] + x[5] + x[9] + x[13] == 1, "2"
problem += x[2] + x[6] + x[10] + x[14] == 1, "3"
problem += x[3] + x[7] + x[11] + x[15] == 1, "4"

problem += x[0] + x[1] + x[2] + x[3] == 1, "5" #сумма по строке = 1
problem += x[4] + x[5] + x[6] + x[7] == 1, "6"
problem += x[8] + x[9] + x[10] + x[11] == 1, "7"
problem += x[12] + x[13] + x[14] + x[15] == 1, "8"

problem.solve()
print("Оптимальное распределение:")
k = 1
for i in [0, 4, 8, 12]:
    print(k, "|", x[i].value(), "|", x[i + 1].value(), "|", x[i + 2].value(), "|", x[i + 3].value(), "|")
    k += 1
print("Минимальный срок выполнения работ:")
print(value(problem.objective))