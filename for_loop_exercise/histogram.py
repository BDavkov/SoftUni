numbers = int(input())
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0
p6_count = 0
for i in range(1, numbers + 1):
    current_number = int(input())
    if current_number < 200:
        p1_count += 1
    elif current_number < 400:
        p2_count += 1
    elif current_number < 600:
        p3_count += 1
    elif current_number < 800:
        p4_count += 1
    else:
        p5_count += 1

p1 = p1_count / numbers * 100
p2 = p2_count / numbers * 100
p3 = p3_count / numbers * 100
p4 = p4_count / numbers * 100
p5 = p5_count / numbers * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
