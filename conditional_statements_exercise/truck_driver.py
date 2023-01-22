season = input()
kilometres = float(input())
distance = kilometres * 4
salary = 0

if kilometres <= 5000:
    if season == "Spring":
        salary = distance * 0.75
    elif season == "Autumn":
        salary = distance * 0.75
    elif season == "Summer":
        salary = distance * 0.9
    elif season == "Winter":
        salary = distance * 1.05
elif 5000 < kilometres <= 10000:
    if season == "Spring":
        salary = distance * 0.95
    elif season == "Autumn":
        salary = distance * 0.95
    elif season == "Summer":
        salary = distance * 1.1
    elif season == "Winter":
        salary = distance * 1.25
else:
    salary = distance * 1.45

salary -= salary * 0.1

print(f"{salary:.2f}")
