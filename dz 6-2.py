class Road:
    mass = 30
    thickness = 3
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def result(self):
        print(F"Масса асфальта = {self._width * self._length * Road.mass * Road.thickness} тн")


r = Road(2000, 3)
r.result()