import sys

max_number = -sys.maxsize

while True:
    current_number = input()
    if current_number == "Stop":
        print(max_number)
        break

    current_number = int(current_number)

    if current_number > max_number:
        max_number = current_number
