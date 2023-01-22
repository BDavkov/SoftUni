ticket = (input())
rows = int(input())
columns = int(input())

all_seats = rows * columns
price = 0
if ticket == "Premiere":
    price = all_seats * 12
elif ticket == "Normal":
    price = all_seats * 7.5
elif ticket == "Discount":
    price = all_seats * 5

print(f"{price:.2f} leva")
