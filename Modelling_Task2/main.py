# This is a sample Python script.
from pulp import *


if __name__ == '__main__':
    c11 = 5
    c12 = 3
    c13 = 10
    c14 = 5
    c21 = 7
    c22 = 8
    c23 = 8
    c24 = 7
    c31 = 4
    c32 = 8
    c33 = 3
    c34 = 8
    a1 = 23
    a2 = 22
    a3 = 21
    b1 = 16
    b2 = 12
    b3 = 19
    b4 = 19
    # variables
    v11 = pulp.LpVariable("v11", 0)
    v12 = pulp.LpVariable("v12", 0)
    v13 = pulp.LpVariable("v13", 0)
    v14 = pulp.LpVariable("v14", 0)
    v21 = pulp.LpVariable("v21", 0)
    v22 = pulp.LpVariable("v22", 0)
    v23 = pulp.LpVariable("v23", 0)
    v24 = pulp.LpVariable("v24", 0)
    v31 = pulp.LpVariable("v31", 0)
    v32 = pulp.LpVariable("v32", 0)
    v33 = pulp.LpVariable("v33", 0)
    v34 = pulp.LpVariable("v34", 0)
    # function
    costs = 0
    costs += v11 * c11
    costs += v12 * c12
    costs += v13 * c13
    costs += v14 * c14
    costs += v21 * c21
    costs += v22 * c22
    costs += v23 * c23
    costs += v24 * c24
    costs += v31 * c31
    costs += v32 * c32
    costs += v33 * c33
    costs += v34 * c34
    problem = pulp.LpProblem('0', LpMinimize)
    problem += costs, "Function"
    # csontraints на мощности балластных карьеров
    problem += v11 + v12 + v13 + v14 == a1
    problem += v21 + v22 + v23 + v24 == a2
    problem += v31 + v32 + v33 + v34 == a3
    # csontraints на потребности участков строящейся
    problem += v11 + v21 + v31 == b1
    problem += v12 + v22 + v32 == b2
    problem += v13 + v23 + v33 == b3
    problem += v14 + v24 + v34 == b4
    # solving problem
    status = problem.solve()
    print(status)
    print("Результат:")
    for variable in problem.variables():
        if variable.varValue != 0:
            print(variable.name, "=",
                  variable.varValue)
    print("Издержки:")
    print(value(problem.objective))