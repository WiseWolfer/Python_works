import numpy
import math

smena_excavator = 0  # время работы экскаватора 6 разрядом, сек в 2 смены
smena_buld = 0  # время работы бульдозер 6 разрядом, сек в 2 смены
smena_excavator_repair = 0  # время починки экскаватора 6 разрядом, сек в 2 смены
smena_buld_repair = 0       # время починки бульдозера 6 разрядом, сек в 2 смены
ex_work_per_day = 0         # время работы экскаватора в день
buld_work_per_day = 0       # время работы бульдозера в день
ex_repair_per_day = 0       # время починки экскаватора в день
buld_repair_per_day = 0     # время починки бульдозера в день

excavator_income = 500  # доход по экскаватору
buld_income = 300  # доход по бульдозеру

excavator_idle_cost = 500  # расходы по экскаватору
buld_idle_cost = 300  # расходы по бульдозеру

expences_plumber_3 = 60  # слесарь 3 разряда получает
expences_plumber_6 = 100  # слесарь 6 разряда получает
repair_expences = 50  # накладные расходы на ремонт

time_of_plumber_6_excavator = 1  # время починки экскаватора 6 разрядом
time_of_plumber_6_buld = 2  # время починки бульдозера 6 разрядом

voc_result_6 = {}
days = int(input("Введите кол-во дней(1000): "))

# число дней прокручиваем для 6 разряда
for i in range(days):

    rand_value_excavator = math.ceil(numpy.random.exponential(4) * 3600)  # длительность работы экскаватора
    rand_value_buld = math.ceil(numpy.random.exponential(6) * 3600)  # длительность работы бульдозера

    if rand_value_buld > 16 * 3600:
        rand_value_buld = 16 * 3600

    if rand_value_excavator > 16 * 3600:
        rand_value_excavator = 16 * 3600

    smena_excavator += rand_value_excavator  # время до поломки экскаватора
    smena_buld += rand_value_buld  # время до поломки бульдозера
    ex_work_per_day += rand_value_excavator
    buld_work_per_day += rand_value_buld

    rand_value_repair = 0  # время починки в сек
    status_excavator = 1  # состояния экскаватора: -1 - чинится 0 - простаивается 1 - работает
    status_buld = 1  # состояния бульдозера: -1 - чинится 0 - простаивается 1 - работает
    point_excavator = rand_value_excavator  # точка изменения состояния экскаватора
    point_buld = rand_value_buld  # точка изменения состояния бульдозера
    # Проход двух смен в секундах
    for t in range(16 * 3600):

        if t == point_excavator:  # точка изменения состояния экскаватор
            if status_excavator == 1:  # если экскаватор работает
                if status_buld != -1:  # проверка чинит ли слесарь бульдозер
                    status_excavator = -1
                    rand_value_repair = math.ceil(numpy.random.exponential(time_of_plumber_6_excavator) * 3600)
                    if rand_value_repair > (16 * 3600 - t):
                        rand_value_repair = 16 * 3600 - t
                    point_excavator += rand_value_repair
                    smena_excavator_repair += rand_value_repair
                    ex_repair_per_day += rand_value_repair

                elif status_buld == -1:  # Если бульдозер чинится, значит экскаватор простаивается
                    status_excavator = 0
                    point_excavator = point_buld  # время окончания починки бульдозера
                    # будет временем следующей починки экскаватора
            elif status_excavator == 0:  # если экскаватор простаивает
                status_excavator = -1  # смена состояния экскаватора с простоя на состояние починки
                rand_value_repair = math.ceil(numpy.random.exponential(time_of_plumber_6_excavator) * 3600)
                if rand_value_repair > (16 * 3600 - t):
                    rand_value_repair = 16 * 3600 - t
                point_excavator += rand_value_repair
                smena_excavator_repair += rand_value_repair  # фиксация суммарного времени починки экскаватора
                ex_repair_per_day += rand_value_repair
            else:  # status_grader == -1 - пора отправить на работу!!
                status_excavator = 1  # после починки экскаватор отправляется на работу (смена состояния)
                rand_value_excavator = math.ceil(numpy.random.exponential(4) * 3600)
                if rand_value_excavator > (16 * 3600 - t):
                    rand_value_excavator = 16 * 3600 - t
                point_excavator += rand_value_excavator  # точка изменения состояния экскаватора
                smena_excavator += rand_value_excavator  # время работы экскаватора
                ex_work_per_day += rand_value_excavator

        if t == point_buld:  # точка изменения состояния бульдозера
            if status_buld == 1:  # если бульдозер работает
                if status_excavator != -1:  # проверка чинит ли слесарь экскаватор
                    status_buld = -1
                    rand_value_repair = math.ceil(numpy.random.exponential(time_of_plumber_6_buld) * 3600)
                    if rand_value_repair > (16 * 3600 - t):
                        rand_value_repair = 16 * 3600 - t
                    point_buld += rand_value_repair
                    smena_buld_repair += rand_value_repair
                    buld_repair_per_day += rand_value_repair

                elif status_excavator == -1:  # Если экскаватор чинится, значит бульдозер простаивается
                    status_buld = 0
                    point_buld += point_excavator  # время окончания починки экскаватора
                    # будет временем следующей починки бульдозера
            elif status_buld == 0:  # если бульдозер простаивает
                status_buld = -1  # смена состояия бульдозера с простоя на состояние починки
                rand_value_repair = math.ceil(numpy.random.exponential(time_of_plumber_6_buld) * 3600)
                if rand_value_repair > (16 * 3600 - t):
                    rand_value_repair = 16 * 3600 - t
                point_buld += rand_value_repair
                smena_buld_repair += rand_value_repair  # фиксация суммарного времени починки бульдозера
                buld_repair_per_day += rand_value_repair
            else:  # status_buld == -1 - пора отправить на работу!!
                status_buld = 1  # после починки бульдозера отправляется на работу (смена состояния)
                rand_value_buld = int(numpy.random.exponential(6) * 3600)
                if rand_value_buld > (16 * 3600 - t):
                    rand_value_buld = 16 * 3600 - t
                point_buld += rand_value_buld  # точка изменения состояния бульдозера
                smena_buld += rand_value_buld  # время работы бульдозера
                buld_work_per_day += rand_value_buld

    smena_sp = [ex_work_per_day / 3600, buld_work_per_day / 3600,
                ex_repair_per_day / 3600, buld_repair_per_day / 3600,
                16 - ex_work_per_day / 3600 - ex_repair_per_day / 3600,
                16 - buld_work_per_day / 3600 - buld_repair_per_day / 3600,
                ex_work_per_day / 3600 * excavator_income,
                buld_work_per_day / 3600 * buld_income]
    voc_result_6[i+1] = smena_sp
    ex_work_per_day = 0
    buld_work_per_day = 0
    ex_repair_per_day = 0
    buld_repair_per_day = 0

