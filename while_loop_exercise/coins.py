from math import floor
exchance = float(input())
coins = floor(exchance * 100)
count_coins = 0

while True:
    if coins >= 200:
        count_coins = coins // 200
        coins = coins % 200
    elif coins >= 100:
        count_coins += coins // 100
        coins = coins % 100
    elif coins >= 50:
        count_coins += coins // 50
        coins = coins % 50
    elif coins >= 20:
        count_coins += coins // 20
        coins = coins % 20
    elif coins >= 10:
        count_coins += coins // 10
        coins = coins % 10
    elif coins >= 5:
        count_coins += coins // 5
        coins = coins % 5
    elif coins >= 2:
        count_coins += coins // 2
        coins = coins % 2
    elif coins == 1:
        count_coins += 1
        coins = 0

    if coins == 0:
        break

print(f"{count_coins:.0f}")