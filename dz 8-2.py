class Null(Exception):
    def __init__(self, text):
        self.text = text


param_1 = input("Введите делимое: ")
param_2 = input("Введите делитель: ")
try:
    param_1 = int(param_1)
    param_2 = int(param_2)
    if param_2 == 0:
        raise Null("Делитель не должен быть равен нулю")
    result = param_1 / param_2
except ValueError:
    print("Нужно вводить только числа")
except Null as n:
    print(n)
else:
    print(f"Результат деления {result}")
