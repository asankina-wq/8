text = input("Введите ваш текст: ")
words = text.split()
first_word = words[0]
for word in words[1:]:
    if  not word == first_word and len(word) == len(set(word)):
      print(word)