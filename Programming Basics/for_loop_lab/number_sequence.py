import sys
number = int(input())

min_number = sys.maxsize
max_number = -sys.maxsize

for i in range(number):
    current_number = int(input())
    if min_number > current_number:
        min_number = current_number
    if max_number < current_number:
        max_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
