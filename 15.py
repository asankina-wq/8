secret = input("Ведущий, введите 4-значное число без повторяющихся цифр: ")
print("\n" * 25)
attempts = 10

while attempts > 0:
    guess = input("Попытка игрока: ")
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    print("Быков:", bulls, "Коров:", cows)
    if bulls == 4:
        print("Победа!")
        break
    attempts -= 1
else:
    print("Проигрыш!")