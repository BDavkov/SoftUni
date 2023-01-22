needed_money = int(input())
pays = 0
cs_pays = 0
cs_sum = 0
cc_pays = 0
cc_sum = 0
flag = False

while True:
    current_sum = input()
    if current_sum == "End":
        flag = True
        break

    pays += 1
    current_sum = int(current_sum)

    if pays % 2 != 0:
        if current_sum > 100:
            print("Error in transaction!")
        else:
            cs_pays += 1
            cs_sum += current_sum
            print("Product sold!")
    else:
        if current_sum < 10:
            print("Error in transaction!")
        else:
            cc_pays += 1
            cc_sum += current_sum
            print("Product sold!")

    if needed_money <= (cc_sum + cs_sum):
        break

if cs_pays > 0:
    avg_cs = cs_sum / cs_pays
else:
    avg_cs = 0

if cc_pays > 0:
    avg_cc = cc_sum / cc_pays
else:
    avg_cc = 0

if flag:
    print("Failed to collect required money for charity.")
else:
    print(f"Average CS: {avg_cs:.2f}\nAverage CC: {avg_cc:.2f}")
