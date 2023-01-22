from sys import maxsize
number = int(input())

total = 0
max_number = -maxsize
for i in range(1, number + 1):
    current_number = int(input())
    total += current_number
    if current_number > max_number:
        max_number = current_number

without_max = total - max_number

if max_number == without_max:
    print(f"Yes")
    print(f"Sum = {without_max}")
else:
    diff = abs(max_number - without_max)
    print(f"No")
    print(f"Diff = {diff}")
