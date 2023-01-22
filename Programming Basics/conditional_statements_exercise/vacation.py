budget = float(input())
season = input()
location = 0
settlement = 0
price = 0

if budget <= 1000:
    settlement = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = 0.65 * budget
        print(f"{location} - {settlement} - {price:.2f}")
    elif season == "Winter":
        location = "Morocco"
        price = 0.45 * budget
        print(f"{location} - {settlement} - {price:.2f}")
elif 1000 < budget <= 3000:
    settlement = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = 0.8 * budget
        print(f"{location} - {settlement} - {price:.2f}")
    elif season == "Winter":
        location = "Morocco"
        price = 0.6 * budget
        print(f"{location} - {settlement} - {price:.2f}")
elif budget > 3000:
    settlement = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = 0.9 * budget
        print(f"{location} - {settlement} - {price:.2f}")
    elif season == "Winter":
        location = "Morocco"
        price = 0.9 * budget
        print(f"{location} - {settlement} - {price:.2f}")
