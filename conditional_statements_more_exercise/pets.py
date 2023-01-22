import math

days = int(input())
food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

dog_food = days * dog_food_per_day
cat_food = days * cat_food_per_day
turtle_food = days * (turtle_food_per_day / 1000)
total_food = dog_food + cat_food + turtle_food

diff = abs(total_food - food_left)

if total_food <= food_left:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")
