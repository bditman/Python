user_number = int(input("Введите любое натуральное число: "))
my_list = [7, 5, 3, 3, 2]
for i in range(len(my_list)):
    if user_number > my_list[i]:
        my_list.insert(i, str(user_number))
        break
    elif user_number <= my_list[-1]:
        my_list.append(str(user_number))
        break
print(my_list)

