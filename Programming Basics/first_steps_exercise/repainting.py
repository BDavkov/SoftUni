nylon = int(input())
paint = int(input())
thinner = int(input())
workmen_hours = int(input())

nylon_price = (nylon + 2) * 1.5
paint_price = (paint * 1.1) * 14.5
thinner_price = thinner * 5
workmen_price = (((nylon_price + paint_price + thinner_price + 0.4) * 0.3) * workmen_hours)

all_price = nylon_price + paint_price + thinner_price + workmen_price + 0.4

print(all_price)