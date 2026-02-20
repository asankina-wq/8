text_1 = input("Введите текст: ")
text_2 = input("Введите текст: ")
text_3 = input("Введите текст: ")
set1 = set(text_1)
set2 = set(text_2)
set3 = set(text_3)
result = (set1 - set2 - set3) | (set2 - set1 - set3) | (set3 - set1 -set2)
for letter in result:
    print("Неповторяющийся элемент: ", letter)