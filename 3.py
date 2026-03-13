text = input("Введите ваш текст: ")
letters = set()

for letter in text:
    if letter.isalpha():
        letters.add(letter.lower())
        
print("Количество разных букв: ", len(letters))
