class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return f"Сложение клеток: {self.num + other.num}"

    def __sub__(self, other):
        if self.num > other.num:
            return f"Вычитание клеток: {self.num - other.num}"
        else:
            print("Первое число должно быть больше второго для вычитания")

    def __mul__(self, other):
        return f"Умножение клеток: {self.num * other.num}"

    def __truediv__(self, other):
        if other.num == 0:
            print("Второе число не должно быть нулем!")
        else:
            return f"Деление клеток: {round(self.num / other.num)}"

    def make_order(self, rows):
        return '\\n'.join(['*' * rows for _ in range(self.num // rows)]) + '\\n' + '*' * (self.num % rows)

x = Cell(10)
y = Cell(5)
print(x + y)
print(x - y)
print(x / y)
print(x * y)
print(x.make_order(4))
