month = input()
nights = int(input())

# May, June, July, August, September или October;
price_per_night1 = 0
price_per_night2 = 0
place1 = "Studio"
place2 = "Apartment"

if month == "May" or month == "October":
    price_per_night1 = 50
    price_per_night2 = 65
elif month == "June" or month == "September":
    price_per_night1 = 75.2
    price_per_night2 = 68.7
elif month == "July" or month == "August":
    price_per_night1 = 76
    price_per_night2 = 77

full_price1 = price_per_night1 * nights
full_price2 = price_per_night2 * nights

if (month == "May" or month == "October") and nights > 14:
    full_price1 = full_price1 * 0.7
elif (month == "May" or month == "October") and 7 < nights <= 14:
    full_price1 = full_price1 * 0.95
elif (month == "June" or month == "September") and nights > 14:
    full_price1 = full_price1 * 0.8

if nights > 14:
    full_price2 = full_price2 * 0.9

print(f"Apartment: {full_price2:.2f} lv.")
print(f"Studio: {full_price1:.2f} lv.")
