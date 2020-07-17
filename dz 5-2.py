# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.

with open("test.txt", encoding="utf-8") as test:
    count = 0
    for i in test:
        count += 1
        word = i.split()
        print(f"Длина {count} строки равна {len(word)}")
    print(f"Всего строк {count}")
