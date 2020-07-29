class My_class(Exception):
    def __init__(self, text):
        self.text = text


while True:
    result = []
    in_data = input("Если хотите завершить программу нажмите 'q' \n"
                    "Введиче числа через пробел: ")
    if in_data == "q":
        print("Bye bye")
        break
    else:
        for i in in_data.split():
            try:
                if i.isdigit():
                    result.append(i)
                else:
                    raise My_class("Вы ввели строку. Нужно вводить только числа. Будьте внимательны!")
            except My_class as err:
                print(err)
    print("Список состоящий из чисел ", result)
