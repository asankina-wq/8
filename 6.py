text = input("Введите ваш текст: ")
words = text.split()
reversed_text = words [::-1]
result = ' '.join(reversed_text)
print(result)