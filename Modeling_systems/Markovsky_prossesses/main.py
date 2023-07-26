import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Вычисляет производную от y в момент времени t.


def f(y, t):
    y1, y2, y3, y4, y8 = y
    return [-y1 * (0.008 + 0.25*math.exp(-0.8 + 0.08*t) + 0.22*math.exp(-0.3 + 0.002 * t)
                   + 0.24*math.exp(-0.4 + 0.004*t) + y2 * 0.1 + y3 * 0.05 + y4 * 0.2),
            -y2 * 0.1 + 0.008 * y1 + y4 * 0.02,
            -y3 * 0.05 + y1 * 0.25*math.exp(-0.8 + 0.08*t) + y4 * 0.002,
            -y4 * (0.2 + 0.02 + 0.002) + y1 * 0.22*math.exp(-0.3 + 0.002 * t),
            y1 * ((t-50)/3000)]


if __name__ == '__main__':
    # вернет массив чисел из интервала от 1 до 50, 10 цифр
    # (последовательность моментов времени, для которых нужно найти y )
    t = np.linspace(1, 50, 11)
    # в начальном состоянии ЭВМ - исправна
    y0 = [1, 0, 0, 0, 0]
    # решение системы дифференциальных уравнений методом Рунге-Кутта
    w = odeint(f, y0, t)
    y1 = w[:, 0]
    y2 = w[:, 1]
    y3 = w[:, 2]
    y4 = w[:, 3]
    y8 = w[:, 4]
    print("Результат: ")
    print('--------------------------------------------')
    for i in range(11):
        if i != 0:
            print("| ", round(w[i][0], 3), " ", round(w[i][1], 3), " ",
                  round(w[i][2], 3), " ", round(w[i][3], 3), " ",
                  round(w[i][4], 3), " |")
    print('--------------------------------------------')

    fig = plt.figure(facecolor='white')
    plt.plot(t, y1, '-o', t, y2, '-o', t, y3, '-o', t, y4, '-o', t, y8, '-o', linewidth=1)
    plt.ylabel("p")
    plt.xlabel("t")
    plt.grid(True)
    plt.show()
