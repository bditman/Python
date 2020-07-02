count_user = int(input("Введите количество товаров, которые хотите добавить в систему: "))
count_max = 0
i = 0
list = []
while count_max != count_user:
    name = input("Введите название: ")
    price = int(input("Введите цену: "))
    quantity = int(input("Введите количество: "))
    unit = input("Введите еденицы измерения: ")
    items = (i + 1, {"Название": name, "Цена": price, "Количество": quantity, "Ед.изм": unit})
    list.append(items)
    count_max += 1
    i += 1
    x = {"Название": name, "Цена": price, "Количество": quantity, "Ед.изм": unit}
print(list)

