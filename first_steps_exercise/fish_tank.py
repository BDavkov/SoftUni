lenght = int(input())
width = int(input())
height = int(input())
interest = float(input())

capacity = lenght * width * height
capacity_leters = capacity / 1000

needed = capacity_leters - (capacity_leters * (interest / 100))

print(needed)