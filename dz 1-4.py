number = int(input("Введиче любое число: "))
max = 0
while number > 0:
    if number % 10 > max:
        max = number % 10
    number //= 10
print(max)
