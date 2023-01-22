travel_price = float(input())
puzzles_count = int(input())
talking_toys_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzles_price = puzzles_count * 2.6
talking_toys_price = talking_toys_count * 3
bears_price = bears_count * 4.1
minions_price = minions_count * 8.2
trucks_price = trucks_count * 2

total_price = puzzles_price + talking_toys_price + bears_price + minions_price + trucks_price
total_count = puzzles_count + talking_toys_count + bears_count + minions_count + trucks_count
if total_count >= 50:
    total_price -= total_price * 0.25
total_price -= total_price * 0.1

if total_price >= travel_price:
    print(f"Yes! {total_price - travel_price:.2f} lv left.")
else:
    print(f"Not enough money! {travel_price - total_price:.2f} lv needed.")