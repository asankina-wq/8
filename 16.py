text = input("Введите текст: ")
unclosed_parentheses = 0
for sym in text:
    if sym == "(":
        unclosed_parentheses += 1
    elif sym == ")":
        unclosed_parentheses -= 1
        if unclosed_parentheses  < 0:
            print("Скобки расставлены неправильно")
            exit()
if unclosed_parentheses  == 0:
    print("Скобки расставлены правильно")
else:
    print("Скобки расставлены неправильно")