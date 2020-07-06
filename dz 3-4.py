# вариант для проверки
def my_func(x, y):
    degree = x ** y
    return degree


# вариант со встроенной функцией (из методички, но мы не проходили импорт пока)
import math
def my_func2(x, y):
    if y == 0:
        return 1
    elif y < 0:
        degree = math.pow(x, y)
    return degree

#вариант с циклом
def my_func3(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y > 0:
         print("Степень должна быть отрицательной!")
    elif y == 0:
        return 1
    else:
        return 1 / result


x = int(input("Введиче натуральное число: "))
y = int(input("Введиче отрицательное число для возведения в степень: "))
print(f"Решение через встроенную функцию: {my_func(x, y)}")
print(f"Решение через импорт: {my_func2(x, y)}")
print(f"Решение через цикл: {my_func3(x, y)}")
