user_num = int(input("Введите колчисетво секунд: "))
hour = user_num // 3600
min = (user_num % 3600) // 60
sec = user_num % 60
print(f"{hour:02d}:{min:02d}:{sec:02d}")

