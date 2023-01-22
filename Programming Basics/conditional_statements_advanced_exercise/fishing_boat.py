budget = int(input())
season = input()
count_fishers = int(input())

price = 0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if count_fishers <= 6:
    price -= price * 0.1
elif 6 < count_fishers <= 11:
    price -= price * 0.15
elif count_fishers > 11:
    price -= price * 0.25

if count_fishers % 2 == 0 and season != "Autumn":
    price -= price * 0.05

diff = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
