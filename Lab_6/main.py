# This is a sample Python script.


from multiprocessing import Pool
import multiprocessing
from threading import Thread
import threading
# Очереди, модуль queue
from queue import Queue

#
# class Point(object):
#
#     def __init__(self, x, y):
#         self.mutex = threading.RLock()
#         self.set(x, y)
#
#     # метод возвращает один из потоков
#
#     def get(self):
#         with self.mutex:
#             return self.x, self.y
#
#     # метод записи в коструктор одного из потоков
#
#     def set(self, x, y):
#         with self.mutex:
#             self.x = x
#             self.y = y
#
#
# def f(x):
#     return x*x
#
#
# def count(n):
#     while n != 0:
#         n -= 1
#
#
# def worker(queue, n):
#     while True:
#         # удаление и возврат элемента из очереди - get()
#         item = queue.get()
#         if item is None:
#             break
#         print("process data:", n, item)
#



    # распределяем выполнение одной функции
    # между несколькими процессами для разных входных значений
    # p = Pool(5)
    # print(p.map(f, [1, 2, 3]))
    # # запускаем функцию через два потока параллельно
    # t1 = Thread(target=count, args=(100000000,))
    # t1.start()
    # t2 = Thread(target=count, args=(100000000,))
    # t2.start()
    # t1.join()
    # t2.join()
    # # запускаем последовательно, получаем более быстрое выполнение,чем параллельное выполнение
    # # через потоки
    # count(100000000)
    # count(100000000)
    #
    # # тоже самое только через процессы параллельно
    # t1 = multiprocessing.Process(target=count, args=(100000000,))
    # t1.start()
    # t2 = multiprocessing.Process(target=count, args=(100000000,))
    # t2.start()
    # t1.join()
    # t2.join()
    # # создаем очередь размером 5
    # q = Queue(5)
    # th1 = Thread(target=worker, args=(q, 1))
    # th2 = Thread(target=worker, args=(q, 2))
    # th1.start()
    # th2.start()
    # for i in range(50):
    #     # поместить элемент в очередь
    #     q.put(i)
    # q.put(None)
    # q.put(None)
    # th1.join()
    # th2.join()

    # # use in threads
    # my_point = Point(10, 20)
    # my_point.set(15, 10)
    # my_point.get()
    # print(my_point.get())



# Задание 2 матрица из элементов
import time

def elements(p, q):
    sp = [[round(((p[j]*p[matrix_item] + q[j] * q[matrix_item]) ** 0.5)) for matrix_item in range(len(p))] for j in range(len(q))]
    for item in sp:
        print(item)


if __name__ == '__main__':
    start_time = time.time()
    print(start_time)
    P = [i for i in range(1, 1000)]
    Q = [j for j in range(1, 1000)]
    elements(P, Q)
    end_time = time.time()
    print(end_time)
    res = end_time - start_time
    print("Всего времени задействует без процессоров и потоков:", res)

    print("\nСчитаем через потоки:")
    start_time = time.time()
    print(start_time)
    thread = Thread(target=elements, args=([i for i in range(1,101)], [j for j in range(1,101)],))
    thread.start()
    thread.join()
    end_time = time.time()
    print(end_time)
    res_1 = end_time - start_time
    print("Всего времени задействует с использованием потоков:", res_1)

    # print("\nСчитаем через процессы:")
    # start_time = time.time()
    # print(start_time)
    # Process_1 = multiprocessing.Process(target=elements,
    #                                     args=([i for i in range(1,1000)],
    #                                           [j for j in range(1,1000)],))
    # Process_1.start()
    # Process_1.join()
    # end_time = time.time()
    # print(end_time)
    # res_2 = end_time-start_time
    # print("Всего времени задействует с использованием процессов:", res_2)

    print("Самое быстрое исполнения программы:", min(res, res_1))
    # import os
    #
    # def search_file(dir):
    #     print("Нужные дирректории:")
    #     for root, dirs, files in os.walk(dir):
    #         for file in files:
    #             if file.endswith(".txt"):
    #                 if "Dima" in file:
    #                     print(root, file)
    #
    # directory = "C:/Users/Dmitriy/PycharmProjects/Lab_6"
    # th1 = Thread(target=search_file, args=(directory,))
    # th1.start()
    # th1.join()
    # th2 = multiprocessing.Process(target=search_file, args=(directory,))
    # th2.start()
    # th2.join()

    # Синхронизация потоков с помощью семафоров
    # сначала семафор равен 1
    try_semaphore = threading.BoundedSemaphore()
    counter = 0
    while True:
        t1 = Thread()
        print("Поток 1 начал работу")
        t1.start()
        t2 = Thread()
        print("Поток 2 начал работу")
        t2.start()
        counter += 1
        t2.join()
        print("Заблокирован проток 2")
        try_semaphore.acquire()  # -1
        t1.join()
        print("Заблокирован поток 1")
        try_semaphore.release()  # +1
        if counter == 2:
            print("Работа выполнена!")
            break
