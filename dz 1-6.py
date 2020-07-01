'''
num1 = int(input("Сколько километров вы пробежали в первый день? "))
num2 = int(input("К какому результату вы стремитесь? "))
day = 1
print(f"День {day}: {num1} км")
while num1 <= num2:
    num1 = num1 + (num1 * 0.1)
    day += 1
    print(f"День {day}: {num1:.2f} км")
'''

print(int('11100', 2))