form = input()
from math import pi
area = 0

if form == "square":
    a = float(input())
    area = a * a
elif form == "rectangle":
    a, b = float(input()), float(input())
    area = a * b
elif form == "circle":
    r = float(input())
    area = (r * r) * pi
elif form == "triangle":
    a, h = float(input()), float(input())
    area = (a * h) / 2

print(f"{area:.3f}")
