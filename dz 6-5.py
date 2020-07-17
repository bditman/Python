# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
# класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом
# из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры
# классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = "Какое-то название"

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("В это классе я вывожу Pen")

class Pencil(Stationery):
    def draw(self):
        print("В это классе я вывожу Pencil")

class Handle(Stationery):
    def draw(self):
        print("В это классе я вывожу Handle")

s = Stationery()
s.draw()
p = Pen()
p.draw()
p_2 = Pencil()
p_2.draw()
h = Handle()
h.draw()