# Задача 4
import numpy


def poisson(lam):
    # распределение при n = 0
    el =numpy.exp(-lam) # e^(-lam)
    n = 0
    u = numpy.random.uniform(0,1) # либо 0 либо 1
    pp = el
    fact = 1
    pow = 1
    while u >pp:
        n = n+1
        fact = n*fact
        pow = lam*pow
        pp = pp + (pow/fact)*el
    return n

# n = 100 # Кол-во итераций
# kolnorm = 0
# for i in range(n):
#     z = 0
#
for i in range(10):
    t = numpy.random.exponential(2) # Рапсределение по экспоненциальному закону
    print(t)
#     lam = 0.02 * t # Кол-во помех за время передачи
#     m = poisson(lam) # Распределение Пуассона
#     if m != 0:
#         print("Получены помехи")
#         print('______________________________________________')
#     if m == 0:
#         z+=1
#         kolnorm += 1 # Кол-во сигнала без искажений
#         print("Cигнал без искажения")
# print('По результатам моделирования, вероятность передачи сигнала без искажений составляет примерно', kolnorm/n)
