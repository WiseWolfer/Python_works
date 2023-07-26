from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel,\
    QWidget, QLineEdit, QVBoxLayout, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        # наследуую функционал QMainWindow
        super().__init__()
        self.ASCIIAlphabet2, self.Alphabet10_2 = {}, {}
        self.letters_to_bin, self.keyword_to_bin, self.encrypted_word, self.decode_alpha = [], [], [], []
        self.reg_frase = QRegExp("^[а-яА-Я]{1,10}$")
        self.validator = QRegExpValidator(self.reg_frase)
        self.setWindowTitle("Главное окно")

        # создаем экземпляры интерфейса
        self.label_bin_alphabet = QLabel("Двоичный алфавит: ")
        font1 = self.label_bin_alphabet.font()
        font1.setPointSize(10)
        self.label_bin_alphabet.setFont(font1)

        self.input_bin_alphabet = QTextEdit()
        font1 = self.input_bin_alphabet.font()
        font1.setPointSize(12)
        self.input_bin_alphabet.setFont(font1)

        self.label_word_to_be_code = QLabel("Введите слово, которое нужно закодировать:")
        font1 = self.label_word_to_be_code.font()
        font1.setPointSize(10)
        self.label_word_to_be_code.setFont(font1)

        self.input_word_to_be_code = QLineEdit()
        font1 = self.input_word_to_be_code.font()
        font1.setPointSize(12)
        self.input_word_to_be_code.setFont(font1)
        self.input_word_to_be_code.setValidator(self.validator)

        self.label_key = QLabel("Введите ключ (гамму): ")
        font1 = self.label_key.font()
        font1.setPointSize(10)
        self.label_key.setFont(font1)

        self.input_key = QLineEdit()
        font1 = self.input_key.font()
        font1.setPointSize(12)
        self.input_key.setFont(font1)
        self.input_key.setValidator(self.validator)

        self.label_coded_word = QLabel("Закодированное слово:")
        font1 = self.label_coded_word.font()
        font1.setPointSize(10)
        self.label_coded_word.setFont(font1)

        self.input_coded_word = QLineEdit()
        font1 = self.input_coded_word.font()
        font1.setPointSize(12)
        self.input_coded_word.setFont(font1)

        self.label_decoded_word = QLabel("Раскодированное слово:")
        font1 = self.label_decoded_word.font()
        font1.setPointSize(10)
        self.label_decoded_word.setFont(font1)

        self.input_decoded_word = QLineEdit()
        font1 = self.input_decoded_word.font()
        font1.setPointSize(12)
        self.input_decoded_word.setFont(font1)

        button_code_input_word = QPushButton("Закодировать слово методом"
                                             " гаммирования по модулю 2!")
        font1 = button_code_input_word.font()
        font1.setPointSize(10)
        button_code_input_word.setFont(font1)
        button_code_input_word.clicked.connect(self.button_code_input_word_clicked)

        button_decode_input_word = QPushButton("Раскодировать слово методом"
                                               " гаммирования по модулю 2!")
        font1 = button_decode_input_word.font()
        font1.setPointSize(10)
        button_decode_input_word.setFont(font1)
        button_decode_input_word.clicked.connect(self.button_decode_input_word_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label_bin_alphabet)
        layout.addWidget(self.input_bin_alphabet)
        layout.addWidget(self.label_word_to_be_code)
        layout.addWidget(self.input_word_to_be_code)
        layout.addWidget(self.label_key)
        layout.addWidget(self.input_key)
        layout.addWidget(button_code_input_word)
        layout.addWidget(self.label_coded_word)
        layout.addWidget(self.input_coded_word)
        layout.addWidget(button_decode_input_word)
        layout.addWidget(self.label_decoded_word)
        layout.addWidget(self.input_decoded_word)
        container = QWidget()
        container.setLayout(layout)
        # Установка кнопки на форму
        self.setCentralWidget(container)
        # Создание и вывод двоичного алфавита в консоль
        self.showASCIIAlphabet2()

    def createASCIIAlphabet2(self):
        for i in self.ASCIIAlphabet10():
            self.ASCIIAlphabet2[i] = (bin(self.ASCIIAlphabet10()[i])).lstrip("0b")

    def showASCIIAlphabet2(self):
        self.createASCIIAlphabet2()
        numbers = 0
        alpha_word = ""
        for it in self.ASCIIAlphabet2.items():
            if numbers == 6 or numbers == 12 or numbers == 18 or numbers == 24 or numbers == 30:
                alpha_word = alpha_word + "\n"
            numbers = numbers + 1
            alpha_word = alpha_word + str(it) + "\t"
        self.input_bin_alphabet.setText(alpha_word)

    def button_code_input_word_clicked(self):
        self.start_clear()
        word = self.input_word_to_be_code.text().upper()
        keyword = self.input_key.text().upper()
        self.ASCIIAlphabet2.clear()
        self.createASCIIAlphabet2()
        for letter in word:
            for item in self.ASCIIAlphabet2:
                if item == letter:
                    self.letters_to_bin.append(self.ASCIIAlphabet2[item])
        for letter in keyword:
            for item in self.ASCIIAlphabet2:
                if item == letter:
                    self.keyword_to_bin.append(self.ASCIIAlphabet2[item])
        if len(self.keyword_to_bin) < len(self.letters_to_bin):
            count_diff = len(self.letters_to_bin) - len(self.keyword_to_bin)
            for val in self.keyword_to_bin:
                if count_diff != 0:
                    self.keyword_to_bin.append(val)
                    count_diff -= 1
        code_word = ""
        index = 0
        for idx, i in enumerate(self.letters_to_bin):
            while index != len(self.letters_to_bin[idx]):
                code_word = code_word + str(int(i[index]) ^
                                            int(self.keyword_to_bin[idx][index]))
                index = index + 1
            self.encrypted_word.append(code_word)
            code_word = ""
            index = 0
        coded_word = ""
        for enc_word in self.encrypted_word:
            self.decode_alpha.append(int(enc_word, 2))
            coded_word = coded_word + str(int(enc_word, 2)) + "(" + str(enc_word) + ")" + " "
        self.input_coded_word.setText(coded_word)

    def button_decode_input_word_clicked(self):
        decode_alpha = []
        for val_dec, key_bin in zip(self.decode_alpha, self.keyword_to_bin):
            decode_alpha.append(int(val_dec) ^ int(key_bin, 2))
        decode_word = ""
        for dec_code in decode_alpha:
            for key in self.ASCIIAlphabet10().keys():
                if dec_code == self.ASCIIAlphabet10().get(key):
                    decode_word = decode_word + key
        self.input_decoded_word.setText(decode_word.capitalize())

    def start_clear(self):
        self.ASCIIAlphabet2, self.Alphabet10_2 = {}, {}
        self.letters_to_bin, self.keyword_to_bin, self.decode_alpha, self.encrypted_word = [], [], [], []
        self.input_coded_word.setText("")
        self.input_decoded_word.setText("")

    @staticmethod
    def ASCIIAlphabet10():
        return {
            "А": 128, "Б": 129, "В": 130, "Г": 131, "Д": 132, "Е": 133,
            "Ё": 134, "Ж": 135, "З": 136, "И": 137, "Й": 138, "К": 139,
            "Л": 140, "М": 141, "Н": 142, "О": 143, "П": 144, "Р": 145,
            "С": 146, "Т": 147, "У": 148, "Ф": 149, "Х": 150, "Ц": 151,
            "Ч": 152, "Ш": 153, "Щ": 154, "Ъ": 155, "Ы": 156, "Ь": 157,
            "Э": 158, "Ю": 159, "Я": 160
        }


def Main():
    app = QApplication([])
    win = MainWindow()
    win.setFixedSize(QSize(1400, 550))
    win.show()
    app.exec()


if __name__ == '__main__':
    Main()
