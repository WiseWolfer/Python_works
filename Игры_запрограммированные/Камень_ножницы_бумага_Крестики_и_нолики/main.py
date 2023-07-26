import random as rand
# 1 игра - крестики и нолики
# amount_of_rounds = int(input("Введите количество раундов: "))
# correct_data = True
# for i in range(amount_of_rounds):
#     user = input("Введите К, Н, Б: ")
#     if user != "К" and user != "Н" and user != "Б":
#         print("Пользователь ввел некорректные данные для игры! \n"
#               "Игра закончена!")
#         correct_data = False
#         break
#
#     if correct_data:
#         num = i + 1
#         variants = ["K", "Н", "Б"]
#         action = str(rand.choice(variants))
#         if user == action:
#             print("Раунд " + str(num) + " ничья")
#         elif (user == "К" and action == "Б") or (user == "Н" and action == "Б") \
#                 or (user == "К" and action == "Н"):
#             print("Раунд " + str(num) + " Человек победил!!")
#         else:
#             print("Раунд " + str(num) + " Компьютер победил!!")
# print("\n")

################################################################################
################################################################################
# 2 игра - Крестики и нолики


# Функция вывода матрицы на экран с крестиками и ноликами
def fieldprint(matrix_field):
    for i in range(len(matrix_field)):
        print("|", matrix_field[i], end=" |")
        if i == 2 or i == 5 or i == 8:
            print("\n")


# Функция для автоматического заполнения матрицы
def addtofield_auto(user, comp_actions, matrix_field):
    step = 0
    step_swap = False
    sequence_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    cur_matrix_field = matrix_field
    while step != 9 and cur_matrix_field.count(".") != 0:
        step += 1
        cur_matrix_field = matrix_field
        place_to_add = rand.choice(sequence_choice)
        print(f"ход № {step}")
        if step_swap != True and matrix_field[place_to_add] == ".":
            cur_matrix_field.pop(place_to_add)
            cur_matrix_field.insert(place_to_add, user)
            fieldprint(cur_matrix_field)
            sequence_choice.remove(place_to_add)
            step_swap = True
            if whoWin(cur_matrix_field):
                print("X - победили!!")
                break
            elif whoWin(cur_matrix_field) == False:
                print("0 - победили!!")
                break
        elif step_swap and matrix_field[place_to_add] == ".":
            cur_matrix_field.pop(place_to_add)
            cur_matrix_field.insert(place_to_add, comp_actions)
            fieldprint(cur_matrix_field)
            sequence_choice.remove(place_to_add)
            step_swap = False
            if whoWin(cur_matrix_field):
                print("X - победили!!")
                break
            elif whoWin(cur_matrix_field) == False:
                print("0 - победили!!")
                break
    if whoWin(cur_matrix_field) == None:
        print("Победила дружба!!")


# Функция для ручного заполненния матрицы
def addtofield_manual(user, comp_actions, matrix_field):
    step = 0
    step_swap = False
    cur_matrix_field = matrix_field
    while step != 9 and cur_matrix_field.count(".") != 0:
        step += 1
        cur_matrix_field = matrix_field
        sequence_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        place_to_add_comp = rand.choice(sequence_choice)
        if step_swap != True:
            print(f"ход № {step} - пользователь")
            place_to_add = int(input('Введите куда вставить X или 0 '
                                     '\n(позиция (1 стр; 1 столб) - 1, '
                                     'позиция (1 стр; 2 столб) - 2, '
                                     'позиция (1 стр; 3 столб) - 3,\n'
                                     'позиция (2 стр; 1 столб) - 4, '
                                     'позиция (2 стр; 2 столб) - 5, '
                                     'позиция (2 стр; 3 столб) - 6,\n'
                                     'позиция (3 стр; 1 столб) - 7, '
                                     'позиция (3 стр; 2 столб) - 8, '
                                     'позиция (3 стр; 3 столб) - 9): ')) - 1
            if cur_matrix_field[place_to_add] == ".":
                cur_matrix_field.pop(place_to_add)
                cur_matrix_field.insert(place_to_add, user)
                fieldprint(cur_matrix_field)
                step_swap = True
                if whoWin(cur_matrix_field):
                    print("X - победили!!")
                    break
                elif whoWin(cur_matrix_field) == False:
                    print("0 - победили!!")
                    break
        elif step_swap:
            print(f"ход № {step} - компьютер")
            while True:
                if cur_matrix_field[place_to_add_comp] == '.':
                    cur_matrix_field.pop(place_to_add_comp)
                    cur_matrix_field.insert(place_to_add_comp, comp_actions)
                    fieldprint(cur_matrix_field)
                    sequence_choice.remove(place_to_add_comp)
                    step_swap = False
                    break
                else:
                    place_to_add_comp = rand.choice(sequence_choice)
            if whoWin(cur_matrix_field):
                print("X - победили!!")
                break
            elif whoWin(cur_matrix_field) == False:
                print("0 - победили!!")
                break
    if whoWin(cur_matrix_field) == None:
        print("Победила дружба!!")


# Функция определения победителя
def whoWin(cur_matrix_field):
    if (cur_matrix_field[0] == "X" and cur_matrix_field[1] == "X" and (cur_matrix_field[2] == "X")
            or (cur_matrix_field[0] == "X" and cur_matrix_field[4] == "X" and cur_matrix_field[8] == "X")
            or (cur_matrix_field[2] == "X" and cur_matrix_field[4] == "X" and cur_matrix_field[6] == "X")
            or (cur_matrix_field[3] == "X" and cur_matrix_field[4] == "X" and cur_matrix_field[5] == "X")
            or (cur_matrix_field[6] == "X" and cur_matrix_field[7] == "X" and cur_matrix_field[8] == "X")
            or (cur_matrix_field[0] == "X" and cur_matrix_field[3] == "X" and cur_matrix_field[6] == "X")
            or (cur_matrix_field[1] == "X" and cur_matrix_field[4] == "X" and cur_matrix_field[7] == "X")
            or (cur_matrix_field[2] == "X" and cur_matrix_field[5] == "X" and cur_matrix_field[8] == "X")):
        return True
    elif (cur_matrix_field[0] == "0" and cur_matrix_field[1] == "0" and (cur_matrix_field[2] == "0")
            or (cur_matrix_field[0] == "0" and cur_matrix_field[4] == "0" and cur_matrix_field[8] == "0")
            or (cur_matrix_field[2] == "0" and cur_matrix_field[4] == "0" and cur_matrix_field[6] == "0")
            or (cur_matrix_field[3] == "0" and cur_matrix_field[4] == "0" and cur_matrix_field[5] == "0")
            or (cur_matrix_field[6] == "0" and cur_matrix_field[7] == "0" and cur_matrix_field[8] == "0")
            or (cur_matrix_field[0] == "0" and cur_matrix_field[3] == "0" and cur_matrix_field[6] == "0")
            or (cur_matrix_field[1] == "0" and cur_matrix_field[4] == "0" and cur_matrix_field[7] == "0")
            or (cur_matrix_field[2] == "0" and cur_matrix_field[5] == "0" and cur_matrix_field[8] == "0")):
        return False
    else:
        return None


if __name__ == '__main__':
    print("Игра крестики и нолики:\n")
    user = input("Введите X, O: ")
    if user == "X":
        comp_actions = input("Введите 0 для игрока-компьютера: ")
    else:
        comp_actions = input("Введите X для игрока-компьютера: ")
    print("\nИгра началась: \n")
    matrix_field = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    fieldprint(matrix_field)
    addtofield_manual(user, comp_actions, matrix_field)
