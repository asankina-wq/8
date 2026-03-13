text = input("Введите ваш текст: ")
words = text.split()

for word in words:
    if words.count(word) == 2:
        print("Слово, повторяющееся дважды:", word)
        break
