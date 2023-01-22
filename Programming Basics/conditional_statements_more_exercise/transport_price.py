kilometres = int(input())
day_night = input()

tax = 0

if kilometres >= 100:
    if day_night == "day":
        tax = 0.06 * kilometres
    elif day_night == "night":
        tax = 0.06 * kilometres
elif kilometres >= 20:
    if day_night == "day":
        tax = 0.09 * kilometres
    elif day_night == "night":
        tax = 0.09 * kilometres
else:
    if day_night == "day":
        tax = (0.79 * kilometres) + 0.7
    elif day_night == "night":
        tax = (0.90 * kilometres) + 0.7

print(f"{tax:.2f}")
