text = input("Введите ваш текст: ")
current_repeat = 1
max_repeat = 1
for symbol in range(1, len(text)):
    if text[symbol] == text[symbol-1]:
        current_repeat += 1
        if current_repeat > max_repeat:
            max_repeat = current_repeat
    else:
            current__repeat = 1
print(" Максимальное количество повторяющихся символов: " , max_repeat)
