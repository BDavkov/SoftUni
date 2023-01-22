needed_money = float(input())
available_money = float(input())
total_money = available_money
days = 0
spend_days = 0
flag = False

while total_money < needed_money:
    action = input()
    current_money = float(input())
    days += 1

    if action == "save":
        total_money += current_money
        spend_days = 0
    elif action == "spend":
        total_money -= current_money
        spend_days += 1
        if spend_days == 5:
            flag = True
            break
        elif total_money <= 0:
            total_money = 0

if flag:
    print(f"You can't save the money.\n{days}")
else:
    print(f"You saved the money for {days} days.")
