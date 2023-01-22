inherited_money = float(input())
year_to_live = int(input())

money = 0
spend = 0
for i in range(0, year_to_live - 1799):
    if i % 2 == 0:
        spend += 12000
    else:
        money = ((i + 18) * 50) + 12000
        spend += money

diff = abs(inherited_money - spend)
if inherited_money >= spend:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
