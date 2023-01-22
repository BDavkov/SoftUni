days = int(input())
place = input()
evaluation = input()
nights = days - 1
discount = 0

if place == "apartment":
    if days < 10:
        discount = 0.3
    elif 10 <= days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.5
elif place == "president apartment":
    if days < 10:
        discount = 0.1
    elif 10 <= days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.2

price = 0
if place == "room for one person":
    price = nights * 18
elif place == "apartment":
    price = (nights * 25) * (1 - discount)
elif place == "president apartment":
    price = (nights * 35) * (1 - discount)

if evaluation == "positive":
    price += price * 0.25
if evaluation == "negative":
    price -= price * 0.1

print(f"{price:.2f}")
