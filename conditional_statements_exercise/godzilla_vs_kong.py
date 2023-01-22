budget = float(input())
actors_count = int(input())
price_suit_per_actor = float(input())

decor = budget * 0.1
suit_price = actors_count * price_suit_per_actor

if actors_count > 150:
    suit_price -= 0.1 * suit_price

total_sum = decor + suit_price

if total_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_sum - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_sum:.2f} leva left.")
