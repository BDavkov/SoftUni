num = int(input())

for i in range(1, num + 1):
    for j in range(1, num + 1):
        for k in range(1, num + 1):
            for l in range(1, num + 1):
                if (i + j == k + l) and num % (i + j) == 0:
                    print(f"{i}{j}{k}{l}", end=" ")
