ticket_number = 0

while True:
    ticket = input("Введите ваш билет: ")
    ticket_number += 1
    
    if len(ticket) % 2 == 0:
        half = len(ticket) // 2
        if sum(int(num) for num in ticket[:half]) == sum(int(num) for num in ticket[half:]):
            print("Счастливый билет:", ticket_number)
            break
