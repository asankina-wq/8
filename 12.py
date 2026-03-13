import keyword

name = input("Введите имя для проверки: ")

if not name or name[0].isdigit() or keyword.iskeyword(name):
    print("Не может быть именем")
else:
    for char in name:
        if not (char.isalpha() or char.isdigit() or char == "_"):
            print("Не может быть именем")
            break
    else:
        print("Может быть именем")
