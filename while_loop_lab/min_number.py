import sys

min_number = sys.maxsize

while True:
    current_number = input()
    if current_number == "Stop":
        print(min_number)
        break

    current_number = int(current_number)

    if current_number < min_number:
        min_number = current_number
