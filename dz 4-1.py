import sys

arg_1, arg_2, arg_3 = map(float, sys.argv[1:])
pay = arg_1 * arg_2 + arg_3
print(f"Выработка в часах составляет: {arg_1} часов")
print(f"Ставка в часах составляет: {arg_2} рублей/час")
print(f"Премия составляет: {arg_3} рублей")
print(f"Зарплата за месяц составляет: {pay} рублей")