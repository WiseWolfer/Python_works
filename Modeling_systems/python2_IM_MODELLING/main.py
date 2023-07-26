import random

classic = [35, 15, 10, 40]
extra = [20, 40, 10, 30]


def inter_classic(rate):
    inter = []
    for i in range(len(rate)):
        # интервалы для определения вида датчиков
        if not inter:
            inter.append(rate[i]/sum(rate))
        else:
            inter.append(rate[i]/sum(rate)+inter[i-1])
    return inter


def inter_extra(rate):
    inter = []
    for i in range(len(rate)):
        # интервалы для определения доп требований
        if not inter:
            inter.append(rate[i]/sum(rate))
        else:
            inter.append(round(rate[i] / sum(rate) + inter[i-1], 3))
    return inter


def pribil(inter_c, inter_e):
    cost_list = [45, 35, 60, 50] # цена продажи датчиков
    cost_classic = [25, 15, 35, 30] # затраты датчиков в обычном исполнении
    cost_extra = [8, 12, 10, 0] # дополнительные затраты при выпуске датчика
    numWithExtra = 0 # кол-во деталей с дополнительными требованиями
    total = 0 # Итоговая прибыль
    n = 100000 # Кол-во ситуаций
    for i in range(n):
        # Цены для случайных датчиков с доп требованиями
        random_extra_cost = []
        # Детали с доп требованиями для 1 модели
        numWithExtrafor1 = 0
        # получаем случайное число для определения типа датчика
        random_classic = random.random()
        print(f'№ итерации {i+1} случайное число для определения типа датчика: {random_classic}')
        # Определяем тип датчика и его цену
        for i in range(len(inter_c)):
            if 0 < random_classic <= inter_c[i]:
                cost_random_detail = cost_classic[i]
                profit_detail_price = cost_list[i]
                break
            elif inter_c[i] < random_classic <= inter_c[i+1]:
                cost_random_detail = cost_classic[i+1]
                profit_detail_price = cost_list[i+1]
                break

        for k in range(3):
            random_extra = random.random()
            print(f'|Случайное число {random_extra} для определения {k+1} доп требования|')
            for i in range(len(inter_e)):
                if 0 < random_extra <= inter_e[i]:
                    random_extra_cost.append(cost_extra[i])
                    break
                elif inter_e[i] < random_extra <= inter_e[i+1]:
                    random_extra_cost.append(cost_extra[i+1])
                    break
        # Определяем кол-во требований у модели датчика
        for j in range(len(random_extra_cost)):
            if random_extra_cost[j] > 0:
                numWithExtrafor1 += 1
        # кол-во датчиков с доп.требованиями всего
        if numWithExtrafor1 > 0:
            numWithExtra += 1
        total_price = cost_random_detail+sum(random_extra_cost)# цена производства
        profit_price = profit_detail_price + numWithExtrafor1 * 0.2 * profit_detail_price #Цена продажи
        total += profit_price - total_price # прибыль с 1 датчика
    text1 = 'Средняя прибыль с одного датчика составляет'
    text2 = 'усл. ед.'
    text3 = 'доля датчиков специальной сборки из 100 000 заказов - '
    return text1, total/n, text2, text3, numWithExtra

print(pribil(inter_classic(classic), inter_extra(extra)))
