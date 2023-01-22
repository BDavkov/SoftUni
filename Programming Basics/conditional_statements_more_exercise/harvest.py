import math

grapes_yard = int(input())
kg_grapes_per_yard = float(input())
needed_wine = int(input())
workers = int(input())

total_wine = ((grapes_yard * kg_grapes_per_yard) / 2.5) * 0.4
diff = 0

if total_wine < needed_wine:
    diff = math.floor(abs(total_wine - needed_wine))
    print(f"It will be a tough winter! More {diff} liters wine needed.")
else:
    diff = abs(total_wine - needed_wine)
    print(f"Good harvest this year! Total wine: {math.floor(total_wine)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.ceil(diff / workers)} liters per person.")
