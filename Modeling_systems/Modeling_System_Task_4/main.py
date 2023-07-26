import numpy as np
from pulp import *

count = [0, 10, 20, 30, 40]

CMR = np.array([
		[0,  0,  0,  0],
		[6,  7,  8,  8],
		[12, 14, 13, 16],
		[21, 19, 26, 26],
		[30, 32, 29, 31]
	])

v = np.array([
	[pulp.LpVariable("v11", cat='Binary'),
	pulp.LpVariable("v12", cat='Binary'),
	pulp.LpVariable("v13", cat='Binary'),
	pulp.LpVariable("v14", cat='Binary')],
	[pulp.LpVariable("v21", cat='Binary'),
	pulp.LpVariable("v22", cat='Binary'),
	pulp.LpVariable("v23", cat='Binary'),
	pulp.LpVariable("v24", cat='Binary')],
	[pulp.LpVariable("v31", cat='Binary'),
	pulp.LpVariable("v32", cat='Binary'),
	pulp.LpVariable("v33", cat='Binary'),
	pulp.LpVariable("v34", cat='Binary')],
	[pulp.LpVariable("v41", cat='Binary'),
	pulp.LpVariable("v42", cat='Binary'),
	pulp.LpVariable("v43", cat='Binary'),
	pulp.LpVariable("v44", cat='Binary')],
	[pulp.LpVariable("v51", cat='Binary'),
	pulp.LpVariable("v52", cat='Binary'),
	pulp.LpVariable("v53", cat='Binary'),
	pulp.LpVariable("v54", cat='Binary')]
])

C = max(count) 	# Объем распределяемых ресурсов
problem = pulp.LpProblem('0', LpMaximize)
# ЦФ
profit = np.sum(CMR*v)
problem += profit, "Function"
# Ограничние доступности средств
problem += (np.sum(v[0]) * count[0] + np.sum(v[1]) * count[1] +
			np.sum(v[2]) * count[2] + np.sum(v[3]) * count[3] + np.sum(v[4]) * count[4]) == C
# Ограничение "Накаждый объект может быть выделен только 1 кол-во рабочих"
problem += np.sum(v[:, 0]) <= 1
problem += np.sum(v[:, 1]) <= 1
problem += np.sum(v[:, 2]) <= 1
problem += np.sum(v[:, 3]) <= 1
# Произведение рсчетов
status = problem.solve()
# Вывод результата
print("Результат:")
c = 0
for variable in problem.variables():
	if c == 0:
		print('\t', end='| ')
	print(variable.varValue, end=' ')
	if c == 3:
		print('|\n', end=' ')
		c = 0
	else:
		c += 1
print("Общий СМР:", value(problem.objective))