excavator_income_total = (smena_excavator / 3600) * excavator_income
buld_income_total = (smena_buld / 3600) * buld_income
expences_plumber_6_total = expences_plumber_6 * (smena_excavator_repair / 3600 + smena_buld_repair / 3600)

if (16 * days - smena_excavator / 3600 - smena_excavator_repair / 3600) <= 0:
    total_idle_cost_excavator = 0
else:
    total_idle_cost_excavator = (16 * days - smena_excavator /
                                 3600 - smena_excavator_repair / 3600) * excavator_idle_cost
if (16 * days - smena_buld / 3600 - smena_buld_repair / 3600) <= 0:
    total_idle_cost_buld = 0
else:
    total_idle_cost_buld = (16 * days - smena_buld / 3600 - smena_buld_repair / 3600) * buld_idle_cost
total_idle_cost = total_idle_cost_excavator + total_idle_cost_buld
brigade_overhead_costs = (smena_excavator_repair / 3600 + smena_buld_repair / 3600) * repair_expences
total_costs = expences_plumber_6_total + total_idle_cost + brigade_overhead_costs
net_profit = excavator_income_total + buld_income_total - total_costs
print("\nИтог по работе слесаря 6 разряда: " +
      "\nВремя работы экскаватора: " + str(round(smena_excavator / 3600, 1)),
      "\nВремя работа бульдозера: " + str(round(smena_buld / 3600, 1)),
      "\nВремя починки экскаватора: " + str(round(smena_excavator_repair / 3600, 1)),
      "\nВремя починки бульдозера: " + str(round(smena_buld_repair / 3600, 1)),
      "\nВремя простоя экскаватора: " + str(round(16 * days - smena_excavator / 3600
                                            - smena_excavator_repair / 3600, 1)),
      "\nВремя простоя бульдозера: " + str(round(16 * days - smena_buld / 3600
                                           - smena_buld_repair / 3600, 1)))
