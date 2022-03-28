# This is a sample Python script.

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
   # strochka = "123"
   # sp = [1,2,3,4,5,'123']
    #sp.append(1)
    #sp.pop(5)
    #for i in sp:
    #   print(i)
    #sp.sort()
    #print(sp)
    #print('-------------------------')
    #L = [45, '123', '323', 3]
    #sp.extend(L)
    #print(sp)
    #res_count = sp.count(1)
    #print(res_count)
    #print('-------------------------')
    #stroka = 'Dima'
    # a = tuple()
    # b = ('s',)
    # print(b)
    # baka = "s",
    # print(baka)
    # slovo = tuple("hello world!")
    # check = 'world'
    # n = 100
    # text = "1 + 2 + ' ' +"+ str(n) + " ="
    # s = 0
    # i = 1
    # while True:
    #     s += i
    #     i += 1
    #     if i > n:
    #         break
    # print(text, s)
    # while i <= n:
    #     s += i
    #     i += 1
    # print(text,s)
    # s = [1,2,3,4,5]
    # a = s.remove(5)
    # s.pop(3)
    # print(len(s))
    # A = [["А.С. Пушкин", "Капитанская дочка"],
    #     ["Л.Н. Толстой", "Война и мир"],
    #     ["А.П. Чехов", "Вишневый сад"]]
    # writers = dict(A)
    # writers["А.П. Чехов"] = "Каштанка"
    # print(writers)
    # writers["Ф.М. Достоевский"] = "Преступление и наказание"
    # print(writers)
    # for i in writers.keys():
    #     print(i + ' - Автор' + " ")
    #     print(writers[i] + " - Название произведения" + "\n")
    #
    # lights = dict(красный="движение запрещено",
    #             желтый="приготовится",
    #             зеленый="движение разрешено")
    # color = "желтый"
    # print("Если горит " + color + ", то всем " + lights[color])
    #
    # girls ={(90, 60, 90): "Света", (85, 65, 89): "Юля", (92, 58, 91):"Нина"}
    # name = "Света"
    # size = (92, 58, 91)
    # for i in girls.keys():
    #     if girls[i] == name:
    #         print(i)
    # for i in girls.keys():
    #     if i == size:
    #         print(girls[i])
    # more_voc = {(89,65,75): "Женя", (79,55,35): "Маша", (50,45,85): "Глаша"}
    # girls.update(more_voc)
    # print(girls)
    # girls.pop((50,45,85))
    # print(girls)
    # girls.clear()
    # print(girls)
    # A = ["Пушкин", "Толстой", "Достоевский"]
    # B = ["Капитанская дочка", "Война и мир", "Преступление и наказание"]
    # gen_voc = {A[i]:B[i] for i in range(len(A))}
    # print(gen_voc)


    # def summa(n):
    #     s = 0
    #     for elem in n:
    #         s += elem
    #     return s
    # numbers = []
    # i = 5
    # while True:
    #     numbers.append(int(input("Введите число: ")))
    #     i -= 1
    #     if i == 0:
    #         break
    # result = summa(numbers)
    # print("Итоговоая сумма равна", result)
    f = lambda x,y: x^2+2*y+25
    print(f(5, 4))
