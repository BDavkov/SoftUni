a = int(input())
b = int(input())
c = int(input())
d = int(input())

last1 = a + c
last2 = b + d

for i in range(a, last1 + 1):
    count1 = 0
    for k in range(1, i + 1):
        if i % k == 0:
            count1 += 1

    if count1 <= 2:
        for j in range(b, last2 + 1):
            count2 = 0
            for h in range(1, j + 1):
                if j % h == 0:
                    count2 += 1

            if count2 <= 2:
                print(f"{i}{j}")
