# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random

sum = 0
with open("sum.txt", "w", encoding="utf-8") as file:
    for i in range(1, 20):
        num = random.randint(1, 100)
        file.write(str(num) + " ")
        sum += num
    print(f"Сумма рандомных чисел = {sum}")