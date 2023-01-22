season = input()
sex = input()
students_count = int(input())
nights_count = int(input())
price_per_night = 0
sport = 0

if season == "Winter":
    if sex == "boys":
        price_per_night = students_count * 9.6
    elif sex == "girls":
        price_per_night = students_count * 9.6
    elif sex == "mixed":
        price_per_night = students_count * 10
elif season == "Spring":
    if sex == "boys":
        price_per_night = students_count * 7.2
    elif sex == "girls":
        price_per_night = students_count * 7.2
    elif sex == "mixed":
        price_per_night = students_count * 9.5
elif season == "Summer":
    if sex == "boys":
        price_per_night = students_count * 15
    elif sex == "girls":
        price_per_night = students_count * 15
    elif sex == "mixed":
        price_per_night = students_count * 20

price = price_per_night * nights_count
if students_count >= 50:
    price = price * 0.5
elif 20 <= students_count < 50:
    price = price * 0.85
elif 10 <= students_count < 20:
    price = price * 0.95

if sex == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
elif sex == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif sex == "mixed":
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"

print(f"{sport} {price:.2f} lv.")
