num = int(input())

for i in range(1, num + 1):
    for k in range(1, num + 1):
        if (i == 1 and k == 1) or (i == 1 and k == num) or (i == num and k == 1) or (i == num and k == num):
            print("+", end=" ")
        elif k == 1 or k == num:
            print("|", end=" ")
        else:
            print("-", end=" ")
    print()
