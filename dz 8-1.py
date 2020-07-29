class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def num(cls):
        number = []
        for el in Data("12-11-2034").data.split("-"):
            i = int(el)
            number.append(i)
        return number

    @staticmethod
    def new_data():
        if Data.num()[0] > 31 or Data.num()[0] < 1:
            print("Количество дней в месяце от 1 до 31")
        elif Data.num()[1] > 12 or Data.num()[1] < 1:
            print("Количество месяцев в году от 1 до 12")
        elif Data.num()[2] < 0:
            print("Введите положительное число")
        else:
            print(f"{Data.num()[0]}-{Data.num()[1]}-{Data.num()[2]}")


d = Data("12-12-2034")
print(d.num())
d.new_data()
