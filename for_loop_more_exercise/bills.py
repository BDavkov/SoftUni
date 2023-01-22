months = int(input())

electricity = 0
water = 0
internet = 0
others = 0
for i in range(1, months + 1):
    current_electricity = float(input())
    electricity += current_electricity
    water += 20
    internet += 15
    others += (current_electricity + 20 + 15) * 1.2

avg = (electricity + water + internet + others) / months
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {avg:.2f} lv")
