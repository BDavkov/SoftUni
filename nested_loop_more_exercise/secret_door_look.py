a = int(input())
b = int(input())
c = int(input())

for i in range(2, a + 1):
    if i % 2 == 0:
        for k in range(2, b + 1):
            if k == 2 or k == 3 or k == 5 or k == 7:
                for j in range(2, c + 1):
                    if j % 2 == 0:
                        print(f"{i} {k} {j}")
