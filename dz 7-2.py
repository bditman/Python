from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, num):
        self.num = num

    @abstractmethod
    def expense(self):
        pass

    def __add__(self, other):
        return self.expense + other.expense

class Coat(Clothes):
    @property
    def expense(self):
        print(f"Расход ткани на пальто: {round(self.num / 6.5 + 0.5)}")
        return round(self.num / 6.5 + 0.5)

class Costume(Clothes):
    @property
    def expense(self):
        print(f"Расход ткани на костюм: {2 * self.num + 0.3}")
        return 2 * self.num + 0.3

c = Coat(20)
cos = Costume(55)
print(f"Общий расход ткани: {c + cos}")