print("\nДоход от экскаватора: " + str(round(excavator_income_total, 1)) +
      "\nДоход от бульдозера: " + str(round(buld_income_total, 1)) +
      "\nРасход на слесаря 6 разряда : " + str(round(expences_plumber_6_total, 1)) +
      "\nНакладные расходы за простой экскаватора: " + str(round(total_idle_cost_excavator, 1)) +
      "\nНакладные расходы за простой бульдозера: " + str(round(total_idle_cost_buld, 1)) +
      "\nОбщие накладные расходы за простой: " + str(round(total_idle_cost, 1)) +
      "\nНакладные расходы на бригаду за ремонт: " + str(round(brigade_overhead_costs, 1)) +
      "\nЧистая прибыль от использования слесаря 6 разряда: " + str(round(net_profit, 1)) + "\n")

# =======================================================================================================

smena_excavator_3_6 = 0  # время работы экскаватора 6 разрядом, сек в 2 смены
smena_buld_3_6 = 0  # время работы бульдозер 6 разрядом, сек в 2 смены
smena_excavator_repair_3_6 = 0  # время починки экскаватора 6 разрядом, сек в 2 смены
smena_buld_repair_3_6 = 0  # время починки бульдозера 6 разрядом, сек в 2 смены
time_of_plumber_3_6_excavator = 0.25  # время починки экскаватора 3 и 6 разрядом
time_of_plumber_3_6_buld = 1.5  # время починки бульдозера 3 и 6 разрядом
voc_result_3_6 = {}

