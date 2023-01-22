age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money = 0
total_money = 0
toy_count = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        toy_count += 1
    else:
        money += 10
        total_money += money - 1

total_money += toy_count * toy_price
diff = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


