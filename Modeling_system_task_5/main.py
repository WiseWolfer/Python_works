from pulp import *

if __name__ == '__main__':

    REQUESTS = ['1', '2', '3', '4', '5']
    rate = {'1': 78, '2': 64, '3': 68, '4': 62, '5': 85}
    volunteers = {'1': 7, '2': 4, '3': 6, '4': 5, '5': 8}
    problem = LpProblem("Resources", LpMaximize)
    iterator = [i for i in REQUESTS]
    variables = LpVariable.dicts("Заявка", (REQUESTS),
                                 0, 1, LpInteger)
    problem += lpSum(variables[i] * rate[i] for (i) in
                     iterator)
    problem += lpSum(variables[i] * volunteers[i] for i
                     in REQUESTS) <= 23
    status = problem.solve()
    print(status)
    print("Результат:")
    vol = 0
    for variable in problem.variables():
        if variable.varValue != 0:
            print(variable.name, "=", variable.varValue)
        vol += variable.varValue * volunteers[variable.name[-1:]]
    print("Общая оценка:")
    print(value(problem.objective))
    print('Всего добровольцев:', vol)