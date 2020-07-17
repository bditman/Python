# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

dict_translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("translate.txt", "a", encoding="utf-8") as new:
    with open("numbers.txt", encoding="utf-8") as file:
        num = file.read().split("\n")
        for i in num:
            i = i.split(" - ")
            new.writelines(dict_translate[i[0]] + " - " + i[1] + "\n")