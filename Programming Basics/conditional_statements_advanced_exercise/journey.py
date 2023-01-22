budget = float(input())
season = input()

price = 0
location = ""
place = ""
if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        price = 0.3 * budget
        place = "Camp"
    elif season == "winter":
        price = 0.7 * budget
        place = "Hotel"
elif budget <= 1000:
    location = "Balkans"
    if season == "summer":
        price = 0.4 * budget
        place = "Camp"
    elif season == "winter":
        price = 0.8 * budget
        place = "Hotel"
elif budget > 1000:
    location = "Europe"
    place = "Hotel"
    price = 0.9 * budget

print(f"Somewhere in {location}")
print(f"{place} - {price:.2f}")
