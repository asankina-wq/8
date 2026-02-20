import keyword
name = input("Введите имя для проверки: ")
empty = not name
digit_start = name[0].isdigit()
is_keyword = keyword.iskeyword(name)
if empty or digit_start or is_keyword:
    print("Не может быть именем")
else:
    for letter in name:
        available_letter = letter.isalpha() or letter.isdigit() or letter == '_'
        if not available_letter:
            print("Не может быть именем")
            break
    else:
        print("Может быть именем")