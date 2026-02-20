text = input("Введите ваш текст: ")
max_spaces = 0
current_spaces = 0
for symbol in text:
    if symbol.isspace():
        current_spaces += 1
        if max_spaces < current_spaces:
            max_spaces = current_spaces
    else:
        current_spaces = 0
print(" Максимальное количество: ", max_spaces)