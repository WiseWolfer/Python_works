from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QLineEdit, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        # наследуую функционал QMainWindow
        super().__init__()
        self.alphabet_old, self.alphabet_new = [], []
        self.key_cipher = 0
        self.setWindowTitle("Главное окно")

        # создаем экземпляры интерфейса
        self.label_key = QLabel("Введите ключ шифра Цезаря:")
        font1 = self.label_key.font()
        font1.setPointSize(10)
        self.label_key.setFont(font1)

        self.input_key = QLineEdit()
        font1 = self.input_key.font()
        font1.setPointSize(12)
        self.input_key.setFont(font1)

        self.label_fAlpha = QLabel("ИсходныЙ Алфавит:")
        font1 = self.label_fAlpha.font()
        font1.setPointSize(10)
        self.label_fAlpha.setFont(font1)

        self.input_fAlpha = QLineEdit()
        font1 = self.input_fAlpha.font()
        font1.setPointSize(12)
        self.input_fAlpha.setFont(font1)

        self.label_newAlpha = QLabel("Новый Алфавит:")
        font1 = self.label_newAlpha.font()
        font1.setPointSize(10)
        self.label_newAlpha.setFont(font1)

        self.input_newAlpha = QLineEdit()
        font1 = self.input_newAlpha.font()
        font1.setPointSize(12)
        self.input_newAlpha.setFont(font1)

        self.label_word_to_be_code = QLabel("Введите слово, которое нужно закодировать:")
        font1 = self.label_word_to_be_code.font()
        font1.setPointSize(10)
        self.label_word_to_be_code.setFont(font1)

        self.input_word_to_be_code = QLineEdit()
        font1 = self.input_word_to_be_code.font()
        font1.setPointSize(12)
        self.input_word_to_be_code.setFont(font1)

        self.label_fWord = QLabel("Раскодированное слово:")
        font1 = self.label_fWord.font()
        font1.setPointSize(10)
        self.label_fWord.setFont(font1)

        self.input_fWord = QLineEdit()
        font1 = self.input_fWord.font()
        font1.setPointSize(12)
        self.input_fWord.setFont(font1)

        self.label_newWord = QLabel("Закодированное слово:")
        font1 = self.label_newWord.font()
        font1.setPointSize(10)
        self.label_newWord.setFont(font1)

        self.input_newWord = QLineEdit()
        font1 = self.input_newWord.font()
        font1.setPointSize(12)
        self.input_newWord.setFont(font1)

        button_get_alpha = QPushButton("Пострить исходный и новый алфавиты!")
        font1 = button_get_alpha.font()
        font1.setPointSize(10)
        button_get_alpha.setFont(font1)
        button_get_alpha.clicked.connect(self.button_get_alpha_was_clicked)
        button_decode_input_word = QPushButton("Закодировать слово по шифру Цезаря!")
        font1 = button_decode_input_word.font()
        font1.setPointSize(10)
        button_decode_input_word.setFont(font1)
        button_decode_input_word.clicked.connect(self.button_decode_input_word_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label_key)
        layout.addWidget(self.input_key)
        layout.addWidget(button_get_alpha)
        layout.addWidget(self.label_fAlpha)
        layout.addWidget(self.input_fAlpha)
        layout.addWidget(self.label_newAlpha)
        layout.addWidget(self.input_newAlpha)
        layout.addWidget(self.label_word_to_be_code)
        layout.addWidget(self.input_word_to_be_code)
        layout.addWidget(button_decode_input_word)
        layout.addWidget(self.label_newWord)
        layout.addWidget(self.input_newWord)
        layout.addWidget(self.label_fWord)
        layout.addWidget(self.input_fWord)

        container = QWidget()
        container.setLayout(layout)
        # Установка кнопки на форму
        self.setCentralWidget(container)

    def button_decode_input_word_clicked(self):
        word = self.input_word_to_be_code.text().upper()
        coding_word = ""
        self.alphabet_old = makeAlphabetGreatAgain()
        for item in word:
            for j, i in enumerate(self.alphabet_old):
                if item == i:
                    for index, k in enumerate(self.alphabet_new):
                        if index == j:
                            coding_word = coding_word + str(self.alphabet_new[index]) + " "
        if coding_word == "":
            coding_word = "Закодированное слово пустое, так как было введено " \
                          "недопустимое значение исходного слова!"
            self.input_newWord.setText(coding_word)
        else:
            self.input_newWord.setText(coding_word)
            decoding_word = ""
            for ch in coding_word:
                for finishAlpha in self.alphabet_new:
                    if ch == finishAlpha:
                        decoding_word += makeAlphabetGreatAgain()[makeAlphabetGreatAgain().index(finishAlpha) -
                                                                  self.key_cipher]
            self.input_fWord.setText(decoding_word)

    def start_clear(self):
        self.input_fAlpha.setText("")
        self.input_newAlpha.setText("")
        self.input_word_to_be_code.setText("")
        self.input_fWord.setText("")
        self.input_newWord.setText("")

    def button_get_alpha_was_clicked(self):
        try:
            self.key_cipher = int(self.input_key.text())
            self.alphabet_old = makeAlphabetGreatAgain()
            text = []
            for l_old in self.alphabet_old:
                text.append(l_old + " ")
            self.input_fAlpha.setText(str(text))
            text.clear()
            self.alphabet_new = self.alphabet_old
            for item in range(self.key_cipher):
                self.alphabet_new.append(self.alphabet_old.pop(item - item))
            for l_new in self.alphabet_new:
                text.append(l_new + " ")
            self.input_newAlpha.setText(str(text))
        except ValueError:
            self.start_clear()
            self.input_newAlpha.setText("Ключ шифра Цезаря может быть только цифрой!!!")


def makeAlphabetGreatAgain():
    return ["А", "Б", "В", "Г", "Д", "Е", "Ё",
            "Ж", "З", "И", "Й", "К", "Л", "М",
            "Н", "О", "П", "Р", "С", "Т", "У",
            "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ",
            "Ы", "Ь", "Э", "Ю", "Я"]


def main():
    app = QApplication([])
    win = MainWindow()
    win.setFixedSize(QSize(1400, 600))
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
