def MakeAlphabetGreatAgain(alpha):
    alpha = ['А', 'Б', 'В', 'Г', 'Д', "Е", "Ё",
             "Ж", "З", "И", "Й", "К", "Л", "М",
             "Н", "О", "П", "Р", "С", "Т", "У",
             "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ",
             "Ы", "Ь", "Э", "Ю", "Я"]
    return alpha


if __name__ == '__main__':
    try:
        key_cipher = int(input("Введите ключ шифра Цезаря:"))
        alphabet_old = []
        alphabet_old = MakeAlphabetGreatAgain(alphabet_old)
        print("Исходный Алфавит: ")
        for l_old in alphabet_old:
            print(l_old, end=" ")
        print("\nНовый Алфавит: ")
        alphabet_new = alphabet_old
        for item in range(key_cipher):
            alphabet_new.append(alphabet_old.pop(item - item))
        for l_new in alphabet_new:
            print(l_new, end=" ")
        word = input("\nВведите слово, которое нужно закодировать:")
        print(f"Исходное слово: {word}")
        coding_word = ""
        alphabet_old = MakeAlphabetGreatAgain(alphabet_old)
        for item in word:
            for j, i in enumerate(alphabet_old):
                if item == i:
                    for index, k in enumerate(alphabet_new):
                        if index == j:
                            coding_word = coding_word + str(alphabet_new[index]) + " "
        if coding_word == "":
            print("Закодированное слово пустое, так как было введено "
                  "недопустимое значение исходного слова!")
        else:
            print(f"Закодированное слово: {coding_word}")
    except ValueError as valErr:
        print("Ключ шифра Цезаря может быть только цифрой!!!")


