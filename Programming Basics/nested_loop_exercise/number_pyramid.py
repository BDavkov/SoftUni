number = int(input())
current = 1
for row in range(1, number + 1):
    for col in range(1, row + 1):

        print(current, end=" ")
        current += 1
        if current > number:
            break

    if current > number:
        break

    print()
