days = int(input())
win_count = 0
all_money = 0
current_money = 0
lose_count = 0
win_day = 0
lose_day = 0
for i in range(1, days + 1):
    while True:
        sport = input()
        if sport == "Finish":
            if win_count > lose_count:
                current_money *= 1.1
                win_day += 1
            else:
                lose_day += 1

            all_money += current_money
            current_money = 0
            win_count = 0
            lose_count = 0
            break
        result = input()

        if result == "win":
            win_count += 1
            current_money += 20
        elif result == "lose":
            lose_count += 1

if win_day > lose_day:
    all_money *= 1.2
    print(f"You won the tournament! Total raised money: {all_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {all_money:.2f}")