# число дней прокручиваем для 3 и 6 разряда
for i in range(days):

    rand_value_excavator = math.ceil(numpy.random.exponential(4) * 3600)  # момент времени поломки экскаватора
    rand_value_buld = math.ceil(numpy.random.exponential(6) * 3600)  # момент времени поломки бульозера

    if rand_value_buld > 16 * 3600:
        rand_value_buld = 16 * 3600
    if rand_value_excavator > 16 * 3600:
        rand_value_excavator = 16 * 3600

    smena_excavator_3_6 += rand_value_excavator  # время до поломки экскаватора
    smena_buld_3_6 += rand_value_buld  # время до поломки бульдозера
    ex_work_per_day += rand_value_excavator
    buld_work_per_day += rand_value_buld

    rand_value_repair = 0  # время починки в сек
    status_excavator = 1  # состояния экскаватора: -1 - чинится 0 - простаивается 1 - работает
    status_buld = 1  # состояния бульдозера: -1 - чинится 0 - простаивается 1 - работает
    point_excavator = rand_value_excavator  # точка изменения состояния экскаватора
    point_buld = rand_value_buld  # точка изменения состояния бульдозера
    # Проход двух смен в секундах
    for t in range(16 * 3600):

        if t == point_excavator:  # точка изменения состояния экскаватор
            if status_excavator == 1:  # если экскаватор работает
                if status_buld != -1:  # проверка чинит ли слесарь бульдозер
                    status_excavator = -1
                    rand_value_repair = math.ceil(numpy.random.exponential(time_of_plumber_3_6_excavator) * 3600)
                    if rand_value_repair > (16 * 3600 - t):
                        rand_value_repair = 16 * 3600 - t
                    point_excavator += rand_value_repair
                    smena_excavator_repair_3_6 += rand_value_repair
                    ex_repair_per_day += rand_value_repair
                elif status_buld == -1:  # Если бульдозер чинится, значит экскаватор простаивается
                    status_excavator = 0
                    point_excavator = point_buld  # время окончания починки бульдозера
                    # будет временем следующей починки экскаватора
            elif status_excavator == 0:  # если экскаватор простаивает
                status_excavator = -1  # смена состояния экскаватора с простоя на состояние починки
                rand_value_repair = math.ceil(numpy.random.exponential(time_of_plumber_3_6_excavator) * 3600)
                if rand_value_repair > (16 * 3600 - t):
                    rand_value_repair = 16 * 3600 - t
                point_excavator += rand_value_repair
                smena_excavator_repair_3_6 += rand_value_repair  # фиксация суммарного времени починки экскаватора
                ex_repair_per_day += rand_value_repair
            else:  # status_grader == -1 - пора отправить на работу!!
                status_excavator = 1  # после починки экскаватор отправляется на работу (смена состояния)
                rand_value_excavator = math.ceil(numpy.random.exponential(4) * 3600)
                if rand_value_excavator > (16 * 3600 - t):
                    rand_value_excavator = 16 * 3600 - t
                point_excavator += rand_value_excavator  # точка изменения состояния экскаватора
                smena_excavator_3_6 += rand_value_excavator  # время работы экскаватора
                ex_work_per_day += rand_value_excavator
        if t == point_buld:  # точка изменения состояния бульдозера
            if status_buld == 1:  # если бульдозер работает
                if status_excavator != -1:  # проверка чинит ли слесарь экскаватор
                    status_buld = -1
                    rand_value_repair = math.ceil(numpy.random.exponential(time_of_plumber_3_6_buld) * 3600)
                    if rand_value_repair > (16 * 3600 - t):
                        rand_value_repair = 16 * 3600 - t
                    point_buld += rand_value_repair
                    smena_buld_repair_3_6 += rand_value_repair
                    buld_repair_per_day += rand_value_repair

                elif status_excavator == -1:  # Если экскаватор чинится, значит бульдозер простаивается
                    status_buld = 0
                    point_buld = point_excavator  # время окончания починки экскаватора
                    # будет временем следующей починки бульдозера
            elif status_buld == 0:  # если бульдозер простаивает
                status_buld = -1  # смена состояия бульдозера с простоя на состояние починки
                rand_value_repair = math.ceil(numpy.random.exponential(time_of_plumber_3_6_buld) * 3600)
                if rand_value_repair > (16 * 3600 - t):
                    rand_value_repair = 16 * 3600 - t
                point_buld += rand_value_repair
                smena_buld_repair_3_6 += rand_value_repair  # фиксация суммарного времени починки бульдозера
                buld_repair_per_day += rand_value_repair

            else:  # status_buld == -1 - пора отправить на работу!!
                status_buld = 1  # после починки бульдозера отправляется на работу (смена состояния)
                rand_value_buld = int(numpy.random.exponential(6) * 3600)
                if rand_value_buld > (16 * 3600 - t):
                    rand_value_buld = 16 * 3600 - t
                point_buld += rand_value_buld  # точка изменения состояния бульдозера
                smena_buld_3_6 += rand_value_buld  # время работы бульдозера
                buld_work_per_day += rand_value_buld
    smena_sp = [ex_work_per_day / 3600, buld_work_per_day / 3600,
                ex_repair_per_day / 3600, buld_repair_per_day / 3600,
                16 - ex_work_per_day / 3600 - ex_repair_per_day / 3600,
                16 - buld_work_per_day / 3600 - buld_repair_per_day / 3600,
                ex_work_per_day / 3600 * excavator_income,
                buld_work_per_day / 3600 * buld_income]
    voc_result_3_6[i + 1] = smena_sp
    ex_work_per_day = 0
    buld_work_per_day = 0
    ex_repair_per_day = 0
    buld_repair_per_day = 0

excavator_income_total = (smena_excavator_3_6 / 3600) * excavator_income
buld_income_total = (smena_buld_3_6 / 3600) * buld_income
expences_plumber_6_total = expences_plumber_6 * (smena_excavator_repair_3_6 / 3600 +
                                                 smena_buld_repair_3_6 / 3600)
expences_plumber_3_total = expences_plumber_3 * (smena_excavator_repair_3_6 / 3600 +
                                                 smena_buld_repair_3_6 / 3600)
expences_plumber_3_6_total = expences_plumber_6_total + expences_plumber_3_total
if (16 * days - smena_excavator_3_6 / 3600 - smena_excavator_repair_3_6 / 3600) <= 0:
    total_idle_cost_excavator = 0
else:
    total_idle_cost_excavator = (16 * days - smena_excavator_3_6 /
                                 3600 - smena_excavator_repair_3_6 / 3600) * excavator_idle_cost
if (16 * days - smena_buld_3_6 / 3600 - smena_buld_repair_3_6 / 3600) <= 0:
    total_idle_cost_buld = 0
else:
    total_idle_cost_buld = (16 * days - smena_buld_3_6 / 3600 - smena_buld_repair_3_6 / 3600) * buld_idle_cost
