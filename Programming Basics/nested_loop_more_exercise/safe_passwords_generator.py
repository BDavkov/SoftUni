a = int(input())
b = int(input())
max_pass = int(input())
A = 35
B = 64
count = 0

for i in range(1, a + 1):
    if count > max_pass:
        break

    for k in range(1, b + 1):
        count += 1
        if count > max_pass:
            break

        if A == 56:
            A = 35
        if B == 97:
            B = 64

        C = chr(A)
        D = chr(B)

        print(f"{C}{D}{i}{k}{D}{C}", end="|")
        A += 1
        B += 1
