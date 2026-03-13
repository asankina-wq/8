text = input("Введите ваш текст: ")

for letter in text:
    if text.count(letter) == 3:
        print("Элемент, встречающийся ровно 3 раза:", letter)
        break
