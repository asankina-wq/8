text = input("Введите ваш текст: ")
words = text.split()
amount = {}
for word in words:
    if word in amount:
        amount[word] += 1
    else:
        amount[word] = 1
for word in amount:
    if amount[word] ==2:
        print("Слово, повторяющееся дважды: ", word)
