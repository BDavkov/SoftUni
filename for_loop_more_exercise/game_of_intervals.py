moves = int(input())
points = 0
n1_count = 0
n2_count = 0
n3_count = 0
n4_count = 0
n5_count = 0
invalid_numbers = 0
for i in range(1, moves + 1):
    current_number = int(input())
    if 0 <= current_number <= 9:
        points += 0.2 * current_number
        n1_count += 1
    elif 10 <= current_number <= 19:
        points += 0.3 * current_number
        n2_count += 1
    elif 20 <= current_number <= 29:
        points += 0.4 * current_number
        n3_count += 1
    elif 30 <= current_number <= 39:
        points += 50
        n4_count += 1
    elif 40 <= current_number <= 50:
        points += 100
        n5_count += 1
    else:
        points /= 2
        invalid_numbers += 1

n1_percent = n1_count / moves * 100
n2_percent = n2_count / moves * 100
n3_percent = n3_count / moves * 100
n4_percent = n4_count / moves * 100
n5_percent = n5_count / moves * 100
invalid_percent = invalid_numbers / moves * 100
print(f"{points:.2f}")
print(f"From 0 to 9: {n1_percent:.2f}%")
print(f"From 10 to 19: {n2_percent:.2f}%")
print(f"From 20 to 29: {n3_percent:.2f}%")
print(f"From 30 to 39: {n4_percent:.2f}%")
print(f"From 40 to 50: {n5_percent:.2f}%")
print(f"Invalid numbers: {invalid_percent:.2f}%")
