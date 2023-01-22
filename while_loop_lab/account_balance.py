total_money = 0

while True:
    current_money = input()
    if current_money == "NoMoreMoney":
        print(f"Total: {total_money:.2f}")
        break

    current_money = float(current_money)

    if current_money >= 0:
        print(f"Increase: {current_money:.2f}")
    elif current_money < 0:
        print(f"Invalid operation!\nTotal: {total_money:.2f}")
        break

    total_money += current_money
