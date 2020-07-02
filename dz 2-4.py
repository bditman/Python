words = input("Введите несколько слов: ")
word = words.split()
for count, i in enumerate(word):
    if len(i) > 10:
        print(count + 1, f"{i:.10}")
    else:
        print(count + 1, i)