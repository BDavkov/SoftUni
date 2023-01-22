budget = float(input())
season = input()
cabrio = 0
jeep = 0
car_class = 0

if budget <= 100:
    mobile_class = "Economy class"
    if season == "Summer":
        cabrio = 0.35 * budget
        car_class = "Cabrio"
    elif season == "Winter":
        car_class = "Jeep"
        jeep = 0.65 * budget

if 100 < budget <= 500:
    mobile_class = "Compact class"
    if season == "Summer":
        car_class = "Cabrio"
        cabrio = 0.45 * budget
    elif season == "Winter":
        car_class = "Jeep"
        jeep = 0.8 * budget

if budget > 500:
    car_class = "Jeep"
    mobile_class = "Luxury class"
    cabrio = 0.9 * budget
    jeep = 0.9 * budget

print(mobile_class)
if budget > 500:
    print(f"{car_class} - {jeep:.2f}")
elif budget <= 500:
    if season == "Summer":
        print(f"Cabrio - {cabrio:.2f}")
    elif season == "Winter":
        print(f"Jeep - {jeep:.2f}")
