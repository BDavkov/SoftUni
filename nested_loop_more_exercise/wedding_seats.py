last_sector = input()
first_rows = int(input())
odd_seats = int(input())
seat = 0
count = 0
for i in range(65, ord(last_sector) + 1):
    for k in range(1, first_rows + 1):
        if k % 2 != 0:
            for j in range(1, odd_seats + 1):
                seat = j + 96
                print(f"{chr(i)}{k}{chr(seat)}")
                count += 1
        elif k % 2 == 0:
            for l in range(1, odd_seats + 3):
                seat = l + 96
                print(f"{chr(i)}{k}{chr(seat)}")
                count += 1

    first_rows += 1
print(count)
