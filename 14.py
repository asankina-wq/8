hint = input("Введите подсказку: ")
word = input("Введите загаданное слово: ")
print("\n" * 25)
current = "*" * len(word)
attempts = 10
print(hint)
print(current)
while attempts > 0:
    choice = input("Буква или слово (0 - буква, 1 - слово)? ")
    if choice == "0":
        letter = input("Введите букву: ")
        new_current = ""
        for sym in range(len(word)):
            if word[sym] == letter:
                new_current += letter
            else:
                new_current += current[sym]
        current = new_current
        print(current)
        if current == word:
            print("Победа!")
            break
    elif choice == "1":
        guess = input("Введите слово: ")
        if guess == word:
            print("Победа!")
            break
        else:
            print("Неверно!")
    attempts -= 1
else:
    print("Проигрыш!")