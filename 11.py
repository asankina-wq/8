cities = input("Введите города через пробел: ").split()

for index, city in enumerate(cities[1:], start=1):
    if city[0].lower() != cities[index - 1][-1].lower():
        winner = "Петя" if index % 2 == 0 else "Вася"
        break
else:
    winner = "Вася" if (len(cities) - 1) % 2 == 0 else "Петя"

print("Победитель:", winner)
