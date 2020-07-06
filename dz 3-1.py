def division(x, y):
    try:
        z = x / y
        print(z)
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")


try:
    division(x=int(input("Введите делимое: ")), y=int(input("Введите делитель: ")))
except ValueError:
    print("Введите число!")
