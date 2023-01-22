number = int(input())

combination_count = 0

for a in range(0, number + 1):
    for b in range(0, number + 1):
        for c in range(0, number + 1):
            if a + b + c == number:
                combination_count += 1

print(combination_count)
