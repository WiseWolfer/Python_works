from pulp import *

if __name__ == '__main__':

    # SETS
    ORGANIZATIONS = ['A1', 'A2', 'A3', 'A4', 'A5']
    REPAIR_WORKS = ['B1', 'B2', 'B3', 'B4', 'B5']
    costs = {
        'A1': 3,
        'A2': 3,
        'A3': 3,
        'A4': 3,
        'A5': 2
    }
    # 6 5 10 6  7 8 5 5  16 13 15 29  15 25 14 11  11 43 7 36
    # Dictionary of all work
    time = {'A1': {'B1': 6, 'B2': 5, 'B3': 10, 'B4': 6, 'B5': 0},
            'A2': {'B1': 7, 'B2': 8, 'B3': 5, 'B4': 5, 'B5': 0},
            'A3': {'B1': 16, 'B2': 13, 'B3': 15, 'B4': 29, 'B5': 0},
            'A4': {'B1': 15, 'B2': 25, 'B3': 14, 'B4': 11, 'B5': 0},
            'A5': {'B1': 11, 'B2': 43, 'B3': 7, 'B4': 36, 'B5': 0}
            }
    # Set Problem Variable
    problem = LpProblem("Destination", LpMinimize)
    dests = [(i, j) for i in ORGANIZATIONS for j in REPAIR_WORKS]

    # DECISION VARIABLE
    variables = LpVariable.dicts("Amount", (ORGANIZATIONS,
                                            REPAIR_WORKS), 0, 1)

    # OBJECTIVE FUNCTION
    problem += lpSum(variables[i][j] * time[i][j] * costs[i] for
                     (i, j) in dests)
    print(problem)
    # CONSTRAINTS:
    for j in REPAIR_WORKS:
        problem += lpSum(variables[i][j] for i in ORGANIZATIONS) == 1
    for i in ORGANIZATIONS:
        problem += lpSum(variables[i][j] for j in
                         REPAIR_WORKS) == 1
    # Organization A3 don't do work B1
    problem += variables['A3']['B1'] == 0, "1"
    status = problem.solve()
    print(status)
    print("Результат:")
    for variable in problem.variables():
        if variable.varValue != 0:
            print(variable.name, "=", variable.varValue)
    print("Сумма издержек:")
    print(value(problem.objective))