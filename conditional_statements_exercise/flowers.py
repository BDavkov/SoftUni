chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
day = input()
price = 0
count = chrysanthemums + roses + tulips

if season == "Spring":
    price = (chrysanthemums * 2) + (roses * 4.1) + (tulips * 2.5)
    if day == "Y":
        price += price * 0.15
    if tulips > 7:
        price = price * 0.95
elif season == "Summer":
    price = (chrysanthemums * 2) + (roses * 4.1) + (tulips * 2.5)
    if day == "Y":
        price += price * 0.15
elif season == "Autumn":
    price = (chrysanthemums * 3.75) + (roses * 4.5) + (tulips * 4.15)
    if day == "Y":
        price += price * 0.15
elif season == "Winter":
    price = (chrysanthemums * 3.75) + (roses * 4.5) + (tulips * 4.15)
    if day == "Y":
        price += price * 0.15
    if roses >= 10:
        price = price * 0.9

if count > 20:
    price = price * 0.8

total = price + 2

print(f"{total:.2f}")
