text = input("Введите ваш текст: ")
count = {}
for letter in text:
    if letter in count:
        count[letter] +=1
    else:
        count[letter] = 1
for letter in count:
    if count[letter] ==3:
        print("Элемент, встречающийся ровно 3 раза: ", letter)
        break