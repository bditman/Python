def my_func(text):
    words = text.split()
    result = []
    for i in text:
        if i.isupper() == True:
            return "Введите только маленькие буквы"
    for word in words:
        for i in word:
            if ord(i) < 97 or ord(i) > 122:
                return "Введите только латинские буквы"
        new_word = word.title()
        result.append(new_word)
    return " ".join(result)


user_text = input("Введите несколько слов через пробел: ")
print(my_func(user_text))