total_idle_cost = total_idle_cost_excavator + total_idle_cost_buld
brigade_overhead_costs = (smena_excavator_repair_3_6 / 3600 + smena_buld_repair_3_6 / 3600) * repair_expences
total_costs = expences_plumber_3_6_total + total_idle_cost + brigade_overhead_costs
net_profit = excavator_income_total + buld_income_total - total_costs
print("Итог по работе слесаря 3 и 6 разряда: " +
      "\nВремя работы экскаватора: " + str(round(smena_excavator_3_6 / 3600, 1)),
      "\nВремя работа бульдозера: " + str(round(smena_buld_3_6 / 3600, 1)),
      "\nВремя починки экскаватора: " + str(round(smena_excavator_repair_3_6 / 3600, 1)),
      "\nВремя починки бульдозера: " + str(round(smena_buld_repair_3_6 / 3600, 1)),
      "\nВремя простоя экскаватора: " + str(round(16 * days - smena_excavator_3_6 / 3600
                                            - smena_excavator_repair_3_6 / 3600, 1)),
      "\nВремя простоя бульдозера: " + str(round(16 * days - smena_buld_3_6 / 3600
                                           - smena_buld_repair_3_6 / 3600, 1)))
print("\nДоход от экскаватора: " + str(round(excavator_income_total, 1)) +
      "\nДоход от бульдозера: " + str(round(buld_income_total, 1)) +
      "\nРасход на слесаря 3 и 6 разряда : " + str(round(expences_plumber_3_6_total, 1)) +
      "\nНакладные расходы за простой экскаватора: " + str(round(total_idle_cost_excavator, 1)) +
      "\nНакладные расходы за простой бульдозера: " + str(round(total_idle_cost_buld, 1)) +
      "\nОбщие накладные расходы за простой: " + str(round(total_idle_cost, 1)) +
      "\nНакладные расходы на бригаду за ремонт: " + str(round(brigade_overhead_costs, 1)) +
      "\nЧистая прибыль от использования слесаря 3 и 6 разряда: " + str(round(net_profit, 1)))

print("======================================================================================")
while True:
    num = int(input("Введите номер дня, данные которых хотите посмотреть"
                    " или введите 0, чтобы закончить программу: "))
    if num == 0:
        break
    elif num < 0 or num > days:
        print("Такого дня в рассматриваемом диапазоне нет, введите корректные данные!!!")
        continue
    if voc_result_6[num][4] < 0:
        voc_result_6[num][4] = 0
    if voc_result_6[num][5] < 0:
        voc_result_6[num][5] = 0
    print(f"\nВывод данных за {num} день, когда в бригаде работает слесарь 6 разряда: ")
    print("Время работы экскаватора за день " + str(round(voc_result_6[num][0], 1)),
          "\nВремя работа бульдозера за день: " + str(round(voc_result_6[num][1], 1)),
          "\nВремя починки экскаватора за день: " + str(round(voc_result_6[num][2], 1)),
          "\nВремя починки бульдозера за день: " + str(round(voc_result_6[num][3], 1)),
          "\nВремя простоя экскаватора за день: " + str(round(voc_result_6[num][4], 1)),
          "\nВремя простоя бульдозера за день: " + str(round(voc_result_6[num][5], 1)),
          "\nДоход от работы экскаватора за день: " + str(round(voc_result_6[num][6], 1)),
          "\nДоход от работы бульдозера за день: " + str(round(voc_result_6[num][7], 1)))
    if voc_result_3_6[num][4] < 0:
        voc_result_3_6[num][4] = 0
    if voc_result_3_6[num][5] < 0:
        voc_result_3_6[num][5] = 0
    print(f"\nВывод данных за {num} день, когда в бригаде работают слесари 3 и 6 разряда: ")
    print("Время работы экскаватора за день " + str(round(voc_result_3_6[num][0], 1)),
          "\nВремя работа бульдозера за день: " + str(round(voc_result_3_6[num][1], 1)),
          "\nВремя починки экскаватора за день: " + str(round(voc_result_3_6[num][2], 1)),
          "\nВремя починки бульдозера за день: " + str(round(voc_result_3_6[num][3], 1)),
          "\nВремя простоя экскаватора за день: " + str(round(voc_result_3_6[num][4], 1)),
          "\nВремя простоя бульдозера за день: " + str(round(voc_result_3_6[num][5], 1)),
          "\nДоход от работы экскаватора за день: " + str(round(voc_result_3_6[num][6], 1)),
          "\nДоход от работы бульдозера за день: " + str(round(voc_result_3_6[num][7], 1)))
