product, day, count = input(), input(), float(input())
price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if product == "banana":
        price = 2.5
    elif product == "apple":
        price = 1.2
    elif product == "orange":
        price = 0.85
    elif product == "grapefruit":
        price = 1.45
    elif product == "kiwi":
        price = 2.7
    elif product == "pineapple":
        price = 5.5
    elif product == "grapes":
        price = 3.85

elif day == "Saturday" or day == "Sunday":
    if product == "banana":
        price = 2.7
    elif product == "apple":
        price = 1.25
    elif product == "orange":
        price = 0.9
    elif product == "grapefruit":
        price = 1.6
    elif product == "kiwi":
        price = 3
    elif product == "pineapple":
        price = 5.6
    elif product == "grapes":
        price = 4.2

full_price = price * count

if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day ==
           "Saturday" or day == "Sunday") and (product == "banana" or product == "apple" or product == "kiwi" or
            product == "orange" or product == "grapefruit" or product == "pineapple" or product == "grapes"):
    print(f"{full_price:.2f}")
else:
    print("error")
