
class Person:
    # конструктор
    def __init__(self, name):
        self.name = name # устанавливаем имя
    def display_info(self):
            print("Привет, меня зовут", self.name)
    def __del__(self):
        print(self.name, "удален из памяти")

class Auto:
    def __init__(self, name):
        self.name = name
    def move(self, speed):
            print(self.name, "едет со скоростью", speed, "км/ч")

