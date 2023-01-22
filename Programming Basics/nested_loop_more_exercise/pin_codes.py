a, b, c = int(input()), int(input()), int(input())
count = 0

for i in range(1, a + 1):
    if i % 2 == 0:
        for k in range(2, b + 1):
            count = 0
            for j in range(1, k + 1):
                if k % j == 0:
                    count += 1

            if count <= 2:
                for l in range(1, c + 1):
                    if l % 2 == 0:
                        print(f"{i} {k} {l}")
