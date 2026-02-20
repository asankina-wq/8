cities = input("Введите города через пробел: ").split()
winner = None
for index_city in range(1, len(cities)):
    current_city = cities[index_city]
    previous_city = cities[index_city - 1]
    if current_city[0].lower() != previous_city[-1].lower():
        if index_city % 2 == 0:
            winner = "Вася"
        else:
            winner = "Петя"
        break

    if len(cities) % 2 == 0:
        winner = "Вася"
    else:
        winner = "Петя"

print("Победитель:", winner)