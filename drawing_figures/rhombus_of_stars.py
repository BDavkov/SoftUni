num = int(input())

for i in range(1, num + 1):
    for k in range(i, num):
        print(" ", end="")
    print("* " * i, end="")
    print()

for j in range(num - 1, 0, -1):
    for l in range(j, num):
        print(" ", end="")
    print("* " * j, end="")
    print()