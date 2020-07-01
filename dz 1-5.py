revenue = int(input("Введите сумму выручки вашей фирмы: "))
expenses = int(input("Введите сумму затрат вашей фирмы: "))
if revenue > expenses:
    print("Фирма работает с прибылью :)")
    rent = (revenue - expenses) / revenue
    print(f"Рентабельность фирмы состовляет {rent}%")
    user = int(input("Введите количество работников фирмы: "))
    print(f"Прибыль фирмы из расчета на каждого сотрудника {rent / user}%")
else:
    print("Фирма работает с убытком :(")