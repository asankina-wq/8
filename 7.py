text = input("Введите ваш текст: ")
words = text.split()
length_words = [len(word) for word in words]
shortest_word = min(length_words)
print("Длина самого короткого слова: ", shortest_word)
