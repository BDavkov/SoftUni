l = float(input()) #ДЪЛЖИНА
w = float(input()) #ШИРИНА

length = l * 100
length_count = length // 120

width = w * 100
width_count = (width - 100) // 70

places = (length_count * width_count) - 3

print(f"{places:.0f}")
