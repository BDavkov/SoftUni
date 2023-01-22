chicken = int(input())
fish = int(input())
vegan = int(input())

chicken_price = chicken * 10.35
fish_price = fish * 12.4
vegan_price = vegan * 8.15
dessert = (chicken_price + fish_price + vegan_price) * 0.2

all_sum = chicken_price + fish_price + vegan_price + dessert + 2.5

print(all_sum)