user_num = int(input("Введите количество элементов списка "))
list = []
i = 0
while i < user_num:
    list.append(input("Введите следующее значение списка "))
    i += 1
for element in range(0, len(list), 2):
    j = 0
    list[j], list[j + 1] = list [j + 1], list[j]
print(list)
