# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше
# усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class TrafficLight:
    color = ["Red", "Yellow", "Green"]

    def running(self):
        i = 0
        while i < 300:
            print(f"Светофор переключается\n{TrafficLight.color[i]}")
            if TrafficLight.color[i] == "Red":
                time.sleep(7)
            elif TrafficLight.color[i] == "Yellow":
                time.sleep(2)
            elif TrafficLight.color[i] == "Green":
                time.sleep(7)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
