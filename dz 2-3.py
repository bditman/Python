num_month = int(input("Введите номер месяца: "))
#через словарь
month = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
for key in month.keys():
    if num_month in month[key]:
        print(key)

#через список
seasons = ["Зима", "Весна", "Лето", "Осень"]
if num_month == 12 or num_month == 1 or num_month == 2:
    print(seasons[0])
elif num_month == 3 or num_month == 4 or num_month == 5:
    print(seasons[1])
elif num_month == 6 or num_month == 7 or num_month == 8:
    print(seasons[2])
else:
    print(seasons[3])

