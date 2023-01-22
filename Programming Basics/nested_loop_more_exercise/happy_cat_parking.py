days = int(input())
hours = int(input())
total = 0

for i in range(1, days + 1):
    price = 0
    if i % 2 == 0:
        for k in range(1, hours + 1):
            if k % 2 != 0:
                price += 2.5
            else:
                price += 1
    else:
        for h in range(1, hours + 1):
            if h % 2 == 0:
                price += 1.25
            else:
                price += 1

    print(f"Day: {i} - {price:.2f} leva")
    total += price
print(f"Total: {total:.2f} leva")
