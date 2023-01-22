type_flowers = input()
count_flowers = int(input())
budget = int(input())

price = 0
if type_flowers == "Roses":
    price = count_flowers * 5
    if count_flowers > 80:
        price *= 0.9
elif type_flowers == "Dahlias":
    price = count_flowers * 3.8
    if count_flowers > 90:
        price *= 0.85
elif type_flowers == "Tulips":
    price = count_flowers * 2.8
    if count_flowers > 80:
        price *= 0.85
elif type_flowers == "Narcissus":
    price = count_flowers * 3
    if count_flowers < 120:
        price *= 1.15
elif type_flowers == "Gladiolus":
    price = count_flowers * 2.5
    if count_flowers < 80:
        price *= 1.2

diff = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
