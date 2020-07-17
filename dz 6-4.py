import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"Скорость равна {self.speed} км/ч")

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self):
        direction = ["Север", "Юг", "Запад", "Восток", "Налево", "Направо"]
        print(f"Машина повернула на {random.choice(direction)}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Скорость больше 60 км/ч, сбавьте обороты")
        else:
            print("Вы едете по правилам")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Скорость больше 40 км/ч, сбавьте обороты")
        else:
            print("Вы едете по правилам")


class PoliceCar(Car):
    pass


# c = Car(100, "Red", "Mazda", False)
# c.show_speed()
t = TownCar(30, "Red", "Mazda", False)
t.show_speed()
w = WorkCar(50, "Red", "Mazda", False)
w.show_speed()

