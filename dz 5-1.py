with open("test.txt", "w", encoding="utf-8") as test:
    while True:
        user_text = input("Enter strings: ")
        test.write(user_text + "\n")
        if user_text == "":
            break