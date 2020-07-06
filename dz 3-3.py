def my_func(x, y, z):
    if x + y > y + z:
        sum_max = x + y
        return sum_max
    elif x + y > x + z:
        sum_max = x + z
        return sum_max
    else:
        sum_max = y + z
        return  sum_max


def my_func2(x, y, z):
    numbers = [x, y, z]
    numbers.remove(min(numbers))
    return sum(numbers)


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
print(f"Вы ввели 3 числа {num1}, {num2}, {num3} - сумма максимальных "
      f"двух числе составила {my_func(num1, num2, num3)}")
print(f"Второй вариант: {my_func2(num1, num2, num3)}")
